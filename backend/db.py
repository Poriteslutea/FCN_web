from sqlmodel import SQLModel, create_engine, Session
import models
from dotenv import load_dotenv
import os
load_dotenv()

POSTGRES_URI = os.getenv('POSTGRES_URI')
engine = create_engine(POSTGRES_URI, echo=True)
connect = engine.connect()


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

 
def get_session():
    with Session(engine) as session:
        yield session

