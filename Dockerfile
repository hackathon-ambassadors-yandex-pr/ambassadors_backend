FROM python:3.11-slim as base
RUN apt-get update
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir
COPY ./backend/ .
COPY ./db_data/data.json .
COPY ./infra/scripts/wait-for-it.sh .
RUN chmod +x wait-for-it.sh
RUN python manage.py collectstatic --no-input

FROM base as prod
COPY ./infra/scripts/run_app.prod.sh .
RUN chmod +x run_app.prod.sh

FROM base as dev
COPY infra/scripts/run_app.dev.sh .
RUN chmod +x run_app.dev.sh
COPY ./db_data/test_media/ ./media/
COPY ./db_data/test_data.json .
