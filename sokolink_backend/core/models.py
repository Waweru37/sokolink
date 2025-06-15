from django.db import models

class Farmer(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, unique=True)
    location = models.CharField(max_length=100)
    registered_at = models.DateTimeField(auto_now_add=True)

class Product(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    available_until = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
