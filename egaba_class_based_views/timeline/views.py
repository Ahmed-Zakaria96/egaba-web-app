from django.shortcuts import render
from django.db.models import F, Count

from django.views.generic.list import ListView

from structure.models import University, Faculty, Department, Subject
from questions.models import Question
from accounts.models import UserProfile
from notification.models import Notification

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .mixin import SuggestionsMixin

# Create your views here.
class Timeline(SuggestionsMixin, ListView):
    model = University
    template_name = 'timeline.html'
    context_object_name = 'universities'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        faculties = Faculty.objects.all()
        departments = Department.objects.all()
        subjects = Subject.objects.all()

        # annotate new field for vote counts
        questions = Question.objects.all().order_by('-date').annotate(
        total_vote = Count(F('up_vote')) - Count(F('down_vote')))
        context['questions'] = questions

        # if user is logged in get his notification
        if self.request.user.is_authenticated:
            user_profile = UserProfile.objects.get(user=self.request.user)
            notifications = Notification.objects.filter(noti_for=user_profile, read=False).count()
            context['notif'] = notifications
            context['suggestions'] = self.get_suggestions()
        return context

class Following(LoginRequiredMixin, ListView):
    model = University
    template_name = 'timeline.html'
    context_object_name = 'universities'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_following = UserProfile.objects.get(user=self.request.user).following.all()
        questions = Question.objects.filter(
            asked_by__in=user_following).annotate(
            total_vote = Count(F('up_vote')) - Count(F('down_vote')))
        context['questions'] = questions

        # suggestions
        import random
        suggestion = UserProfile.objects.all().exclude(following=F('pk'))
        random_items = random.choice(suggestion)
        context['suggestions'] = random_items

        return context

class SubjectView(ListView):
    model = University
    template_name = 'subject.html'
    context_object_name = 'universities'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        uni = University.objects.filter(name__iexact=self.kwargs['university']).first()
        fac = Faculty.objects.filter(name__iexact=self.kwargs['faculty']).first()
        dep = Department.objects.filter(name__iexact=self.kwargs['department']).first()
        subj = Subject.objects.filter(name__iexact=self.kwargs['subject']).first()
        questions = Question.objects.filter(
                        university=uni,faculty=fac,department=dep, subject=subj
                        ).order_by('-date').annotate(
                        total_vote = Count(F('up_vote')) - Count(F('down_vote')))
        context['questions'] = questions
        context['university'] = uni
        context['faculty'] = fac
        context['department'] = dep
        context['subject'] = subj
        return context

class DepartmentView(ListView):
    model = University
    template_name = 'department.html'
    context_object_name = 'universities'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        uni = University.objects.filter(name__iexact=self.kwargs['university']).first()
        fac = Faculty.objects.filter(name__iexact=self.kwargs['faculty']).first()
        dep = Department.objects.filter(name__iexact=self.kwargs['department']).first()
        questions = Question.objects.filter(
            university=uni,faculty=fac, department=dep
            ).order_by('-date').annotate(
            total_vote = Count(F('up_vote')) - Count(F('down_vote')))
        context['questions'] = questions
        context['university'] = uni
        context['faculty'] = fac
        context['department'] = dep
        return context

class FacultyView(ListView):
    model = University
    template_name = 'faculty.html'
    context_object_name = 'universities'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        uni = University.objects.filter(name__iexact=self.kwargs['university']).first()
        fac = Faculty.objects.filter(name__iexact=self.kwargs['faculty']).first()
        questions = Question.objects.filter(university=uni,faculty=fac).order_by('-date').annotate(
        total_vote = Count(F('up_vote')) - Count(F('down_vote')))
        context['questions'] = questions
        context['university'] = uni
        context['faculty'] = fac
        return context

class UniversityView(ListView):
    model = University
    template_name = 'university.html'
    context_object_name = 'universities'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        uni = University.objects.filter(name__iexact=self.kwargs['university']).first()
        questions = Question.objects.filter(university=uni).order_by('-date').annotate(
        total_vote = Count(F('up_vote')) - Count(F('down_vote')))
        context['questions'] = questions
        context['university'] = uni
        return context
