from django.db import models
from django.contrib.auth.models import User

# Anytime new classes or changes to classes happen, run:
# python manage.py makemigrations
# python manage.py migrate
# if you delete db.sqlite and migration folder or it is first time
# you are making migrations add app name to command like so:
# python manage.py makemigrations quiz


class Quiz(models.Model):
    name = models.CharField(max_length=120)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="duration of the quiz in minutes")

    def __str__(self):
        return f"{self.name}"

    def get_questions(self):
        return self.question_set.all()[:self.number_of_questions]

    class Meta:
        verbose_name_plural = 'Quizzes'


class Question(models.Model):
    text = models.CharField(max_length=250)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        return self.answer_set.all()


CHARACTERISTIC_CHOICES = (
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


class Answer(models.Model):
    text = models.CharField(max_length=100)
    score = models.IntegerField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    characteristic = models.CharField(max_length=20, choices=CHARACTERISTIC_CHOICES, default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"question: {self.question.text}, answer: {self.text}, score: {self.score}"


class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return str(self.pk)
