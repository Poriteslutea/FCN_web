from typing import List, Annotated, Union
from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlmodel import Session


from db import get_session
from service.db_product import (
    create_product,
    remove_product
)
from service.oauth2 import (
    get_current_active_user, 
)
from model import Member
from schema import ( 
    ProductResp,
    ProductCreateReq,
    ApiSuccessResp
)


router = APIRouter(
    prefix='/product',
    tags=['Product']
)


@router.get("/all", response_model=List[Union[ProductResp, None]])
async def get_all_products(member: Member=Depends(get_current_active_user)):

    if len(member.products) == 0:
        print('目前沒有資料')
        return []

    product_list = []
    for product in member.products:
        p = ProductResp(
            code=product.code,
            start_date=product.start_date.strftime('%Y-%m-%d'),
            start_trace_date=product.start_trace_date.strftime('%Y-%m-%d'),
            end_date=product.end_date.strftime('%Y-%m-%d'),
            ko_limit=product.ko_limit,
            ki_limit=product.ki_limit
        )
        print(p)
        product_list.append(p)
    
    return product_list


@router.post("/create", response_model=ApiSuccessResp)
async def create_product_api(req: ProductCreateReq,
                         member: Member=Depends(get_current_active_user),
                         session: Session=Depends(get_session)):
    
        return create_product(member, req, session)
    

@router.delete("/{product_code}", response_model=ApiSuccessResp)
async def remove_product_api(product_code: str,
                         member: Member=Depends(get_current_active_user),
                         session: Session=Depends(get_session)):
    
        return remove_product(member, product_code, session)












