from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    quantity_in_stock = models.DecimalField(max_digits=6, decimal_places=2)
    unit = models.CharField(max_length=20)
