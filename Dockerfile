FROM python:3.10.6-slim-buster

WORKDIR /app

RUN apt update && \
    apt install make && \
    rm -rf /var/lib/apt/lists/*

COPY pyproject.toml poetry.lock Makefile ./

RUN make install && \
    rm -rf poetry.lock

COPY main.py main.py
COPY ./src ./src
COPY ./tests ./tests