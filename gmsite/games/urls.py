from django.urls import include, path
from .views import (
    games_list,
    users_games,
)


app_name = 'games'

urlpatterns = [
    path('', games_list, name='games-list'),
    path('<pk>/', users_games, name='users-list'),
 ]
