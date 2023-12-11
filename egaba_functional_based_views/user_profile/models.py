from django.db import models

from registrations.models import User
# Create your models here.
import time

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    display_name = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
    bio = models.CharField(max_length=500)
    vote_points = models.IntegerField(default=0)
    mentor = models.BooleanField(default=False)
    badge = models.ForeignKey('Badge', on_delete=models.PROTECT, related_name="user_badge", null=True, default=None)

    def get_badge(self):
        if self.vote_points >= 1000:
            self.badge = Badge.objects.filter(points__gte =  1000).first()
        elif self.vote_points >= 500:
            self.badge = Badge.objects.filter(points__gte =  500).first()
        elif self.vote_points >= 250:
            self.badge = Badge.objects.filter(points__gte =  250).first()
        elif self.vote_points >= 200:
            self.badge = Badge.objects.filter(points__gte =  200).first()
        elif self.vote_points >= 150:
            self.badge = Badge.objects.filter(points__gte =  150).first()
        elif self.vote_points >= 100:
            self.badge = Badge.objects.filter(points__gte =  100).first()
        elif self.vote_points >= 80:
            self.badge = Badge.objects.filter(points__gte =  80).first()
        elif self.vote_points >= 30:
            self.badge = Badge.objects.filter(points__gte =  30).first()
        else:
            self.badge = Badge.objects.filter(points__gte =  0).first()
        return self.badge


class Badge(models.Model):
    points = models.IntegerField(default=0)
    title = models.CharField(default='test', max_length=50)
    name = models.CharField(max_length=50000)

    def __str__(self):
        return f"{self.title}"

class Mail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_mails")
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mail_sender")
    recipients = models.ManyToManyField(User, name="mail_recipients")
    mail_subject = models.CharField(max_length=100)
    mail_body = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    archeive = models.BooleanField(default=False)

    def serialize(self):
        return {
            'id': self.id,
            'user': self.user.username,
            'sender': self.sender.username,
            'recipients': [u.username for u in self.mail_recipients.all()],
            'subject': self.mail_subject,
            'body': self.mail_body,
            'date': self.date.strftime("%b %#d %Y, %#I:%M %p"),
        }
