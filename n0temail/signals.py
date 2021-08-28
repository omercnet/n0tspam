import logging

from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from .models import Email


@receiver(post_save, sender=Email)
def email_created(instance: Email, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            instance.to_email.replace("@", "._."), {"email": instance.pk}
        )
