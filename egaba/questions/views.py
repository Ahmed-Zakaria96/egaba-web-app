from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import F, Count

from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Question, Answer
from accounts.models import UserProfile, Badge
from structure.models import University

from .forms import QuestionForm, AnswerForm
from questions.models import Question

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
class QuestionDetailView(DetailView):
    model = Question
    paginate_by = 10
    contex_object_name = "question"
    template_name = 'question.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        answers = self.get_object().question_answered.all().annotate(
            total_vote = Count(F('up_vote')) - Count(F('down_vote'))
        )
        context['answers'] = answers
        context['answerform'] = AnswerForm()
        return context

class QuestionCreateView(LoginRequiredMixin, CreateView):
    form_class = QuestionForm
    model = Question
    template_name = 'ask.html'

    def form_valid(self, form):
        form.instance.asked_by = UserProfile.objects.get(user=self.request.user)
        return super(QuestionCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        badges = Badge.objects.all()
        context['badges'] = badges
        return context

class QuestionEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Question
    form_class = QuestionForm
    template_name = 'edit.html'

    def test_func(self):
        user = UserProfile.objects.get(user=self.request.user)
        if self.get_object().asked_by == user:
            return True
        else:
            return False

class QuestionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Question
    contex_object_name = 'question'
    success_url = reverse_lazy('timeline:timeline')
    template_name = "question_confirm_delete.html"

    def test_func(self):
        user = UserProfile.objects.get(user=self.request.user)
        if self.get_object().asked_by == user:
            return True
        else:
            return False

class AnswerCreateView(LoginRequiredMixin, CreateView):
    model = Answer
    fields = ['body']
    template_name = 'answer.html'

    def form_valid(self, form):
        form.instance.answered_by = UserProfile.objects.get(user=self.request.user)
        form.instance.question = Question.objects.get(id=self.kwargs['pk'])
        return super(AnswerCreateView, self).form_valid(form)

class AnswerEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Answer
    form_class = AnswerForm
    context_object_name = 'answer_edit'
    template_name = 'edit_answer.html'

    def test_func(self):
        user = UserProfile.objects.get(user=self.request.user)
        if self.get_object().answered_by == user:
            return True
        else:
            return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        question = self.get_object().question
        context['question'] = question
        return context

class AnswerDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Answer
    contex_object_name = 'answer'
    success_url = reverse_lazy('timeline:timeline')
    template_name = 'answer_delete_confirm.html'

    def test_func(self):
        user = UserProfile.objects.get(user=self.request.user)
        if self.get_object().answered_by == user:
            return True
        else:
            return False
