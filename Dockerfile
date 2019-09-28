FROM python:3.7

ENV PYTHONUNBUFFERED 1

MAINTAINER Fabrice NIYOMWUNGERI

RUN mkdir /usr/src/app

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt
