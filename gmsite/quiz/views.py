# Django views are Python functions that takes http requests and returns http response, like HTML documents.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Question, Answer
from django.http import Http404
from django.urls import reverse


# writing my first view
def index(request):
    latest_question_list = Question.objects.order_by('id')[:10]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'quiz/index.html', context)


# let's write more views (web pages) this time they take an argument
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'quiz/detail.html', {'question': question})


def results():
    response = "Your results are..."
    return HttpResponse(response)


def login(request):
    return render(request, 'quiz/login.html')


def gamer_test(request):
    latest_question_list = Question.objects.order_by('id')[:10]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'quiz/gamer-test.html', context)




