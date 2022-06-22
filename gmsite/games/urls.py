from django.urls import include, path
from .views import (
    games_list,
    go_to_quiz
)


app_name = 'games'

urlpatterns = [
    path('', games_list, name='games-list'),
 ]
