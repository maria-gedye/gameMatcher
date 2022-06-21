from django.contrib import admin
from .models import Quiz
from .models import Result
from .models import Question, Answer

admin.site.register(Quiz)
admin.site.register(Result)


class AnswerInline(admin.TabularInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]  # allow answer fields to be edited on same page as question fields


admin.site.register(Question, QuestionAdmin)

