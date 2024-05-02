from pydantic import BaseModel
from typing import List

# Member 
class MemberCreateReq(BaseModel):
    email: str
    username: str
    password: str

class MemberResp(BaseModel):
    email: str
    username: str

class Token(BaseModel):
    access_token: str
    token_type: str
    email: str
    name: str 

# Report
class StockReportResp(BaseModel):
    stock: str
    date: str
    close: float
    ko_base: float
    ki_base: float
    ko_diff: float | None
    ki_diff: float | None
    is_ko: bool
    is_ki: bool

# Product
    
class ProductCreateReq(BaseModel):
    code: str
    start_date: str
    start_trace_date: str
    end_date: str
    ko_limit: float
    ki_limit: float
    stocks: List[str]


class ProductResp(BaseModel):
    code: str
    start_date: str
    start_trace_date: str
    end_date: str
    ko_limit: float
    ki_limit: float


class ApiSuccessResp(BaseModel):
    result: str