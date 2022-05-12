from django.http import HttpResponse
from django.shortcuts import render
from .models import Question
from django.http import Http404


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


def results(request):
    response = "Your results are..."
    return HttpResponse(response)

# thinking of having 2 quizzes: 1) Gamer Motivation     2) Personality
