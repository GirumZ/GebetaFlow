# from django.shortcuts import render
from rest_framework import viewsets
from .models import (
    MenuItem, Category, Section, Ingredient, MenuItemIngredient,
    IngredientType, IngredientTag
)
from .serializers import (
    IngredientSerializer, IngredientTagSerializer, IngredientTypeSerializer, CategorySerializer,
    SectionSerializer, MenuItemIngredientSerializer, MenuItemSerializer
)


"""
# Create your views here.
def list_menu(request):
    items = MenuItem.objects.prefetch_related('menuitemingredient_set__ingredient')
    return render(request, 'menu/menu_list.html', {'items': items})
"""
class IngredientTypeViewSet(viewsets.ModelViewSet):
    queryset = IngredientType.objects.all()
    serializer_class = IngredientTypeSerializer

class IngredientTagViewSet(viewsets.ModelViewSet):
    queryset = IngredientTag.objects.all()
    serializer_class = IngredientTagSerializer

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class MenuItemIngredientViewSet(viewsets.ModelViewSet):
    queryset = MenuItemIngredient.objects.all()
    serializer_class = MenuItemIngredientSerializer