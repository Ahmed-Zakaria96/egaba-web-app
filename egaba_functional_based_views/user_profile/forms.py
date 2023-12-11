from django.forms import ModelForm, Select, TextInput, Textarea, PasswordInput
from .models import Mail, Profile

class MailForm(ModelForm):
    class Meta:
        model = Mail
        fields = ['mail_recipients', 'mail_subject', 'mail_body']

        widgets = {
            'mail_recipients': TextInput(attrs={'class': 'form-control', 'id': 'first_name'}),
            'mail_subject': TextInput(attrs={'class': 'form-control', 'id': 'first_name'}),
            'mail_body': TextInput(attrs={'class': 'form-control editor', 'id': 'first_name'})
        }

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['profession', 'bio', 'display_name']

        widgets = {
            'display_name': TextInput(attrs={'class': 'form-control'}),
            'profession': TextInput(attrs={'class': 'form-control'}),
            'bio': TextInput(attrs={'class': 'form-control'})
        }
