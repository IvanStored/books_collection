FROM python:3.11.4-slim-bullseye
LABEL maintainer="jus1stored@gmai.com"

WORKDIR /project

ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv
ENV POETRY_CACHE_DIR=/opt/.cache

RUN python3 -m venv $POETRY_VENV && $POETRY_VENV/bin/pip install -U pip setuptools && $POETRY_VENV/bin/pip install poetry

ENV PATH="${PATH}:${POETRY_VENV}/bin"

COPY poetry.lock pyproject.toml ./
RUN poetry install --no-root

COPY . /project
