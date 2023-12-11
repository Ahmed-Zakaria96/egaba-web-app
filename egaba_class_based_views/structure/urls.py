from django.urls import path
from .views import IndexTemplateView, CoverageListView

app_name = 'index'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('coverage/', CoverageListView.as_view(), name='coverage'),
]
