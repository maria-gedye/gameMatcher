# Django views are Python functions that takes http requests and returns http response, like HTML documents.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Question
from .models import Choice
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


def results(request):
    response = "Your results are..."
    return HttpResponse(response)


def login(request):
    return render(request, 'quiz/login.html')


def gamer_test(request):
    latest_question_list = Question.objects.order_by('id')[:10]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'quiz/gamer-test.html', context)


"""  below function to return a post request when a user selects a choice """

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


