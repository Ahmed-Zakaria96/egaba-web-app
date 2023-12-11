from django.shortcuts import render
from registrations.models import User
from .models import Profile, Mail
from questions.models import Question, Notification
from django.db.models import Q

from django.core.paginator import Paginator

from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse

from .forms import MailForm, ProfileForm

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST

# Create your views here.

# profile view
def user_profile(request, username):
    # try to get profile with username
    try:
        user = User.objects.get(username__iexact=username)
        profile = Profile.objects.get(user=user)
        return render(request, 'profile.html', {
            'profile': profile
        })
    # if not exist display error page
    except Exception as e:
        return render(request, 'error.html', {
            'error': e
        })

# edit profile view
@login_required(login_url="account:login")
def edit_profile(request):
    user_profile = Profile.objects.get(user=request.user)
    profile = ProfileForm(instance=user_profile)
    if request.method == "POST":
        # make sure user requested is the profile owner
        if user_profile.user == request.user:
            edited_profile = ProfileForm(request.POST, instance=user_profile)
            if edited_profile.is_valid():
                edited_profile.save()
                return HttpResponseRedirect(reverse('profile:user_profile', args=[user_profile.user.username]))
            else:
                return render(request, 'edit_profile.html', {
                    'profile_form': profile,
                    'error': edited_profile.errors
                })
        # if not profile owner
        else:
            return render(request, 'edit_profile.html', {
                'profile_form': profile,
                'error': edited_profile.errors
            })

    # if request method is get
    return render(request, 'edit_profile.html', {
        'profile_form': profile
    })

from django.contrib import messages
# create new email
@login_required(login_url="account:login")
def compose(request):
    if request.method == "POST":
        mail = MailForm(request.POST)
        # get recipients list from form
        recipients = [r.strip() for r in request.POST['mail_recipients'].split(',')]
        # check if list is empty
        if recipients == [""]:
            return render(request, 'compose.html', {
                "error": "At least one recipient required.",
                "mail": mail
            })
        receivers = []
        invalid = []
        # try to get user for each receiptients user entered (valid user)
        for r in recipients:
            try:
                user = User.objects.get(username__iexact=r)
                receivers.append(user)
            except:
                invalid.append(r)

        if not receivers:
            mail = MailForm()
            return render(request, 'compose.html', {
                'mail': mail,
                'error': invalid
            })

        subject = request.POST['mail_subject']
        body = request.POST['mail_body']
        users = set()
        users.add(request.user)
        users.update(receivers)
        # todo should be many to many create email obj for each user
        for u in users:
            email = Mail(
                user=u,
                sender=request.user,
                mail_subject=subject,
                mail_body=body)
            email.save()
            for r in receivers:
                email.mail_recipients.add(r)
                email.save()

        messages.error(request, invalid)
        return HttpResponseRedirect(reverse('profile:user_mail', args=['sent']))

    mail = MailForm()
    return render(request, 'compose.html', {
        'mail': mail
    })

@login_required(login_url="account:login")
def inbox_person_mails(request, id):
    mail_sender = User.objects.get(id=id)
    mails = Mail.objects.filter(user=request.user, mail_recipients=request.user).order_by('-date')
    ready_mails = [m.serialize() for m in mails]
    return JsonResponse(ready_mails, safe=False)

@login_required(login_url="account:login")
def sent_person_mails(request, id):
    mail_sender = User.objects.get(id=id)
    mails = Mail.objects.filter(user=request.user, sender=request.user, mail_recipients=mail_sender).order_by('-date')
    ready_mails = [m.serialize() for m in mails]
    return JsonResponse(ready_mails, safe=False)

@login_required(login_url="account:login")
def archeive_person_mails(request, id):
    mail_sender = User.objects.get(id=id)
    mails = Mail.objects.filter(Q(sender=request.user) | Q(mail_recipients=request.user), user=request.user, archeive=True).order_by('-date')
    ready_mails = [m.serialize() for m in mails]
    return JsonResponse(ready_mails, safe=False)

@login_required(login_url="account:login")
def archeive(request, id):
    mail = Mail.objects.get(id=id)
    if mail.archeive == True:
        mail.archeive = False
        mail.save()
    else:
        mail.archeive = True
        mail.save()
    return HttpResponseRedirect(reverse('profile:user_mail', args=['archeive']))

@login_required(login_url="account:login")
def delete_mail(request, id):
    mail = Mail.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('profile:user_mail', args=['inbox']))

@login_required(login_url="account:login")
def user_mail(request, mail_box='inbox'):
    if mail_box == "inbox":
        mails = Mail.objects.filter(user=request.user, mail_recipients=request.user, archeive=False).order_by('-date')
    elif mail_box == "sent":
        mails = Mail.objects.filter(user=request.user, sender=request.user, archeive=False).order_by('-date')
    elif mail_box == "archeive":
        mails = Mail.objects.filter(Q(sender=request.user) | Q(mail_recipients=request.user), user=request.user, archeive=True).order_by('-date')
    return render(request, 'mail_box2.html', {
        'mails': mails,
        'mailbox': mail_box
    })

@login_required(login_url="account:login")
def mails_details(request, id):
    mail = Mail.objects.get(id=id)
    return render(request, 'mail.html', {
        'mail': mail
    })

@login_required(login_url="account:login")
def notification(request):
    notifications = Notification.objects.filter(notification_for=request.user).order_by('-date')

    paginator = Paginator(notifications, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'notification.html', {
        'page_obj': page_obj
    })

@login_required(login_url="account:login")
def my_questions(request):
    questions = Question.objects.filter(asked_by=request.user).order_by('-date')

    paginator = Paginator(questions, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'my_questions.html', {
        'page_obj': page_obj
    })


# activation


def user_activate(request, uidb64, token):
    pass
