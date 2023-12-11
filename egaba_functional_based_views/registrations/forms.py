from django.forms import ModelForm, Select, TextInput, Textarea, PasswordInput, EmailInput

from .models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email', 'password']
        # 'image': _('Image Link'),

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'id': 'first_name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'id': 'last_name'}),
            'email': EmailInput(attrs={'class': 'form-control', 'id': 'email'}),
            'username': TextInput(attrs={'class': 'form-control', 'id': 'username'}),
            'password': PasswordInput(attrs={'class': 'form-control', 'id': 'password'}),
        }
