# import json
# import logging
#
# import channels.layers
# from asgiref.sync import async_to_sync
#
# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
# from .models import Question
#
#
# @receiver(post_save, sender=Question)
# def QuestionNotification(sender, instance, created, **kwargs):
#
#     message = {
#         'question_id': instance.id,
#     }
#
#     channel_layer = channels.layers.get_channel_layer()
#
#     async_to_sync(channel_layer.group_send)(
#         'notification',
#         {
#             'type': 'send_notification',
#             'text': message
#         }
#     )
