from django.db import models
from django.contrib.auth.models import User

# We will need a game model to store game objects into the database
# the game model needs an attribute called genre which takes a value of a list of genres
# We will need to import the result model from quiz to access the user's hiscore


class GamesList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_games(self):
        games = list(self.game_set.all())
        return games


class Game(models.Model):
    name = models.CharField(max_length=250)
    games_list = models.ForeignKey(GamesList, on_delete=models.CASCADE)
    year = models.IntegerField()
    image = models.ImageField(blank=True, upload_to='images')
    genres = models.JSONField(default=list)
    info = models.CharField(max_length=250)

    def __str__(self):
        return f"game: {self.name}, id: {str(self.pk)}, genres: {self.genres}, year: {self.year}, info: {self.info}"

