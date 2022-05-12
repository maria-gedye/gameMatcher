from django.urls import path

from . import views

# to call views in views.py we need to map it to a URL using URLconf
urlpatterns = [
    # so path functions take 4 args: route(str, req), view(req), kwargs, name
    path('', views.index, name='index'),
    # path for individual question
    path('<int:question_id>/', views.detail, name='detail'),
    # path for results
    path('results/', views.results, name='results')
]
