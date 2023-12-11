from django.forms import ModelForm, Select, TextInput, Textarea, PasswordInput, EmailInput

from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext, gettext_lazy as _
from django import forms
from .models import User

class UserRegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email', 'password']

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'id': 'first_name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'id': 'last_name'}),
            'email': EmailInput(attrs={'class': 'form-control', 'id': 'email'}),
            'username': TextInput(attrs={'class': 'form-control', 'id': 'username'}),
            'password': PasswordInput(attrs={'class': 'form-control', 'id': 'password'}),
        }

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
                                attrs={'class': 'form-control',
                                        'placeholder': '',
                                        'id': 'username'
                                        }
                                    )
                                )
    password = forms.CharField(widget=forms.PasswordInput(
                                attrs={'class': 'form-control',
                                        'placeholder': '',
                                        'id': 'password'
                                        }
                                    )
                                )

    error_messages = {
        'invalid_login': _(
            "Invalid username and/or password."
        ),
        'inactive': _("This account is inactive."),
    }


from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
