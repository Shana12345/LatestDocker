FROM python:alpine3.11


MAINTAINER shana12345 <shana_charlery@msn.com>


RUN apk add --update


COPY . /Docker/Projecto/Service_2/


WORKDIR /Docker/Projecto/Service_2/


RUN set -e; \
        apk add --no-cache --virtual .build-deps \
            gcc \ 
            libc-dev \
            linux-headers \
            mariadb-dev \
            python3-dev \
            postgresql-dev \
        ;

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3" , "app.py"]