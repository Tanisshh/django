from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import Record, Topic, WebPage


def index(request):
    date_list = Record.objects.order_by('date')
    webpage_dict = {'accessrecords':date_list}
    return render(request, 'index.html', context=webpage_dict)

def index2(request):
    return HttpResponse("hello im from views.py file")
