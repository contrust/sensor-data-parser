FROM python:3.10.6-slim-buster

WORKDIR /app

RUN apt-get update && \
    apt-get install -y make="4.3-4.1build1" --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

COPY pyproject.toml poetry.lock ./

RUN pip install --no-cache-dir poetry=="1.7.1" && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-root && \
    rm -rf poetry.lock

COPY Makefile Makefile
COPY sensor_data_parser ./sensor_data_parser
COPY ./tests ./tests