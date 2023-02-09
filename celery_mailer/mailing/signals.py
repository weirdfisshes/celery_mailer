from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Mailing, Client, ClientMail
from .tasks import send_message
from . import logs


@receiver(post_save, sender=Mailing, dispatch_uid="create_mailing")
def create_client_mail(sender, instance, created, **kwargs):
    if created:
        mailing = Mailing.objects.filter(id=instance.id).first()
        clients = Client.objects.filter(group=mailing.group).all()

        for client in clients:
            ClientMail.objects.create(
                client=client,
                mail_template=mailing.mail_template,
                mailing = mailing,
                status = 'not read'

            )
            message = ClientMail.objects.filter(
                id=instance.id,
                client=client.id
            ).first()

            send_message.apply_async((message),)
