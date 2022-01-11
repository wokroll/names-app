# start by pulling the python image
FROM python:3.10.1

RUN mkdir -p /app
WORKDIR /app
RUN pip install pipenv

COPY Pipfile Pipfile
COPY templates templates
COPY db db
COPY models models
COPY app.py app.py


RUN set -ex && pipenv install
CMD FLASK_APP=app.py pipenv run flask run -h 0.0.0.0 -p 5000