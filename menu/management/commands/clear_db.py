from django.core.management.base import BaseCommand
from menu.models import IngredientType, Ingredient, IngredientTag, Category, Section, MenuItem, MenuItemIngredient  

class Command(BaseCommand):
    help = 'Clears all data from specified models'

    def handle(self, *args, **kwargs):
        
        self.stdout.write("Clearing data from Ingredient model...")
        Ingredient.objects.all().delete()

        self.stdout.write("Clearing data from IngredientType model...")
        IngredientType.objects.all().delete()

        self.stdout.write("Clearing data from IngredientTag model...")
        IngredientTag.objects.all().delete()

        self.stdout.write("Clearing data from Category model...")
        Category.objects.all().delete()

        self.stdout.write("Clearing data from Section model...")
        Section.objects.all().delete()

        self.stdout.write("Clearing data from MenuItem model...")
        MenuItem.objects.all().delete()

        self.stdout.write("Clearing data from MenuItemIngredient model...")
        MenuItemIngredient.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Database cleared successfully!'))
