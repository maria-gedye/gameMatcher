from django.db import models


# Create 2 models here: Question and Choice
# models are represented by python classes

# USE python manage.py makemigrations to create migrations for any changes below
# USE python manage.py migrate to apply those changes to the database

class Question(models.Model):
    question_text = models.CharField(max_length=250)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    # change below to work for a scale choice (instead of a bi-choice)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
