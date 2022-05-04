from django.shortcuts import render
from django.http import HttpResponse

# writing my first view
def index(request):
    return HttpResponse("kia ora tatou...Quiz home page here")

