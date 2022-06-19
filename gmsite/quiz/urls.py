from django.urls import path
from django.views.generic import TemplateView
from .views import (
    QuizListView,
    quiz_view,
    quiz_data_view,
    save_quiz_view
)

app_name = 'quizzes'

urlpatterns = [
    path('', TemplateView.as_view(template_name="quiz/MainMenu.html"), name='main-view'),
    # primary key is important and is how we retrieve the quiz object
    path('<pk>/', quiz_view, name='quiz-view'),
    path('<pk>/save/', save_quiz_view, name='save-view'),
    path('<pk>/data/', quiz_data_view, name='quiz-data-view')
]

