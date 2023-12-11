from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    # registration
    path('login', views.login_view, name="login"),
    path('register', views.register, name="register"),
    path('logout', views.logout_view, name="logout"),

    path('need_activate', views._need_activate, name='need_activate'),
    path('activate', views.send_activate, name='send_activate'),
    path('activate/<uidb64>/<token>', views.activate, name='activate')
]
