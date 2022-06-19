from django.db import models
from quiz/models import Result

# We will need a game model to store game objects into the database
# the game model needs an attribute called genre which takes a value of a list of genres
# We will need to import the result model from quiz to access the user's hiscore

# Functions needed:
# a for loop that matches any value from the user's hiscore against a game's genre values.
# count how many genres match per game
# sort games out. games with the highest number of matching genres are ordered first
# store sorted games to a dictionary or into another model called user_games
# display games in a listed table format, allow users to delete games and reorder them

# this below class is to create a custom django field so that the game model
# return a list when accessed


class SeparatedValuesField(models.TextField):
    __metaclass__ = models.SubfieldBase

    def __init__(self, *args, **kwargs):
        self.token = kwargs.pop('token', ',')
        super(SeparatedValuesField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            return
        if isinstance(value, list):
            return value
        return value.split(self.token)

    def get_db_prep_value(self, value):
        if not value:
            return
        assert(isinstance(value, list) or isinstance(value, tuple))
        return self.token.join([unicode(s) for s in value])

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)


class Game(models.Model):
    name = models.CharField(max_length=250)
    year = models.IntegerField()
    image = models.ImageField(blank=True, upload_to='images')
    genres = SeparatedValuesField()
    info = models.CharField(max_length=250)

