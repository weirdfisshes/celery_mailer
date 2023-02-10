import django.template
from celery_mailer.celery_settings import app
import django.core.mail

from . import logs


@app.task(bind=True, retry_backoff=True)
def send_message(self, data, mail):
    try:
        template = django.template.Template(mail['template'])
        context = django.template.Context(data)
        django.core.mail.send_mail(
            mail['subject'],
            template.render(context),
            mail['mail_from'],
            [data['email']]
        )
        logs.logger.error('Sent mail')
    except Exception as error:
        logs.logger.error('Failed to send mail')
        raise self.retry(exc=error)
