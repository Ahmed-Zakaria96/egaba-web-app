from django.forms import ModelForm, Select, TextInput, Textarea

from questions.models import Question, Answer

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'body', 'university', 'faculty', 'department', 'subject']

        widgets = {
            'body': Textarea(attrs={'class': 'form-control'}),
        }

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['body']

        widgets = {
            'body': Textarea(attrs={'class': 'form-control'}),
        }
