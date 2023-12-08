from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse


# Create your models here.
class User(AbstractUser):
    verified_user = models.BooleanField(default=False)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profession = models.CharField(max_length=100)
    profile_pic = models.ImageField(default='1.png')
    bio = models.CharField(max_length=500)
    vote_points = models.IntegerField(default=0)
    following = models.ManyToManyField('self', related_name='following')

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
        else:
            self.badge = Badge.objects.filter(points__gte =  0).first()
        return self.badge

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def serialize(self):
        return {
            'name': self.first_name
        }

    def get_absolute_url(self):
        return reverse('profile:user_profile', kwargs={'pk': self.id})


class Badge(models.Model):
    points = models.IntegerField(default=0)
    title = models.CharField(default='test', max_length=50)
    name = models.CharField(max_length=50000)

    def __str__(self):
        return f"{self.title}"
