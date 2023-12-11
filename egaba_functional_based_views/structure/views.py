from django.shortcuts import render
from questions.models import Question
from .models import *

from django.core.paginator import Paginator

from django.http import HttpResponse

# Create your views here.
def index(request):
    universities = University.objects.all()
    questions = Question.objects.all()

    paginator = Paginator(questions, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', {
        'page_obj':page_obj,
        'universities': universities
    })

def groups(request, u, f, d, l, s):
    university = University.objects.get(name=u)
    faculty = Faculty.objects.get(name=f)
    department = Department.objects.get(name=d)
    level = Level.objects.get(name=l)
    subject = Subject.objects.get(name=s)
    questions = Question.objects.filter(university=university, faculty=faculty, department=department,
                                        level=level, subject=subject)

    paginator = Paginator(questions, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'group.html', {
        'page_obj': page_obj
    })

def about(request):
    return render(request, 'about.html')
