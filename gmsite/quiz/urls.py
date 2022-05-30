from django.urls import path
from .views import (
    QuizListView,
    quiz_view
)

app_name = 'quizzes'

urlpatterns = [
    path('', QuizListView.as_view(), name='main-view'),
    # primary key is important and is how we retrieve the quiz object
    path('<pk>/', quiz_view, name='quiz-view')
]

