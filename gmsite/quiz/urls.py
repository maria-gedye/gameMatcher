from django.urls import path
from django.views.generic import TemplateView
from .views import (
    QuizListView,
    quiz_view,
    quiz_data_view,
    save_quiz_view,
    results_view,

)

app_name = 'quizzes'

urlpatterns = [
    path('', QuizListView.as_view(), name='quiz-list'),
    # primary key is important and is how we retrieve the quiz object
    path('<pk>/', quiz_view, name='quiz-view'),
    path('<pk>/save/', save_quiz_view, name='save-view'),
    path('<pk>/data/', quiz_data_view, name='quiz-data-view'),
    path('<pk>/results/', results_view, name='results-view'),

]

