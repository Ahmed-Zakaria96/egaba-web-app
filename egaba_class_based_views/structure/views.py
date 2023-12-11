from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views import View

from .models import University

from questions.models import Question
from django.contrib.auth.mixins import UserPassesTestMixin

class IndexTemplateView(View):
    http_method_name = ['get']

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(reverse('timeline:timeline'))
        else:
            return render(request, 'index.html')

class CoverageListView(TemplateView):
    context_object_name = 'universities'
    template_name = 'coverage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        universities = University.objects.all()
        context['universities'] = universities
        return context
