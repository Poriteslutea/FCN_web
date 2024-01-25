from sqlmodel import Session, select
from pydantic import BaseModel
import sys
import os
current_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
sys.path.insert(0, parent_directory)
from models import StockReport, Product, Stock
from db import connect, engine
import yfinance as yf
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
from typing import List



class StockReportCreate(BaseModel):
    code: str
    date: str
    close: float
    ko_base: float
    ki_base: float
    ko_diff: float
    ki_diff: float
    is_ko: int
    is_ki: int



def create_report(report: StockReportCreate, session: Session):

    db_report = StockReport(code=report.code, 
                            date=report.date,
                            close=report.close,
                            ko_base=report.ko_base,
                            ki_base=report.ki_base,
                            ko_diff=report.ko_diff,
                            ki_diff=report.ki_diff,
                            is_ko=report.is_ko,
                            is_ki=report.is_ki)
    session.add(db_report)
    session.commit()
    session.refresh(db_report)

    return db_report


def get_hist_price(stock_code: List[str], start_date: str, end_date: str, price_type: str='Close') -> pd.DataFrame:

    stock_hist = yf.download(stock_code, start=start_date, end=end_date)[price_type]

    return stock_hist

def get_latest_price(stock_code: List[str], price_type: str='Close') -> dict:

    curr_date = datetime.today().strftime('%Y-%m-%d')
    start_date = (datetime.today() - timedelta(days=5)).strftime('%Y-%m-%d')
    stock_latest = get_hist_price(stock_code=stock_code, start_date=start_date, end_date=curr_date, price_type=price_type)
    stock_latest = stock_latest.reset_index()
    ret = stock_latest.to_dict("records")[-1]
    ret['Date'] = ret['Date'].strftime('%Y-%m-%d')
    
    return ret


def replace_after(df, condition_type, critical_val, replace_val):
    '''
    給一個dataframe或series，去判斷所有值是否大於、等於、小於、小於等於、大於等於critical_val，
    是的話就把符合條件的值全部替代成replace_val
    如果給定的dataframe不只一個column的話，只要有一個column符合條件，整個row都會換成replace_val 
    '''
    
    if condition_type not in {'<', '<=', '>', '>=', '=='}:
        return 
    if isinstance(df, pd.Series):
        dd = df.to_frame()
    else:
        dd = df.copy()
    condition_str = 'dd' + condition_type + str(critical_val)
    condition = eval(condition_str)
    init_date = dd[dd[condition].any(axis=1)].index
    if len(init_date) == 0:
        return dd
    else:
        init_date = init_date[0]
    init_idx = dd.index.get_loc(init_date)
    dd.iloc[(init_idx + 1):] = replace_val
    
    return dd


def get_hist_report(stock_code: List[str], 
                    start_date: str, 
                    end_date: str, 
                    start_trace_date: str,
                    ko_limit: float=1.0,
                    ki_limit: float=0.6, 
                    price_type: str='Close') -> pd.DataFrame:

    stock_hist = get_hist_price(stock_code=stock_code, start_date=start_date, end_date=end_date, price_type=price_type)

    # 得到與ko及ki的差距比例(%)
    ko_diff = stock_hist.sub(stock_hist.iloc[0] * ko_limit).div(stock_hist) * 100
    ki_diff = stock_hist.sub((stock_hist.iloc[0] * ki_limit)).div(stock_hist) * 100

    # 換一下column name，對不同dataframe加上後綴
    ko_diff = ko_diff.rename(columns={col: col+'_koDiff' for col in ko_diff.columns})
    ki_diff = ki_diff.rename(columns={col: col+'_kiDiff' for col in ki_diff.columns})

    # 當每支股票遇到ko差值大於等於0的情況時（目前價>=起始價) 後面都變nan值 （從起始追蹤日開始判斷)
    start_trace_dt = datetime.strptime(start_trace_date, '%Y-%m-%d')
    end_dt = datetime.strptime(end_date, '%Y-%m-%d')
    if start_trace_dt > end_dt:
        print('還未到達開始追蹤日期')
        merge_df = ko_diff.merge(ki_diff, left_index=True, right_index=True).merge(stock_hist, left_index=True, right_index=True)
        return merge_df
    elif start_trace_date not in stock_hist.index:
        raise ValueError('開始追蹤日期不能給假日(不能給沒開市的日期)')
    
    ts_list = []
    for c in ko_diff.columns:
        ts = replace_after(ko_diff[c].loc[start_trace_date:], '>=', 0, np.nan)
        ts_list.append(ts)
    ko = pd.concat(ts_list, axis=1)

    # 當每一支股票ko_diff都變nan時直接結束
    ko.dropna(how='all', inplace=True)

    # 把起始追蹤日期之前的資料合併進來
    init_idx = ko_diff.index.get_loc(start_trace_date)
    ko = pd.concat([ko_diff.iloc[:(init_idx)], ko])

    # 當其中一支股票的ki差值小於等於0時，後面的值都變nan（目前價<=（起始價×0.6）) (從產品起始日就開始判斷)
    ki = replace_after(ki_diff, '<=', 0, np.nan)

    # 將產品開始到產品結束（可能會因all ko而提前結束)的資料合併起來
    merge_df = ko.merge(ki, left_index=True, right_index=True).merge(stock_hist, left_index=True, right_index=True)

    return merge_df


