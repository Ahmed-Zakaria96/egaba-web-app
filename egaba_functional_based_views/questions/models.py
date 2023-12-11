from django.db import models
from structure.models import *
from registrations.models import User

# questions and answers
class Question(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name="question_university")
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name="question_faculty")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="question_department")
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name="question_Level")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="question_subject")
    asked_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="asked_by")
    answered_by = models.ManyToManyField(User, related_name='answered_by_list')
    question_title = models.CharField(max_length=150)
    question_body = models.CharField(max_length=20000)
    question_status = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_title

class Answer(models.Model):
    answered_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="answered_by")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="question_answered")
    answer_body = models.CharField(max_length=20000)
    votes = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.answer_body

class Notification(models.Model):
    notification_for = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notification_user")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='notification_question', default=None, null=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='notification_answer')
    date = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.answer.answered_by.username} answered: {self.answer.answer_body}'
