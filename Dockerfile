FROM python:3.8

ENV PYTHONBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /code
RUN pip install python-dotenv
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
