FROM python:3.8-alpine

#RUN apk add --no-cache python3-dev && pip install --upgrade pip
RUN pip install --upgrade pip

WORKDIR /api

COPY . /api

RUN set -e; apk add --no-cache --virtual .build-deps gcc libc-dev linux-headers
RUN	pip install --no-cache-dir -r requirements.txt
RUN apk del .build-deps

CMD ["uwsgi", "app.ini"]