FROM python:3.11.1
LABEL authors="Ivan"

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBEFFERED 1

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /usr/src/app/