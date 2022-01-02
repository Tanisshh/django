from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import Record, Topic, WebPage
from firstapp.form import NewUser


def index(request):
    date_list = Record.objects.order_by('date')
    webpage_dict = {'accessrecords':date_list}
    return render(request, 'index.html', context = webpage_dict)

def index2(request):
    form = NewUser()
    if request.method == 'post':
        form = NewUser(request.post)

        if form.is_valid():

            form.save(commit=True)
            return index(request)

        else:
            print("validation error")

    return render(request, 'form.html',{'form': form})
