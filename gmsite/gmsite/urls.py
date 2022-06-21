from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('quiz/', include('quiz.urls', namespace='quizzes')),
    path('games/', include('games.urls')),
]
