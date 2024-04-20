from typing import Optional, Annotated
from datetime import datetime, timedelta

from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from fastapi import HTTPException, Depends, status
from sqlmodel import Session


from db import get_session
from config import SECRET_KEY
from service.db_member import get_member_by_email
from service.hash import Hash
from model import Member



# Authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/member/login")
ALGORITHM = 'HS256'

def authenticate_user(username=str, password=str, session = Depends(get_session)):
  member = get_member_by_email(email=username, 
                              session=session)
  if not member:
    return False
  if not Hash.verify(member.password_hash, password):
    print("Incorrect Password")
    return False
  return member

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
  to_encode = data.copy()
  if expires_delta:
    expire = datetime.utcnow() + expires_delta
  else:
    expire = datetime.utcnow() + timedelta(minutes=15)
  to_encode.update({"exp": expire})
  encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
  return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme), 
                           session: Session = Depends(get_session)):
  
  credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
  )
  try:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    username: str = payload.get("email")
    if username is None:
      raise credentials_exception
  except Exception:
    raise credentials_exception
  
  return get_member_by_email(email=username, session=session)


async def get_current_active_user(
    current_user: Annotated[Member, Depends(get_current_user)],
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

