from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from app.models import Customers
from app.models import Employees
import json
from django.http import HttpResponse


def customer_pg(request):
    if request.method =='GET':
        return get_cust(request)
    if request.method =='POST':
        return add_cust(request)

def employee_pg(request):
    if request.method =='GET':
        return get_employ(request)
    if request.method =='POST':
        return add_employ(request)
    if request.method =='PUT':
        return update_employ(request)

def get_cust(request):
    customers = Customers.objects.all()
    employees = Employees.objects.all()#filter(available=True)
    c = {'customers': customers, 'employees': employees}
    c.update(csrf(request))
    get_employ(request)
    return render(request, 'home.html', c)

def add_cust(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        barber = request.POST.get('barber')
        trim = request.POST.get('trim')
        if name:
            customer = Customers()
            customer.name = name
            customer.barber = barber
            if trim:
                customer.trim = trim
            customer.save()
    return get_cust(request)

def get_employ(request):
    employees = Employees.objects.all()
    c = {'employees': employees}
    c.update(csrf(request))
    return render(request, 'employees.html', c)

def add_employ(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            employee = Employees()
            employee.name = name
            employee.save()
    return get_employ(request)

def archive(request):
    customers = Customers.objects.all()
    c = {'customers': customers}
    c.update(csrf(request))
    return render(request, 'archive.html', c)

@csrf_exempt
def update_employ(request):
    data = json.loads(request.raw_post_data)
    status = data.get("available")
    employ_id = data.get("employ_id")
    employee = Employees.objects.filter(id=employ_id)
    if status == True:
        employee.available=True
    if status == False:
        employee.available=False
    employee.save()
    return get_employ(request)
