from django.contrib import admin
from .models import Profile, Mail, Badge
# Register your models here.
@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    list_display = ['title', 'points']

@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    list_display = ['user', 'sender', 'mail_subject']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'display_name', 'vote_points']
