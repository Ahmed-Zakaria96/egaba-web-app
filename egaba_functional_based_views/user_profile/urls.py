from django.urls import path
from . import views

app_name = 'profile'

urlpatterns = [
    path('my_questions', views.my_questions, name="my_questions"),
    path('notifications', views.notification, name='notifications'),

    path('inbox_person_mails/<int:id>', views.inbox_person_mails, name="inbox_person_mails"),
    path('sent_person_mails/<int:id>', views.sent_person_mails, name="sent_person_mails"),
    path('archeive_person_mails/<int:id>', views.archeive_person_mails, name="archeive_person_mails"),


    path('mail/compose', views.compose, name='compose'),
    path('mail/delete/<int:id>', views.delete_mail, name='delete_mail'),
    path('mail/archeive/<int:id>', views.archeive, name='archeive_mail'),


    path('mail/<int:id>', views.mails_details, name='mails'),
    path('mail/<str:mail_box>', views.user_mail, name='user_mail'),

    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('<str:username>', views.user_profile, name='user_profile'),
]
