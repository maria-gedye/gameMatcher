from django.contrib import admin
from .models import Quiz
from .models import Result
from .models import Question, Answer, Game

admin.site.register(Quiz)
admin.site.register(Result)
admin.site.register(Game)


class AnswerInline(admin.TabularInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]


admin.site.register(Question, QuestionAdmin)

