FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./

ARG DB_NAME
ARG DB_USER
ARG DB_PASSWD
ARG DB_HOST

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:80