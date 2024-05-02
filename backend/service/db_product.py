from typing import List, Union
from fastapi import HTTPException, status, Depends
from sqlmodel import Session, select


from db import get_session
from schema import ProductCreateReq, ProductResp, ApiSuccessResp
from model import Member, Product, Stock


def create_product(member: Member, 
                   req: ProductCreateReq,
                   session: Session) -> ApiSuccessResp:
  
    stock_code_list = [i.upper() for i in req.stocks]
    stocks = []
    for st_code in stock_code_list:
        st = session.query(Stock).filter(Stock.code == st_code).first()
        if not st:
            st = Stock(code=st_code)
            try:
                session.add(st)
                session.commit()
                session.refresh(st)
            except Exception as e:
                session.rollback()
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                    detail=f'Failed to insert stock data: {e}')
            finally:
                session.close()
                
        stocks.append(st)
    
    pd = session.query(Product).filter(Product.code == req.code).first()
    if pd:
        return ApiSuccessResp(result=f"Product:{req.code} has already existed in database")
    
    new_product = Product(
       code=req.code,
       start_date=req.start_date,
       start_trace_date=req.start_trace_date,
       end_date=req.end_date,
       ko_limit=req.ko_limit,
       ki_limit=req.ki_limit,
       price_type='Close',
       stocks=stocks,
       members=[member]
    )

    try:
        session.add(new_product)
        session.commit()
        session.refresh(new_product)
        print('insert data successfully')
        return ApiSuccessResp(result=f"Insert product ({req.code}) successfully")
        
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Failed to insert product data: {e}')
    finally:
        session.close()
       

    
def remove_product(member: Member, 
                   product_code: str,
                   session: Session) -> Union[ApiSuccessResp, None]:
    
    product = session.exec(select(Product).where(Product.code == product_code)).first()
    if not product:
        return 
    try:
        product.members.remove(member)
        session.add(member)
        session.commit()
        return ApiSuccessResp(result=f"Remove product: {product.code} from member:{member.email} successfully")
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Failed to delete product data: {e}')
    finally:
        session.close()






