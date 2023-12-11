from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.http import require_GET, require_POST

from django.db.models import Q
from django import forms

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator

from .forms import QuestionForm, AnswerForm

from .models import *

def search(request):
    search_q = request.GET['q']
    questions = Question.objects.filter(Q(question_body__icontains=search_q) | Q(question_title__icontains=search_q)).order_by('-date')

    paginator = Paginator(questions, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'search.html', {
        'page_obj': page_obj,
        'q': search_q
    })

def question_details(request, id):
    try:
        question = Question.objects.get(id=id)
        answer = AnswerForm()
        return render(request, 'question_details.html', {
            'question': question,
            'answer': answer
        })
    except Exception as e:
        return render(request, 'error.html', {
            'error': e
        })

def verify(user):
    return user.verified_user

@login_required(login_url='account:login')
@user_passes_test(verify, login_url='account:need_activate', redirect_field_name=None)
def ask(request):
    new_question = QuestionForm()
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.asked_by = request.user
            form.save()
            return HttpResponseRedirect(reverse('index:index'))
        else:
            return render(request, 'ask.html', {
                'question': new_question,
                'error': form.errors
            })

    return render(request, 'ask.html', {
        'question': new_question
    })

@login_required(login_url='account:login')
def edit_question(request, id):
    # check if question exist
    if request.method == "GET":
        try:
            question = Question.objects.get(id=id)
            form = QuestionForm(instance=question)
            return render(request, 'edit.html', {
                'question': form,
                'q': question
            })
        except:
            return render(request, 'error.html')
    # edit submit
    if request.method == "POST":
        try:
            question = Question.objects.get(id=id)
        except Exception as e:
            return render(request, 'error.html', {
                'error': e
            })

        if question.asked_by == request.user:
            edited_form = QuestionForm(request.POST, instance=question)
            if edited_form.is_valid():
                edited_form.save()
                return HttpResponseRedirect(reverse('index:index'))
            else:
                return render(request, 'ask.html', {
                    'question': form,
                    'error': edited_form.errors
                })
        else:
            return render(request, 'ask.html', {
                'question': form,
                'error': edited_form.errors
            })

@login_required(login_url='account:login')
def delete_question(request, id):
    try:
        question = Question.objects.get(id=id)
    except:
        return render(request, 'error.html', {
            'error': e
        })
    if request.user == question.asked_by:
        question.delete()
        return HttpResponseRedirect(reverse('index:index'))
    return HttpResponseRedirect(reverse('index:index'))

@login_required(login_url='aacount:login')
@user_passes_test(verify, login_url='account:need_activate', redirect_field_name=None)
@require_POST
def answer_question(request, id):
    answer_form = AnswerForm(request.POST)
    try:
        if answer_form.is_valid():
            answer_form = answer_form.save(commit=False)
            answer_form.answered_by = request.user
            answer_form.question = Question.objects.get(id=id)
            answer_form.save()
            return  HttpResponseRedirect(reverse('questions:question', args=[id]))
    except:
        return HttpResponseRedirect(reverse('questions:question', args=[id]))


# options ajax
# faculty filter
@require_GET
def faculty_options(request, id):
    try:
        faculties = Faculty.objects.filter(university__id=id)
        return JsonResponse([f.serialize() for f in faculties], safe=False)
    except:
        return JsonResponse({"error": "something went wrong, please reload the page"}, status=500)

# department filter
@require_GET
def department_options(request, id):
    try:
        departments = Department.objects.filter(faculty__id=id)
        return JsonResponse([d.serialize() for d in departments], safe=False)
    except:
        return JsonResponse({"error": "something went wrong, please reload the page"}, status=500)

# level filter
@require_GET
def level_options(request, id):
    try:
        levels = Level.objects.filter(department__id=id)
        return JsonResponse([l.serialize() for l in levels], safe=False)
    except:
        return JsonResponse({"error": "something went wrong, please reload the page"}, status=500)

# subject filter
@require_GET
def subject_options(request, id):
    try:
        subjects = Subject.objects.filter(level__id=id)
        return JsonResponse([s.serialize() for s in subjects], safe=False)
    except:
        return JsonResponse({"error": "something went wrong, please reload the page"}, status=500)
