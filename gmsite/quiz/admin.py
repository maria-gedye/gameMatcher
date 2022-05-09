from django.contrib import admin
from .models import Question
from .models import Choice

# tell admin that question objects have an admin interface...
# aka register your models to admin
admin.site.register(Question)
admin.site.register(Choice)

