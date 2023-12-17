import json
import logging

import channels.layers

from asgiref.sync import async_to_sync

from django.db.models.signals import post_save
from django.dispatch import receiver

from questions.models import Question, Answer
from notification.models import Notification

@receiver(post_save, sender=Answer)
def NotificationCreator(sender, instance, created, **kwargs):
    if created:
        user = instance.answered_by
        noti_for = instance.question.asked_by
        question = instance.question
        source = instance
        notification = Notification(user=user, noti_for=noti_for,
                            question=question, source=source)
        notification.save()


@receiver(post_save, sender=Notification)
def NotificationSender(sender, instance, created, **kwargs):
    if created:
        count = Notification.objects.filter(read=False).count()
        message = {
            'body': f'{instance.user} Answerd your question {instance.question.title}',
            'count' : count
        }
        channel_layer = channels.layers.get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f'notification-{instance.noti_for.id}',
            {
                'type': 'send_notification',
                'text': message
            }
        )
