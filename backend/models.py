from sqlmodel import Field, SQLModel
from typing import Optional, Any


class Member(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str
    password: str
 





