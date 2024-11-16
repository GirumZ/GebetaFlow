from django.contrib import admin
from .models import Ingredient, MenuItem, Section, Category, MenuItemIngredient, IngredientType, IngredientTag

# Register your models here.

admin.site.register([Ingredient, MenuItem, Section, Category, MenuItemIngredient, IngredientType, IngredientTag])