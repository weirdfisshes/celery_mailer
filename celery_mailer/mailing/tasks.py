import django.template
from celery_mailer.celery_settings import app

from . import logs

# @app.task(bind=True, retry_backoff=True)
# def send_message(self, data):
#     logs.logger.info(data)

@app.task(bind=True, retry_backoff=True)
def send_message(self, client, message):
    template = django.template.Template(
        message.mail_template.html_template
    )
    data = {
        'name': client.name,
        'surname': client.surname,
        'date_of_birth': client.date_of_birth,
        'email': client.email,
        'group': client.group
    }
    context = django.template.Context(data)
    logs.logger.info(template.render(context))