from typing import List
from fastapi import HTTPException, status, Depends
from sqlmodel import Session, select
from sqlalchemy.exc import IntegrityError

from db import get_session
from schema import StockReportResp
from model import DailyReport
from service.hash import Hash



def get_latest_report(product_code: str,
                      session: Session=Depends(get_session)) -> StockReportResp:
  
  latest_date = session.exec(select(DailyReport.date).order_by(DailyReport.date.desc())).first()
  print(type(latest_date), latest_date)
  # session.query(DailyReport).filter(DailyReport.product_id_fk == product_id).all()
  

if __name__ == '__main__':
  res = get_latest_report('SLN35')
  print(res)


