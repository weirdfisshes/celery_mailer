FROM python:2.7

RUN mkdir /app

COPY requirements.txt /app

RUN pip install -r /app/requirements.txt --no-cache-dir

COPY celery_mailer/ /app

WORKDIR /app

CMD ["python", "manage.py", "runserver", "0:8000"]