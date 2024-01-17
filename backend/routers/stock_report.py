from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from pydantic import BaseModel
from db import get_session
from backend.service import stock_report_service
from models import StockReport


router = APIRouter(
    prefix='/stock_report',
    tags=['StockReport']
)



@router.get('/latest')
def get_latest_report(session: Session = Depends(get_session)):
    query = session.exec(select(StockReport)).all()
    return query


