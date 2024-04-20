from typing import List
from fastapi import HTTPException, status, Depends
from sqlmodel import Session, select
from sqlalchemy.exc import IntegrityError

from db import get_session
from schema import MemberCreateReq, MemberResp
from model import Member
from service.hash import Hash


def create_member(request: MemberCreateReq,
                  session: Session=Depends(get_session)) -> Member:

  new_user = Member(
    name = request.username,
    email = request.email,
    password_hash = Hash.bcrypt(request.password)
  )
  try:
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return MemberResp(email=new_user.email, username=new_user.name)
  except IntegrityError as e:
    session.rollback()
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
      detail=f'Duplicate entry for email: {request.email}')
  finally:
    session.close()


def get_member_by_name(name: str, 
                       session: Session=Depends(get_session)) -> Member:

  member = session.query(Member).filter(Member.name == name).first()
  if not member:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
      detail=f'User with username {name} not found')
  return member


def get_member_by_email(email: str,
                        session: Session=Depends(get_session)) -> Member:
  member = session.query(Member).filter(Member.email == email).first()
  if not member:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
      detail=f'User with email {email} not found')
  return member


def get_all_member(session: Session=Depends(get_session)) -> List[MemberResp]:
  
  members = session.exec(select(Member)).all()
  return members


