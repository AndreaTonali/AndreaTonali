ARG PYTHON_VERSION="3.8.5"
FROM python:${PYTHON_VERSION}-slim-buster

COPY requirements.txt /requirements.txt
WORKDIR /

RUN apt-get update && \
    apt-get install -y --reinstall build-essential && \
    apt-get install -y --no-install-recommends \
    && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . /

RUN mypy -p ConveyorBelt
RUN flake8 ./ConveyorBelt
