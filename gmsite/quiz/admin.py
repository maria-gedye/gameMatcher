from django.contrib import admin
from .models import Quiz
from .models import Result
from .models import Question, Answer

admin.site.register(Quiz)
admin.site.register(Result)


class AnswerInline(admin.TabularInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]


admin.site.register(Question, QuestionAdmin)

