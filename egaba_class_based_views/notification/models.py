from django.db import models
from questions.models import Question, Answer
from accounts.models import UserProfile
# Create your models here.

class Notification(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='notification_from')
    noti_for = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='notification_for')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='notification_question')
    source = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='notification_source')
    read = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name} Answered your question {self.question.title}"
