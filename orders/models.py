from accounts.models import User
from django.db import models
from django.conf import settings

# Create your models here.

    
class Vehicle(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Details(models.Model):
    year = models.IntegerField()
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='details')
    model = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.vehicle} ({self.price})"

class Order(models.Model):
    
    #add user details to ther order
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=100)
    
    product = models.ForeignKey(Details, on_delete=models.CASCADE, related_name='orders')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    quantity = models.IntegerField(default=1)
    date_ordered = models.DateTimeField(auto_now_add=True)

