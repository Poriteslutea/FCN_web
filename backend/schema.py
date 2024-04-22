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
    date: str
    close: float
    ko_base: float
    ki_base: float
    ko_diff: float
    ki_diff: float
    is_ko: bool
    is_ki: bool