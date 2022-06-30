from django.shortcuts import render

# Create your views here.
# Olivias Code


def mainmenu_view(request):
    return render(request, 'home/MainMenu.html', {})


def game_view(request):
    return render(request, 'home/Games.html', {})


def about_view(request):
    return render(request, 'home/About.html', {})


def profile_view(request):
    return render(request, 'home/Profile.html', {})


def quizpage_view(request):
    return render(request, 'quiz/quiz.html', {})
# Olivias Code End
