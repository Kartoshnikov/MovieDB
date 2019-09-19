FROM python:3.7.4-slim
WORKDIR /app
COPY ./docker/python/files /
RUN apt-get update && apt-get install -y libpq-dev build-essential postgresql-client && pip3 install -r /reqirenments.txt
ENV POSTGRES_PASSWORD='1111'
EXPOSE 80