def report_to_db(report: pd.DataFrame, product: Product):
    
    product_id = product.id 
    ko_limit = product.ko_limit
    ki_limit = product.ki_limit
    stock_id_list = [c for c in report.columns if '_' not in c]
    report.reset_index(inplace=True)
    report_rc = report.to_dict('records')
    base_row = report_rc[0]
    ret = []
    for row in report_rc:
        date = row['Date']
        for stock in stock_id_list:
            stock_report_row = {}
            stock_report_row['product_id'] = product_id
            stock_report_row['stock_id'] = stock
            stock_report_row['date'] = date
            stock_report_row['close'] = row[stock]
            stock_report_row['ko_base'] = base_row[stock] * ko_limit
            stock_report_row['ki_base'] = base_row[stock] * ki_limit
            stock_report_row['ko_diff'] = row[f'{stock}_koDiff']
            stock_report_row['ki_diff'] = row[f'{stock}_kiDiff']
            if (stock_report_row['ko_diff'] >= 0) or np.isnan(stock_report_row['ko_diff']):
                stock_report_row['is_ko'] = True
            if stock_report_row['ki_diff'] <= 0 or np.isnan(stock_report_row['ki_diff']):
                stock_report_row['is_ki']= True
            ret.append(stock_report_row)
    
    ret_df = pd.DataFrame(ret)
    ret_df.to_sql(name='stock_report', con=connect, if_exists='append')
    
    return ret_df
          


def import_product(product: Product):
    curr_dt = datetime.today()
    start_dt = datetime.strptime(product.start_date, '%Y-%m-%d')
    end_dt = datetime.strptime(product.end_date, '%Y-%m-%d')
   
    # 還沒開始
    if curr_dt < start_dt:
        print(f'產品：{product.id}還沒開始')
        return
    
    # 已過結束日期
    if curr_dt > end_dt:
        print(f'產品{product.id}已過期')
        return
    
    # 確認資料庫有沒有產品資料
    product_id = product.id
    stock_id_list = [st.id for st in product.stocks]
    curr_date = curr_dt.strftime('%Y-%m-%d')
    with Session(engine) as session:
        statement = select(StockReport).where(StockReport.product_id == product_id)
        results = session.exec(statement)
    
    
    if not results:
        # 資料庫還沒有產品資料（要進行初始化 - 從開始日期計算到當前日期，並將結果存至db中stock_report的table)
        df = get_hist_report(stock_code=stock_id_list, 
            start_date=product.start_date, 
            end_date=curr_date, 
            start_trace_date=product.start_trace_date, 
            ko_limit=product.ko_limit, 
            ki_limit=product.ki_limit,
            price_type=product.price_type) 
        report_to_db(report=df, product=product)
        print(f'產品{product_id}已初始化至資料庫')
    else:
        # 資料庫有產品資料，從資料庫目前存到的最後日期更新到現在日期
        latest_date = results.all()[0].Date
        latest_dt = datetime.strptime(latest_date, '%Y-%m-%d')
        if curr_dt > latest_dt:
            start_dt = latest_dt + timedelta(days=1)
            start_date = start_dt.strftime('%Y-%m-%d')
            df = get_hist_report(stock_code=stock_id_list, 
                start_date=start_date, 
                end_date=curr_date, 
                start_trace_date=product.start_trace_date, 
                ko_limit=product.ko_limit, 
                ki_limit=product.ki_limit,
                price_type=product.price_type) 
            report_to_db(report=df, product=product)
            print(f'產品{product_id}已更新至資料庫')
    
    print('以下為更新資料：')
    print(ret)

    return 

    




if __name__ == '__main__':
    stocks = ['AMD', 'NVDA', 'TSM', 'INTC']
    # 產品起始日期 （開始記錄每日收盤價、ko及ki價差）
    start_date = '2023-12-21'
    # 起始追蹤ko日期 （從這天開始，如果所有股票都Ko，直接結束)
    start_trace_date = '2024-01-02'
    # 產品預計結束日期 (沒有ko的話的結束日期)
    end_date = datetime.today().strftime('%Y-%m-%d') # 今日
    df = get_hist_report(stock_code=stocks, start_date=start_date, end_date=end_date, start_trace_date=start_trace_date)
    print(df)


    product_id = 'fcn' 
    ko_limit = 1
    ki_limit = 0.6
    stock_id_list = [c for c in df.columns if '_' not in c]
    df.reset_index(inplace=True)
    report_rc = df.to_dict('records')
    base_row = report_rc[0]
    ret = []
    for row in report_rc:
        date = row['Date']
        for stock in stock_id_list:
            stock_report_row = {}
            stock_report_row['product_id'] = product_id
            stock_report_row['stock_id'] = stock
            stock_report_row['date'] = date
            stock_report_row['close'] = row[stock]
            stock_report_row['ko_base'] = base_row[stock] * ko_limit
            stock_report_row['ki_base'] = base_row[stock] * ki_limit
            stock_report_row['ko_diff'] = row[f'{stock}_koDiff']
            stock_report_row['ki_diff'] = row[f'{stock}_kiDiff']
            stock_report_row['is_ko'] = (stock_report_row['ko_diff'] >= 0) or np.isnan(stock_report_row['ko_diff'])
            stock_report_row['is_ki']= stock_report_row['ki_diff'] <= 0 or np.isnan(stock_report_row['ki_diff'])
            ret.append(stock_report_row)
    
    ret_df = pd.DataFrame(ret)

    print(ret_df)


