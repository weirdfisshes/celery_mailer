import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "celery_mailer.settings")

app = Celery("celery_mailer")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
