from django.core.context_processors import csrf
from django.shortcuts import render
from app.models import Customers
from app.models import Employees
import json
from django.http import HttpResponse


def get_names(request):
    customers = Customers.objects.all()
    c = {'customers': customers}
    c.update(csrf(request))
    return render(request, 'home.html', c)

def get_employ(request):
    employees = Employees.objects.all()
    c = {'employees': employees}
    c.update(csrf(request))
    return render(request, 'employees.html', c)


def add_name(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            customer = Customers()
            customer.name = name
            customer.save()
    return HttpResponse()

def add_employ(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            employee = Employees()
            employee.name = name
            employee.available = 'A'
            employee.save()
    return HttpResponse()

def archive(request):
    customers = Customers.objects.all()
    c = {'customers': customers}
    c.update(csrf(request))
    return render(request, 'archive.html', c)
