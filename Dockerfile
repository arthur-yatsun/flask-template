FROM python:3.8-slim-buster


ENV SECRET_KEY secret
ENV DB_DSN postgresql+psycopg2://postgres:secret@localhost:5432/postgres

WORKDIR /
COPY . /

RUN pip3 install -r ./requirements.txt


CMD PYTHONPATH=./ python application/app.py