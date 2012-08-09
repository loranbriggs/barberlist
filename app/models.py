from django.db import models

# Create your models here.
class Customers(models.Model):
    name = models.CharField(max_length = 20)
    barber = models.CharField(max_length = 20)
    trim = models.BooleanField(default = False)
    served = models.BooleanField(default = False)
    time  = models.DateTimeField(auto_now_add=True)

class Employees(models.Model):
    name = models.CharField(max_length = 20)
    available = models.BooleanField(default = True)

