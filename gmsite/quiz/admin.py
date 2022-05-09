from django.contrib import admin
from .models import Question

# tell admin that question objects have an admin interface...
# aka register your models to admin
admin.site.register(Question)

