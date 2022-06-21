from django.urls import path
from .views import (
    games_list,
)


app_name = 'games'

urlpatterns = [
    path('', games_list, name='games-list'),
 ]