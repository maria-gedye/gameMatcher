from django.shortcuts import render
from .models import GamesList, Game
from django.http import JsonResponse

# Functions needed:
# a for loop that matches any value from the user's hiscore against a game's genre values.
# count how many genres match per game
# sort games out. games with the highest number of matching genres are ordered first
# store sorted games to a dictionary, pass this into another model called games_list
# display games in a listed table format, allow users to delete games and reorder them


def games_list_view(request, pk):       # displaying all games
    games_list = GamesList.objects.get(pk=pk)
    print(games_list)
    users_games = []
    #for g in games_list.get_games():

        # if g.genre == to result.hiscore
        # append g to users_games[]
    pass


def game_detail(request, pk):     # displaying an individual game
    pass
