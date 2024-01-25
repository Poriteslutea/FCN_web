from sqlmodel import Field, SQLModel, Relationship
from sqlalchemy import Column
from typing import Optional, Any, List


# Link Table Model
class ProductStock(SQLModel, table=True):
    product_id: Optional[str] = Field(default=None, primary_key=True, foreign_key="product.id")
    stock_id: Optional[str] = Field(default=None, primary_key=True, foreign_key="stock.id")

class MemberProduct(SQLModel, table=True):
    member_id: Optional[int] = Field(default=None, primary_key=True, foreign_key="member.id")
    product_id: Optional[str] = Field(default=None, primary_key=True, foreign_key="product.id")
    


# Table Model

class Member(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str
    password: str
    
    products: List["Product"] = Relationship(back_populates="members", link_model=MemberProduct)

class StockReport(SQLModel, table=True):
    __tablename__ = "stock_report"
    id: Optional[int] = Field(default=None, primary_key=True)
    product_id: str = Field(default=None, foreign_key="product.id")
    stock_id: str
    date: str
    close: float
    ko_base: float
    ki_base: float
    ko_diff: float
    ki_diff: float
    is_ko: int
    is_ki: int

    stock: Optional["Stock"] = Relationship(back_populates="stock_report")
    product: Optional["Product"] = Relationship(back_populates="stock_report")

class Product(SQLModel, table=True):
    id: Optional[str] = Field(default=None, primary_key=True)
    start_date: str
    start_trace_date: str
    end_date: str
    ko_limit: float
    ki_limit: float
    price_type: str

    stock_report: Optional["StockReport"] = Relationship(back_populates="product")
    stocks: List["Stock"] = Relationship(back_populates="products", link_model=ProductStock)
    members: List["Member"] = Relationship(back_populates="products", link_model=MemberProduct)

class Stock(SQLModel, table=True):
    id: Optional[str] = Field(default=None, primary_key=True)
    
    products: List["Product"] = Relationship(back_populates="stocks", link_model=ProductStock)
    stock_report: Optional["StockReport"] = Relationship(back_populates="stock_report")



