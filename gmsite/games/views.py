from django.shortcuts import render
from .models import Game, UsersProfile
from django.http import HttpResponse
# MATCHING PART OF THE APP

# Functions needed:
# a for loop that matches any value from the user's hiscore against a game's genre values.
# count how many genres match per game
# sort games out. games with the highest number of matching genres are ordered first
# store sorted games to a dictionary, pass this into another model called games_list
# display games in a listed table format, allow users to delete games and reorder them
HTML_STRING = """
<h1>GAMES LIST</h1>
"""


def games_list(request):
    # game_obj = Game.objects.get(id=) this is to get a single object
    games_queryset = Game.objects.all()
    print(games_queryset)    # prints after server is closed

    context = {
        'object_list': games_queryset
    }
    print(context)
    return render(request, 'games.html', context)



