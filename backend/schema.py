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