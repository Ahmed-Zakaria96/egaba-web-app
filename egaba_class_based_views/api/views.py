from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
import json
from django.contrib.auth.mixins import LoginRequiredMixin

from accounts.models import UserProfile
from questions.models import Question, Answer
from notification.models import Notification

class QuestionUpVote(LoginRequiredMixin, View):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        user_profile = UserProfile.objects.get(user=request.user)
        question = Question.objects.get(id=self.kwargs['q_id'])
        message = ""
        # check if user down voted
        if user_profile in question.down_vote.all():
            question.down_vote.remove(user_profile)
        if user_profile in question.up_vote.all():
            question.up_vote.remove(user_profile)
            message = "removed_up_vote"
        else:
            question.up_vote.add(user_profile)
            message = "added_up_voted"
        question.save()
        return JsonResponse({'message': message, 'votes': question.calc_vote()})

class QuestionDownVote(LoginRequiredMixin, View):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        user_profile = UserProfile.objects.get(user=request.user)
        question = Question.objects.get(id=self.kwargs['q_id'])
        message = ""
        # check if user down voted
        if user_profile in question.up_vote.all():
            question.up_vote.remove(user_profile)
        if user_profile in question.down_vote.all():
            question.down_vote.remove(user_profile)
            message = "removed_down_vote"
        else:
            question.down_vote.add(user_profile)
            message = "added_down_voted"
        question.save()
        return JsonResponse({'message': message, 'votes': question.calc_vote()})

class AnswerUpVote(LoginRequiredMixin, View):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        user_profile = UserProfile.objects.get(user=request.user)
        answer = Answer.objects.get(id=self.kwargs['q_id'])
        message = ""
        # check if user down voted
        if user_profile in answer.down_vote.all():
            answer.down_vote.remove(user_profile)
        if user_profile in answer.up_vote.all():
            answer.up_vote.remove(user_profile)
            message = "removed_up_vote"
        else:
            answer.up_vote.add(user_profile)
            message = "added_up_voted"
        answer.save()
        return JsonResponse({'message': message, 'votes': answer.calc_vote()})

class AnswerDownVote(LoginRequiredMixin, View):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        user_profile = UserProfile.objects.get(user=request.user)
        answer = Answer.objects.get(id=self.kwargs['q_id'])
        message = ""
        # check if user down voted
        if user_profile in answer.up_vote.all():
            answer.up_vote.remove(user_profile)
        if user_profile in answer.down_vote.all():
            answer.down_vote.remove(user_profile)
            message = "removed_down_vote"
        else:
            answer.down_vote.add(user_profile)
            message = "added_down_voted"
        answer.save()
        return JsonResponse({'message': message, 'votes': answer.calc_vote()})

class NotificationRead(LoginRequiredMixin, View):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        user_profile = UserProfile.objects.get(user=request.user)
        notification = Notification.objects.get(id=self.kwargs['id'], user=user_profile)
        message = ""
        if notification.read:
            notification.read = False
            message = "marked as un-read"
        else:
            notification.read = True
            message = "marked as read"
        notification.save()
        return JsonResponse({'message': message})

class Follow(LoginRequiredMixin, View):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        user = UserProfile.objects.get(user=request.user)
        data = json.loads(request.body)
        user_to_follow = UserProfile.objects.get(id=data['user_to_follow'])
        message = ""
        if user_to_follow in user.following.all():
            user.following.remove(user_to_follow)
            message = "Un-followed"
        else:
            user.following.add(user_to_follow)
            message = "Followed"
        user.save()
        return JsonResponse({'message': message})

from django.views.generic.base import TemplateView
# Create your views here.
class JSONResponseMixin:
    """
    A mixin that can be used to render a JSON response.
    """
    def render_to_json_response(self, context, **response_kwargs):
        return JsonResponse(
            self.get_data(context),
            **response_kwargs,
            safe=False
        )

    def get_data(self, context):
        return [c.serialize() for c in context[self.context_object_name]]

class SubjectOptions(JSONResponseMixin, View):
    http_method_names = ['get', 'post']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subjects = Subject.objects.filter(department__id=self.kwargs['dep_id'])
        context['subjects'] = subjects
        return context

    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, **response_kwargs)
