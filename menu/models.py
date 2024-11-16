from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.

class IngredientType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class IngredientTag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=50, unique=True)
    ingredient_type = models.ForeignKey(IngredientType,  on_delete=models.SET_NULL, null=True, blank=True)
    quantity_in_stock = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=20, choices=[
        ('g', 'grams'),
        ('ml', 'milliliters'),
        ('pcs', 'pieces'),
    ])
    ingredient_tags = models.ManyToManyField(IngredientTag, blank=True)

    def __str__(self):
        return(self.name)
    
    def clean(self):
        if self.quantity_in_stock < 0:
            raise ValidationError("Quantity in stock can not be negative")

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return(self.name)

class Section(models.Model):
    name = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True)

    def __str__(self):
        return(self.name)

class MenuItem(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    section = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return(self.name)

class MenuItemIngredient(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity_required = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return(self.menu_item.name + "-" + self.ingredient.name)
    
    def clean(self):
        if self.quantity_required < 0:
            raise ValidationError("Quantity required can not be negative")