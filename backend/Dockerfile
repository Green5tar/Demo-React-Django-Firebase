FROM python:3.11-bullseye
ENV PYTHONUNBUFFERED=1
RUN apt-get update && apt-get -y install libpq-dev gcc && pip install psycopg2
# RUN mkdir /code/requirements

WORKDIR /code

ENV POETRY_HOME=/opt/poetry
ENV PATH="$POETRY_HOME/bin:$PATH"
RUN curl -sSL https://install.python-poetry.org | python3 -

COPY ./pyproject.toml ./
COPY ./poetry.lock ./

RUN poetry config virtualenvs.create false

RUN poetry install --no-interaction
COPY . /code/

CMD python manage.py runserver 0.0.0.0:8000

