# 
FROM python:3.10-slim

WORKDIR /code
COPY . /code
COPY ../genenv.py ../local.ini ../poetry.lock ../pyproject.toml /code/
COPY ../local.ini /code/
COPY ../poetry.lock /code/
COPY ../pyproject.toml /code/

RUN pip3 install poetry==1.8.2
RUN poetry install

RUN VERSION=RELEASE python3 genenv.py

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


