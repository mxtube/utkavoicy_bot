FROM python:3.12.5-alpine3.20

MAINTAINER Kirill Kuznetsov <kafomin@yandex.ru>

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN pip install --upgrade pip
COPY src/requirements.txt /temp/requirements.txt
RUN pip install -r /temp/requirements.txt

COPY src /opt/utkabot
WORKDIR /opt/utkabot
EXPOSE 80

RUN apk add postgresql-client build-base postgresql-dev

RUN adduser --disabled-password mxtube
RUN chown mxtube /opt/
USER mxtube
