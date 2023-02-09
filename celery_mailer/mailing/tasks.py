from celery_mailer.celery_settings import app
from . import logs

@app.task(bind=True, retry_backoff=True)
def send_message(self, data):
    logs.logger.info(data)