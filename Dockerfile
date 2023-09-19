FROM python:3.10 

ENV PYTHONBUFFERED = 1 
ENV DJANGO_SETTINGS_MODULE inventoriku.settings
WORKDIR /django

COPY requirements.txt . 

RUN pip install -r requirements.txt 

COPY . .

EXPOSE 8000

# CMD ["python", "manage.py", "runserver"] 

# FROM mysql:8 
# ENV MYSQL_ROOT_PASSWORD "" 
# ENV MYSQL_ALLOW_EMPTY_PASSWORD 1
# COPY ./inventoriku.sql /docker-entrypoint-init.db/inventoriku.sql 