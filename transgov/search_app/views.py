from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    my_dict = {'inseart_me':"from Tranparent Governance Team"}
    return render(request, 'search_app/index.html', context=my_dict)
