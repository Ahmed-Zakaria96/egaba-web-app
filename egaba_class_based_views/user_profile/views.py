from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

from accounts.models import UserProfile
from questions.models import Question
from notification.models import Notification
from django.views.generic.list import ListView

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
class UserProfileView(DetailView):
    model = UserProfile
    template_name='user_profile.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        questions = Question.objects.filter(
                        asked_by=self.get_object()
                        ).order_by('-date')
        context['questions'] = questions
        return context

class UserProfileEdit(LoginRequiredMixin, UpdateView):
    model = UserProfile
    fields = ['first_name', 'last_name', 'profession', 'profile_pic', 'bio']
    template_name='user_profile_edit.html'
    context_object_name = 'profile'

class NotificationView(LoginRequiredMixin, ListView):
    template_name = 'notification.html'
    context_object_name = 'notifications'

    def get_queryset(self):
        user = self.request.user.user_profile
        return Notification.objects.filter(user=user).order_by('-date')

class Connections(LoginRequiredMixin, ListView):
    template_name = 'connections.html'
    context_object_name = 'connections'

    def get_queryset(self):
        user = self.request.user.user_profile
        return user.following.all()
