from django.urls import path
from django.views.generic import TemplateView
from .views import (
    QuizListView,
    quiz_view,
    quiz_data_view,
    save_quiz_view,
    mainmenu_view, # Olivias code 
    game_view, # Olivias code 
    about_view, # Olivias code 
    profile_view, # Olivias code 
    quizpage_view # Olivias code
)

app_name = 'quizzes'

urlpatterns = [
    # Olivias code 

    #creating a path for views.py
    path('', TemplateView.as_view(template_name="quiz/MainMenu.html"), name='main-view'),
    path('main/', mainmenu_view, name="mainmenu-view"),
    path('games/', game_view, name='game-view'),
    path('about/', about_view, name='about-view'),
    path('profile/', profile_view, name='profile-view'),
    path('quiz/', quizpage_view,name='quizpage-view' ),
      # Olivias code end
    # primary key is important and is how we retrieve the quiz object
    path('<pk>/', quiz_view, name='quiz-view'),
    path('<pk>/save/', save_quiz_view, name='save-view'),
    path('<pk>/data/', quiz_data_view, name='quiz-data-view')
]

