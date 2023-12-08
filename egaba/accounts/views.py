from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from .forms import UserRegisterForm, UserLoginForm, CustomUserCreationForm

from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('accounts:login')

class UserLogIn(LoginView):
    template_name = 'login.html'
    authentication_form = UserLoginForm

    def get_success_url(self):
        url = self.get_redirect_url()
        return url or reverse('index:index')

class UserLogOut(LogoutView):
    template_name = 'logout.html'
