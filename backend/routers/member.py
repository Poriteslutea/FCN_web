from typing import List, Annotated
from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlmodel import Session

from db import get_session
from service.db_member import (
    get_all_member, 
    create_member
)
from service.oauth2 import (
    get_current_active_user, 
    create_access_token,
    authenticate_user
)
from model import Member
from schema import (
    MemberCreateReq, 
    MemberResp,
    Token
)


router = APIRouter(
    prefix='/member',
    tags=['Member']
)

ACCESS_TOKEN_EXPIRE_MINUTES = 30



@router.post("/register", response_model=MemberResp)
async def register(req: MemberCreateReq, 
                   session: Session = Depends(get_session)):
    return create_member(req, session)


@router.post('/login', response_model=Token)
async def login(request: Annotated[OAuth2PasswordRequestForm, Depends()], 
          session: Session = Depends(get_session)) -> Token:
    
    member = authenticate_user(username=request.username,
                               password=request.password,
                               session=session)
    if not member:
        raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"email": member.email}, expires_delta=access_token_expires
    )

    return Token(
        access_token=access_token,
        token_type='bearer',
        email=member.email,
        name=member.name
    )

@router.get("/me", response_model=MemberResp)
async def read_user_me(
    current_user: Annotated[Member, Depends(get_current_active_user)]
):
    return MemberResp(email=current_user.email, 
                    username=current_user.name)
  

@router.get('/all', response_model=List[MemberResp])
async def get_all_activate_member(session: Session = Depends(get_session)):
    members =  get_all_member(session)
    activate_members = [{"username": row.name, "email": row.email} for row in members if not row.disabled]
    return [MemberResp(**member) for member in activate_members]











