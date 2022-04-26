ARG BASE_IMAGE

FROM ${BASE_IMAGE}

ARG PYPI_USER
ARG PYPI_PASSWORD
ARG PYPI_URL

WORKDIR src

COPY config .

COPY pyproject.toml poetry.lock ./
RUN poetry install -vv --no-dev

COPY src .

EXPOSE 8087

CMD gunicorn -c /src/gunicorn.py main:init

