from django.db.models.signals import post_save
from django.dispatch import receiver

from registrations.models import User
from .models import Badge, Profile
from questions.models import Answer


# @receiver(post_save, sender=Profile)
# def user_badge(sender, instance, created, **kwargs):
#     if created:
#         badges = Badge.objects.all()
#         print(badges)
#     else:
#         print('nope')
