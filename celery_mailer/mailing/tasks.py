import django.template
from celery_mailer.celery_settings import app

from . import logs

@app.task(bind=True, retry_backoff=True)
def send_message(self, data, html_template):
    template = django.template.Template(html_template)
    context = django.template.Context(data)
    logs.logger.info(template.render(context))
