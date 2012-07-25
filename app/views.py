# Create your views here.

from django.shortcuts import render

def home(request):
    c = {'content':'this is the start of project barberlist'}
    return render(request, 'home.html', c)
