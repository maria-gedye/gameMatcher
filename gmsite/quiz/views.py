from django.shortcuts import render
from django.http import HttpResponse


# writing my first view
def index(request):
    return HttpResponse("kia ora tatou...Quiz home page here")


# let's write more views (web pages) this time they take an argument
def detail(request, question_id):
    return HttpResponse("Question " % question_id)

def results(request)
    response = "Your results are..."
    return HttpResponse(response)

# thinking of having 2 quizzes: 1) Gamer Motivation     2) Personality
