from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

def index2(request):
    return HttpResponse("hello im from views.py file")
