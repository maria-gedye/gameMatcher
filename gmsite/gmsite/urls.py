from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    # point the root URLconf at the quiz.urls module
    path('quiz/', include('quiz.urls')),
    path('admin/', admin.site.urls),
]
