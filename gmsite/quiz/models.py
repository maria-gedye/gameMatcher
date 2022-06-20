from django.db import models
from django.contrib.auth.models import User
import random

# Anytime new classes or changes to classes happen, run:
# python manage.py makemigrations
# python manage.py migrate

# QUIZ PART OF THE APP


class Quiz(models.Model):
    name = models.CharField(max_length=120)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="duration of the quiz in minutes")

    def __str__(self):
        return f"{self.name}"

    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.number_of_questions]

    class Meta:
        verbose_name_plural = 'Quizzes'


CHARACTERISTIC_CHOICES = (
    ('---', '---'),
    ('action', 'action'),
    ('strategy', 'strategy'),
    ('aesthetics', 'aesthetics'),
    ('competition', 'competition'),
    ('fellowship', 'fellowship'),
    ('challenge', 'challenge'),
    ('discovery', 'discovery'),
    ('completion', 'completion'),
    ('expression', 'expression'),
    ('story', 'story')
)


class Question(models.Model):
    text = models.CharField(max_length=250)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    characteristic = models.CharField(max_length=22, choices=CHARACTERISTIC_CHOICES, default=0)

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        return self.answer_set.all()


class Answer(models.Model):
    text = models.CharField(max_length=100)
    score = models.IntegerField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"question: {self.question.text}, answer: {self.text}, score: {self.score}"


class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # store user's hiscores as a list
    hiscore = models.JSONField(default=list)

    def __str__(self):
        return str(self.pk)


# MATCHING PART OF THE APP

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
    year = models.IntegerField()
    image = models.ImageField(blank=True, upload_to='images')
    genres = models.JSONField(default=list)
    info = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.name}, {self.year}"
