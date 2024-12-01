from django.urls import path, include
# from . import views
from rest_framework.routers import DefaultRouter
from .views import (
    IngredientTypeViewSet, IngredientTagViewSet, IngredientViewSet, CategoryViewSet,
    SectionViewSet, MenuItemViewSet, MenuItemIngredientViewSet
)

"""
urlpatterns = [
    path('', views.list_menu, name='menu_list')
]
"""

router = DefaultRouter()
router.register('ingredient-type', IngredientTypeViewSet)
router.register('ingredient-tag', IngredientTagViewSet)
router.register('ingredients', IngredientViewSet)
router.register('categories', CategoryViewSet)
router.register('sections', SectionViewSet)
router.register('menu-items', MenuItemViewSet)
router.register('menu-item-ingredients', MenuItemIngredientViewSet)

urlpatterns = [
    path('menu/', include(router.urls)),
]