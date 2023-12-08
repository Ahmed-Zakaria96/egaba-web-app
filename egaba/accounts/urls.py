from django.urls import path, reverse
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect

from .views import *

app_name = "accounts"

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', UserLogIn.as_view(), name='login'),
    path('logout/', UserLogOut.as_view(), name='logout'),

    path('password_change/',
        auth_views.PasswordChangeView.as_view(template_name='passwordchange.html',
                                                success_url=reverse_lazy('accounts:password_change_done')),
        name='password_change'
        ),
    path('password_change_done/',
        auth_views.PasswordChangeDoneView.as_view(),
        name='password_change_done'),

    path('reset_password/',
        auth_views.PasswordResetView.as_view(template_name='password_reset_form.html',
                                                success_url=reverse_lazy('accounts:password_reset_done'),
                                                email_template_name='password_reset_email.html'),
        name='password_reset'
        ),

    path('reset_password_sent/',
        auth_views.PasswordResetDoneView.as_view(template_name="reset_password_sent.html"),
        name='password_reset_done'
        ),

    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='reset_new_password.html',
                                                success_url=reverse_lazy('accounts:password_reset_complete')),
        name='password_reset_confirm'
        ),

    path('reset_password_complete/',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'),
]
