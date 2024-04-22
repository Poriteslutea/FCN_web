from pydantic import BaseModel

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