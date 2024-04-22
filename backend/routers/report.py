from typing import List, Annotated
from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlmodel import Session

from db import get_session
from service.db_report import (
    get_latest_report
)

from model import DailyReport, Product
from schema import (
    StockReportResp,

)

router = APIRouter(
    prefix='/report',
    tags=['Report']
)





@router.get("/latest/{product_code}", response_model=List[StockReportResp])
async def get_latest_report_api(
    product_code: str,
    session: Session = Depends(get_session)
):
    return get_latest_report(product_code, session)
  













