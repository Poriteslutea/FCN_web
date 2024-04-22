from typing import List
from datetime import datetime

from fastapi import HTTPException, status, Depends
from sqlmodel import Session, select
from sqlalchemy.exc import IntegrityError


from db import get_session
from schema import StockReportResp
from model import DailyReport, Product
from service.hash import Hash



def get_latest_report(product_code: str,
                      session: Session=Depends(get_session)) -> List[StockReportResp]:
  
  latest_date_dt = session.exec(select(DailyReport.date).order_by(DailyReport.date.desc())).first()
  latest_date = latest_date_dt.strftime('%Y-%m-%d')
  product_id = session.exec(select(Product.id).where(Product.code == product_code)).first()
  latest_report = (session.query(DailyReport)
                  .filter(DailyReport.date == latest_date_dt)
                  .filter(DailyReport.product_id_fk == product_id)
                  .all())
  ret = []
  for stock in latest_report:
    stock_report = StockReportResp(
      date=latest_date,
      stock=stock.stock.code,
      close=stock.close,
      ko_base=stock.ko_base,
      ki_base=stock.ki_base,
      ko_diff=stock.ko_diff,
      ki_diff=stock.ki_diff,
      is_ko = stock.is_ko,
      is_ki=stock.is_ki
    )
    ret.append(stock_report)
  
  return ret



  




