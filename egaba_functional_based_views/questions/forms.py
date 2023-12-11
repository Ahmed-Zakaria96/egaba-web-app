from django.forms import ModelForm, Select, TextInput, Textarea, PasswordInput
from .models import Question, Answer


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        exclude = ('date', 'asked_by', 'answered_by')

        widgets = {
            'university': Select(attrs={'class': 'form-control'}),
            'faculty': Select(attrs={'class': 'form-control'}),
            'department': Select(attrs={'class': 'form-control'}),
            'level': Select(attrs={'class': 'form-control'}),
            'subject': Select(attrs={'class': 'form-control'}),
            'question_title': TextInput(attrs={'class': 'form-control'}),
            'question_body': Textarea(attrs={'class': 'form-control editor'})
        }

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['answer_body']

        widgets = {
            'answer_body': Textarea(attrs={'class': 'form-control editor'})
        }
