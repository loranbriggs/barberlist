from django.db import models

# Create your models here.
class Customers(models.Model):
    name = models.CharField(max_length = 20)
    barber = models.CharField(max_length = 20)
    trim = models.BooleanField("trim?")
    served = models.BooleanField("served?")
    time  = models.DateTimeField(auto_now_add=True)

class Employees(models.Model):
    AVAILABLE = ( ('A', 'Available'), ('U', 'Unavailable') )

    name = models.CharField(max_length = 20)
    available = models.CharField(default='A', max_length=1, choices=AVAILABLE)

