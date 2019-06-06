from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime as dt
from .models import Question, Category, Note
from .forms import *
from django.contrib.auth.decorators import login_required

def index(request):

    return render(request, 'index.html')

def questions(request):

    flask=Question.objects.filter(category__category_name='Flask').all()
    python=Question.objects.filter(category__category_name='Python').all()
    javascript=Question.objects.filter(category__category_name='JavaScript').all()
    jQuery=Question.objects.filter(category__category_name='JQuery').all()
    java=Question.objects.filter(category__category_name='Java').all()
    angular=Question.objects.filter(category__category_name='Angular').all()
    django=Question.objects.filter(category__category_name='Django').all()
    html=Question.objects.filter(category__category_name='HTML').all()
    postgresql=Question.objects.filter(category__category_name='Postgresql').all()
    general=Question.objects.filter(category__category_name='General').all()

    return render(request, 'questions.html', {"flask":flask,"python":python,"javascript":javascript,"jQuery":jQuery,"java":java,"angular":angular,"django":django,"html":html,"postgresql":postgresql,"general":general})

def notes(request):

    flask=Note.objects.filter(category__category_name='Flask').all()
    python=Note.objects.filter(category__category_name='Python').all()
    javascript=Note.objects.filter(category__category_name='JavaScript').all()
    jQuery=Note.objects.filter(category__category_name='JQuery').all()
    java=Note.objects.filter(category__category_name='Java').all()
    angular=Note.objects.filter(category__category_name='Angular').all()
    django=Note.objects.filter(category__category_name='Django').all()
    html=Note.objects.filter(category__category_name='HTML').all()
    postgresql=Note.objects.filter(category__category_name='Postgresql').all()
    general=Note.objects.filter(category__category_name='General').all()

    return render(request, 'notes.html', {"flask":flask,"python":python,"javascript":javascript,"jQuery":jQuery,"java":java,"angular":angular,"django":django,"html":html,"postgresql":postgresql,"general":general})
