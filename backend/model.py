from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel


# Link Table Model
class ProductStock(SQLModel, table=True):
    __tablename__ = "product_stock"
    product_id: Optional[int] = Field(default=None, primary_key=True, foreign_key="product.id")
    stock_id: Optional[int] = Field(default=None, primary_key=True, foreign_key="stock.id")

class MemberProduct(SQLModel, table=True):
    __tablename__ = "member_product"
    member_id: Optional[int] = Field(default=None, primary_key=True, foreign_key="member.id")
    product_id: Optional[int] = Field(default=None, primary_key=True, foreign_key="product.id")
    


# Table Model
class Member(SQLModel, table=True):
    __tablename__ = "member"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str = Field(unique=True, index=True)
    password_hash: str
    disabled: Optional[bool] = Field(default=False)
    
    products: List["Product"] = Relationship(back_populates="members", link_model=MemberProduct)

class DailyReport(SQLModel, table=True):
    __tablename__ = "daily_report"
    id: Optional[int] = Field(default=None, primary_key=True)
    product_id_fk: str = Field(default=None, foreign_key="product.id")
    stock_id_fk: str = Field(default=None, foreign_key="stock.id")
    date: str
    close: float
    ko_base: float
    ki_base: float
    ko_diff: float
    ki_diff: float
    is_ko: int
    is_ki: int

    stock: Optional["Stock"] = Relationship(back_populates="daily_report")
    product: Optional["Product"] = Relationship(back_populates="daily_report")

class Product(SQLModel, table=True):
    __tablename__ = "product"
    id: Optional[int] = Field(default=None, primary_key=True)
    code: str
    start_date: str
    start_trace_date: str
    end_date: str
    ko_limit: float
    ki_limit: float
    price_type: str

    daily_report: Optional["DailyReport"] = Relationship(back_populates="product")
    stocks: List["Stock"] = Relationship(back_populates="products", link_model=ProductStock)
    members: List["Member"] = Relationship(back_populates="products", link_model=MemberProduct)

class Stock(SQLModel, table=True):
    __tablename__ = "stock"
    id: Optional[int] = Field(default=None, primary_key=True)
    code: str
    
    products: List["Product"] = Relationship(back_populates="stocks", link_model=ProductStock)
    daily_report: Optional["DailyReport"] = Relationship(back_populates="stock")



