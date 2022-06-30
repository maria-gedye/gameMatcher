from django.shortcuts import render
from .models import Quiz
from django.views.generic import ListView
from django.http import JsonResponse
from .models import Question, Answer, Result


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
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        questions = []
        data = request.POST
        data_ = dict(data.lists())

        data_.pop('csrfmiddlewaretoken')

        for k in data_.keys():
            question = Question.objects.get(text=k)
            questions.append(question)

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
        incomplete_count = 0
        results = []

        for q in questions:
            a_selected = request.POST.get(q.text)

            if a_selected != "":
                question_answers = Answer.objects.filter(question=q)
                for a in question_answers:

                    if a_selected == a.text:
                        ck = characteristic_scores.keys()
                        for k in ck:
                            if q.characteristic == k:
                                characteristic_scores[k] += a.score
                # if the question's characteristic matches the dict's key
                # take the answers score and update the matching key's value
                results.append({str(q): a_selected})

            else:
                results.append({str(q): 'not answered'})
                incomplete_count += 1

        results.append(characteristic_scores)

# remove characteristics that score under 4 and store into a new dict
        hiscore = {k: v for k, v in characteristic_scores.items() if v > 4}
# create a sorted list of the above dict's keys
        hiscore_keys = sorted(hiscore, key=hiscore.get, reverse=True)
        print(hiscore_keys)
# create a new result object
        Result.objects.create(quiz=quiz, user=user, hiscore=hiscore_keys)

        if incomplete_count == 0:
            return JsonResponse({'all_questions_complete': True, 'results': results, 'scores': characteristic_scores})
        else:
            return JsonResponse({'all_questions_complete': False, 'results': results, 'scores': characteristic_scores})


def results_view(request, pk):
    result_obj = Result.objects.get(id=pk)
    print(result_obj)
    context = {
        'user_result': result_obj
    }
    return render(request, 'results.html', context)