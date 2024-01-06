from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from pydantic import BaseModel
import sys
from db import get_session
from models import Member


router = APIRouter(
    prefix='/member',
    tags=['Member']
)


@router.get('/all')
def get_all_member(session: Session = Depends(get_session)):
    query = session.exec(select(Member)).all()
    return query

class MemberCreate(BaseModel):
    email: str
    password: str


@router.post("/create/", response_model=Member)
async def create_member(member: MemberCreate, session: Session = Depends(get_session)):

    db_member = Member(email=member.email, password=member.password)
    session.add(db_member)
    session.commit()
    session.refresh(db_member)

    return db_member

# @router.delete('/{id}')
# def delete(id: int, db: Session = Depends(get_db)):
#     return db_clientinfo.delete_client(id, db)

# @router.post('')
# def create(request: ClientInfoBase, db: Session = Depends(get_db)):
#     return db_clientinfo.create_client(db, request)


