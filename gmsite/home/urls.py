from django.urls import path
from django.views.generic import TemplateView
from .views import (
 mainmenu_view, # Olivias code
    game_view, # Olivias code
    about_view, # Olivias code
    profile_view, # Olivias code
    quizpage_view # Olivias code
)


app_name = 'home'

urlpatterns = [
    # Olivias code

    #creating a path for views.py
    path('', TemplateView.as_view(template_name="home/MainMenu.html"), name='main-view'),
    path('', mainmenu_view, name="mainmenu-view"),
    path('games/', game_view, name='game-view'),
    path('about/', about_view, name='about-view'),
    path('profile/', profile_view, name='profile-view'),
    path('quiz/', quizpage_view,name='quizpage-view' ),
      # Olivias code end
]