from django.urls import path
from .views import (
    games_view,
)

urlpatterns = [
    path('<pk>/games', games_view, name='games-view'),

]