from django.urls import path
from .views import (
    SubjectView, DepartmentView, FacultyView, UniversityView,
    Timeline, Following
)

app_name = 'timeline'

urlpatterns = [
    path('', Timeline.as_view(), name='timeline'),
    path('following/', Following.as_view(), name='following'),

    path(
        '<str:university>/<str:faculty>/<str:department>/<str:subject>/',
            SubjectView.as_view(), name='subject'),
    path('<str:university>/<str:faculty>/<str:department>/',
            DepartmentView.as_view(), name='department'),
    path('<str:university>/<str:faculty>/', FacultyView.as_view(), name='faculty'),
    path('<str:university>/', UniversityView.as_view(), name='university')

]
