# 
FROM python:3.10-slim

RUN mkdir /fcnapp
WORKDIR /fcnapp/

COPY backend/ /fcnapp/backend/
COPY genenv.py local.ini poetry.lock pyproject.toml /fcnapp/

RUN pip3 install poetry==1.8.2
RUN poetry install

RUN VERSION=RELEASE python genenv.py

ENV PYTHONUNBUFFERED=0
ENV PYTHONPATH=/fcnapp/backend/


CMD ["poetry", "run", "uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]


