# pull official base image
FROM python:3.9.5-slim-buster

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR app

COPY * /app/

# install dependencies
RUN pip install --upgrade pip
RUN pip install --upgrade "setuptools<58"
RUN pip install -r requirements.txt

RUN ./bootstrap.sh
