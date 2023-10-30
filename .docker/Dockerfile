FROM python:3.12.0-alpine3.18

# ENV PYTHONBUFFERED = 1 
ENV DJANGO_SETTINGS_MODULE inventoriku.settings
WORKDIR /django

# RUN apk add python3-dev default-libmysqlclient-dev build-essential pkg-config

RUN apk update \
    && apk --no-cache --update add python3 python3-dev mariadb-dev build-base

COPY requirements.txt . 

RUN pip3 install -r requirements.txt 

COPY . .

RUN python manage.py makemigrations inventori_crud

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"] 

# FROM mysql:8 
# ENV MYSQL_ROOT_PASSWORD "" 
# ENV MYSQL_ALLOW_EMPTY_PASSWORD 1
# COPY ./inventoriku.sql /docker-entrypoint-init.db/inventoriku.sql 