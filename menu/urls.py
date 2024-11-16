from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_menu, name='menu_list')
]