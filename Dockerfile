FROM python:3.10.6-slim-buster

WORKDIR /app

RUN apt update && \
    apt install make && \
    rm -rf /var/lib/apt/lists/*

COPY pyproject.toml poetry.lock ./

RUN pip install --no-cache-dir poetry && \
	poetry config virtualenvs.create false && \
	poetry install --no-interaction --no-root && \
    rm -rf poetry.lock

COPY Makefile Makefile
COPY main.py main.py
COPY sensor_data_parser ./src
COPY ./tests ./tests