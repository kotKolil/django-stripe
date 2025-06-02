FROM python:3.13

RUN mkdir /app
WORKDIR /app

COPY r.txt  /app/
RUN pip install --no-cache-dir -r r.txt
COPY django_stripe /app/

RUN python manage.py makemigrations
RUN python manage.py collectstatic --noinput

EXPOSE 8000
EXPOSE 80

CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000
