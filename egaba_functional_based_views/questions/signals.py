from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Question, Answer, Notification
from user_profile.models import Profile
from registrations.models import User

@receiver(post_save, sender=Answer)
def create_notification(sender, instance, created, **kwargs):
    if created:
        try:
            # create notification
            Notification.objects.create(notification_for=instance.question.asked_by, question=instance.question, answer=instance)
            print('Created Notification')

            # update vote
            user = Profile.objects.get(user=instance.answered_by)
            if instance.answered_by in instance.question.answered_by.all():
                print("already earned vote point")
            else:
                user.vote_points += 1
                user.save()
                print("successfully updated vote points")

                # update answered_by_list
                q = instance.question
                q.answered_by.add(instance.answered_by)
                q.save()
                print('added user to answer list')
        except Exception as e:
            print(e)
