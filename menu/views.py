from django.shortcuts import render
from .models import MenuItem, Category, Section, Ingredient, MenuItemIngredient

# Create your views here.
def list_menu(request):
    items = MenuItem.objects.prefetch_related('menuitemingredient_set__ingredient')
    return render(request, 'menu/menu_list.html', {'items': items})