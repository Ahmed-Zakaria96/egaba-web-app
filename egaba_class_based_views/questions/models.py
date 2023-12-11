from django.db import models

from accounts.models import UserProfile
from structure.models import University, Faculty, Department, Subject

from django.shortcuts import reverse
# Create your models here.
class Question(models.Model):
    asked_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="asked_by")
    answered_by = models.ManyToManyField(UserProfile, related_name='answered_by_list')
    title = models.CharField(max_length=150)
    body = models.CharField(max_length=20000)
    status = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    up_vote = models.ManyToManyField(UserProfile, related_name='question_up_votes')
    down_vote = models.ManyToManyField(UserProfile, related_name='questions_down_votes')

    def calc_vote(self):
        return self.up_vote.all().count() - self.down_vote.all().count()

    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name="question_university")
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name="question_faculty")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="question_department")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="question_subject")

    def __str__(self):
        return self.title

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'status': self.status,
            'date': self.date,
            'up_votes': self.up_vote.all().count(),
            'down_votes': self.down_vote.all().count(),

            'university': self.university.name,
            'university_id': self.university.id,
            'faculty': self.faculty.name,
            'faculty_id': self.faculty.id,
            'department': self.department.name,
            'department_id': self.department.id,
            'subject': self.subject.name,
            'subject.id': self.subject.id,
        }

    def get_absolute_url(self):
        return reverse('questions:question', kwargs={'pk': self.id})

class Answer(models.Model):
    answered_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="answered_by")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="question_answered")
    body = models.CharField(max_length=20000)
    date = models.DateTimeField(auto_now_add=True)
    up_vote = models.ManyToManyField(UserProfile, related_name='answer_up_votes')
    down_vote = models.ManyToManyField(UserProfile, related_name='answer_down_votes')

    def serialize(self):
        return {
            'id': self.id,
            'body': self.body,
            'date': self.date,
            'up_vote': self.up_vote.all().count(),
            'down_vote': self.down_vote.all().count()
        }

    def calc_vote(self):
        return self.up_vote.all().count() - self.down_vote.all().count()

    def __str__(self):
        return self.body

    def get_absolute_url(self):
        return reverse('questions:question', kwargs={'pk': self.question.id})
