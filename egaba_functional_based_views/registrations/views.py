from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse

from django.db import IntegrityError
from django import forms
from .models import *
from .forms import UserForm

from django.core.exceptions import ValidationError
from django.core.validators import validate_email

# registrations
def login_view(request):
    new_form = UserForm()
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index:index"))
        else:
            return render(request, "login.html", {
                "message": "Invalid username and/or password.",
                'form': new_form
            })
    else:
        return render(request, 'login.html',{
            'form': new_form
        })

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index:index"))

from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
import base64

from django.core.mail import EmailMessage
from django.conf import settings

from .tokens import default_token_generator
from datetime import date

def register(request):
    new_form = UserForm()
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        try:
            email_check = validate_email(email)
            # Attempt to create new user if email is valid
            try:
                user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,
                                                email=email, password=password)
                user.save()
            except IntegrityError:
                return render(request, "register.html", {
                    "message": "Username already taken.",
                    'form': new_form
                })

            def _num_days(dt):
                return (dt - date(2001, 1, 1)).days

            mail_body = render_to_string('account_activation.html', {
                'user': user,
                'protocol': 'http',
                'domain': request.get_host(),
                'uidb64': urlsafe_base64_encode(force_bytes(user.id)),
                'token': default_token_generator._make_token_with_timestamp(user, _num_days(date.today())),
            })
            mail = EmailMessage(
                'Egaba account activation',
                mail_body,
                settings.EMAIL_HOST_USER,
                [user.email],
            )

            mail.fail_silently = False
            mail.send()
            login(request, user)
            return HttpResponseRedirect(reverse("index:index"))

        except Exception as e:
            return render(request, "register.html", {
                'form': new_form,
                'error': e
            })
    else:
        return render(request, "register.html", {
            'form': new_form
        })

from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='account:login')
def _need_activate(request):
    if request.user.verified_user:
        messages.success(request, "Your account is already activated.")
        return HttpResponseRedirect(reverse('index:index'))
    return render(request, 'activate.html')

@login_required(login_url='account:login')
def send_activate(request):
    def _num_days(dt):
        return (dt - date(2001, 1, 1)).days

    mail_body = render_to_string('account_activation.html', {
        'user': request.user,
        'protocol': 'http',
        'domain': request.get_host(),
        'uidb64': urlsafe_base64_encode(force_bytes(request.user.id)),
        'token': default_token_generator._make_token_with_timestamp(request.user, _num_days(date.today())),
    })
    mail = EmailMessage(
        'Egaba account activation',
        mail_body,
        settings.EMAIL_HOST_USER,
        [request.user.email],
    )
    mail.fail_silently = False
    mail.send()
    messages.success(request, "Activation link was sent successfully.")
    return HttpResponseRedirect(reverse('index:index'))

def activate(request, uidb64, token):
    try:
        id = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(id=id)
    except:
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        if user.verified_user == True:
            return render(request, 'success.html', {
                'message': 'Your account is already activated.'
            })
        user.verified_user = True
        user.save()
        return render(request, 'success.html', {
            'message': 'Account successfully activated'
        })
    else:
        return render(request, 'error.html', {
            'error': 'Invalid activation link'
        })
