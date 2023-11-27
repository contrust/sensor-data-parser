FROM python:3.11.1-slim-buster

WORKDIR /app

RUN apt update && \
    apt install --no-install-recommends -y make && \
    rm -rf /var/lib/apt/lists/*

COPY pyproject.toml poetry.lock ./

RUN pip install --no-cache-dir poetry=="1.7.1" && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-root && \
    rm -rf poetry.lock

COPY Makefile Makefile
COPY sensor_data_parser ./sensor_data_parser
COPY ./tests ./tests