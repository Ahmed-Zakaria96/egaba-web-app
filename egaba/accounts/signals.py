from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User, UserProfile, Badge


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        try:
            b = Badge.objects.all().first()
            UserProfile.objects.create(
                user=instance, first_name=instance.first_name, last_name=instance.last_name, badge=b)
            print('Profile created')
        except Exception as e:
            print(e)
