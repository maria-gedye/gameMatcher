from django.contrib import admin
from .models import Game
from .models import GamesList

admin.site.register(Game)
admin.site.register(GamesList)

