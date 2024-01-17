from sqlmodel import Field, SQLModel
from sqlalchemy import Column
from typing import Optional, Any


class Member(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str
    password: str
 

class StockReport(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    product_id: str
    stock_id: str
    date: str
    close: float
    ko_base: float
    ki_base: float
    ko_diff: float
    ki_diff: float
    is_ko: int
    is_ki: int

class ProductInfo(SQLModel, table=True):
    id: Optional[str] = Field(default=None, primary_key=True)
    start_date: str
    start_trace_date: str
    end_date: str
    ko_limit: float
    ki_limit: float

class StockInfo(SQLModel, table=True):
    id: Optional[str] = Field(default=None, primary_key=True)

class ProductStock(SQLModel, table=True):
    product_id: Optional[str] = Field(default=None, primary_key=True)
    stock_id: Optional[str] = Field(default=None, primary_key=True)



