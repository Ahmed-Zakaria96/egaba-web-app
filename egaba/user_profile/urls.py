from django.urls import path
from .views import UserProfileView, UserProfileEdit, NotificationView, Connections

app_name = 'profile'

urlpatterns = [
    path('notification/', NotificationView.as_view(), name='notification'),
    path('connections/', Connections.as_view(), name='connections'),
    path('<int:pk>/', UserProfileView.as_view(), name='user_profile'),
    path('edit/<int:pk>/', UserProfileEdit.as_view(), name='user_profile_edit'),
]
