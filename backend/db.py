import os
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
from config import DB_URL

load_dotenv()

engine = create_engine(DB_URL)
connect = engine.connect()

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

