
from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=10)
    age = models.CharField(max_length=10)
    address = models.CharField(max_length=10)




class Product(models.Model):
    shape = models.CharField(max_length=10)
    size = models.CharField(max_length=10)
    location = models.CharField(max_length=10)
    price = models.CharField(max_length=10)
    
    


    