from django.urls import path
from . import views

app_name = 'index'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:u>/<str:f>/<str:d>/<str:l>/<str:s>', views.groups, name='group'),
    path('about', views.about, name='about')
]
