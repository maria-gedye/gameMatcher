from django.shortcuts import render
from .models import Quiz
from django.views.generic import ListView
from django.http import JsonResponse
from .models import Question, Answer


class QuizListView(ListView):
    model = Quiz
    template_name = 'quiz/main.html'


def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(request, 'quiz/quiz.html', {'obj': quiz})


def quiz_data_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = []
    for q in quiz.get_questions():
        answers = []  # reset to empty when the next question loops
        for a in q.get_answers():
            answers.append(a.text)
        # store current question and answers in a dictionary
        questions.append({str(q): answers})
    return JsonResponse({
        'data': questions,
        'time': quiz.time,
    })


def save_quiz_view(request, pk):
    #print(request.POST)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        questions = []
        data = request.POST
        data_ = dict(data.lists())

        data_.pop('csrfmiddlewaretoken')

        for k in data_.keys():
            print('key: ', k)
            question = Question.objects.get(text=k)
            questions.append(question)
        #print(questions)

        user = request.user
        quiz = Quiz.objects.get(pk=pk)
        # going to need dict to store each characteristic score
        characteristic_scores = {
            'action': 0,
            'strategy': 0,
            'aesthetics': 0,
            'competition': 0,
            'fellowship': 0,
            'challenge': 0,
            'discovery': 0,
            'completion': 0,
            'expression': 0,
            'story': 0
        }
        score = 0
        multiplier = 100 / quiz.number_of_questions
        results = []

        for q in questions:
            a_selected = request.POST.get(q.text)

            if a_selected != "":
                question_answers = Answer.objects.filter(question=q)
                for a in question_answers:
                    if a_selected == a.text:
                        ck = characteristic_scores.keys()
                        for k in ck:
                            if a.characteristic == k:
                                score += a.score
                                characteristic_scores[k] = score
                                score = 0
                # if the answers characteristic matches the dict's key
                # take the answers score and update the matching key's value
                print(characteristic_scores)

    return JsonResponse({'text': 'works'})




