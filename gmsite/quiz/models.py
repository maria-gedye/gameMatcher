from django.db import models

# Create 2 models here: Question and Choice
# models are represented by python classes

class Question(models.Model):
    question_text = models.CharField(max_length = 250)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    # change below to work for a scale choice (instead of a bi-choice)
    votes = models.IntegerField(default=0)

