from django.core.management.base import BaseCommand
from menu.models import MenuItem, Ingredient, MenuItemIngredient

class Command(BaseCommand):
    help = "Populate the MenuItemIngredient table with required ingredients for each menu item"

    def handle(self, *args, **kwargs):
        menu_item_ingredients_data = {
            "Beef Tacos": [
                {"ingredient_name": "Beef-Ground", "quantity_required": 200.00},
                {"ingredient_name": "Taco-Shells", "quantity_required": 4},
                {"ingredient_name": "Lettuce", "quantity_required": 50.00},
                {"ingredient_name": "Tomatoes", "quantity_required": 50.00},
                {"ingredient_name": "Cheddar-Cheese", "quantity_required": 50.00},
                {"ingredient_name": "Sour-Cream", "quantity_required": 50.00},
                {"ingredient_name": "Olive-Oil-Light", "quantity_required": 10.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black-Pepper", "quantity_required": 5.00},
            ],
            "Chicken Tacos": [
                {"ingredient_name": "Chicken-Breast", "quantity_required": 200.00},
                {"ingredient_name": "Bell-Peppers-Red", "quantity_required": 100.00},
                {"ingredient_name": "Onions", "quantity_required": 100.00},
                {"ingredient_name": "Tortillas", "quantity_required": 4},
                {"ingredient_name": "Olive-Oil-Light", "quantity_required": 10.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black-Pepper", "quantity_required": 5.00},
            ],
            "Vegan Tacos": [
                {"ingredient_name": "Black-Beans", "quantity_required": 200.00},
                {"ingredient_name": "Corn", "quantity_required": 100.00},
                {"ingredient_name": "Taco-Shells", "quantity_required": 4},
                {"ingredient_name": "Lettuce", "quantity_required": 50.00},
                {"ingredient_name": "Tomatoes", "quantity_required": 50.00},
                {"ingredient_name": "Cheddar-Cheese", "quantity_required": 50.00},
                {"ingredient_name": "Olive-Oil-Light", "quantity_required": 10.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black-Pepper", "quantity_required": 5.00},
            ],
            "Fish Tacos": [
                {"ingredient_name": "White-Fish", "quantity_required": 200.00},
                {"ingredient_name": "Tortillas", "quantity_required": 4},
                {"ingredient_name": "Cabbage-Green", "quantity_required": 100.00},
                {"ingredient_name": "Tomatoes", "quantity_required": 50.00},
                {"ingredient_name": "Limes", "quantity_required": 10.00},
                {"ingredient_name": "Olive-Oil-Light", "quantity_required": 10.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black-Pepper", "quantity_required": 5.00},
            ],
            "Pulled Pork Wrap": [
                {"ingredient_name": "Pork-Ground", "quantity_required": 200.00},
                {"ingredient_name": "Tortillas", "quantity_required": 4},
                {"ingredient_name": "Onions", "quantity_required": 50.00},
                {"ingredient_name": "Cilantro", "quantity_required": 10.00},
                {"ingredient_name": "Limes", "quantity_required": 10.00},
                {"ingredient_name": "Olive-Oil-Light", "quantity_required": 10.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black-Pepper", "quantity_required": 5.00},
            ],
            "Buffalo Chicken Wrap": [
                {"ingredient_name": "Tortillas", "quantity_required": 2},
                {"ingredient_name": "Chicken-Breast", "quantity_required": 200.00},
                {"ingredient_name": "Cheddar-Cheese", "quantity_required": 100.00},
                {"ingredient_name": "Bell-Peppers-Red", "quantity_required": 50.00},
                {"ingredient_name": "Onions", "quantity_required": 50.00},
                {"ingredient_name": "Olive-Oil-Light", "quantity_required": 10.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black-Pepper", "quantity_required": 5.00},
            ],
            "Shrimp Tacos": [
                {"ingredient_name": "Shrimp", "quantity_required": 200.00},
                {"ingredient_name": "Tortillas", "quantity_required": 4},
                {"ingredient_name": "Cabbage-Green", "quantity_required": 100.00},
                {"ingredient_name": "Avocado", "quantity_required": 50.00},
                {"ingredient_name": "Limes", "quantity_required": 10.00},
                {"ingredient_name": "Olive-Oil-Light", "quantity_required": 10.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black-Pepper", "quantity_required": 5.00},
            ],
        }

        for item_name, ingredients in menu_item_ingredients_data.items():
            try:
                menu_item = MenuItem.objects.get(name=item_name)
            except MenuItem.DoesNotExist:
                self.stdout.write(self.style.WARNING(f"MenuItem '{item_name}' not found, skipping..."))
                continue

            for ingredient_data in ingredients:
                try:
                    ingredient = Ingredient.objects.get(name=ingredient_data["ingredient_name"])
                except Ingredient.DoesNotExist:
                    self.stdout.write(self.style.WARNING(f"Ingredient '{ingredient_data['ingredient_name']}' not found, skipping..."))
                    continue

                quantity_required = ingredient_data["quantity_required"]
                
                # Create or update the MenuItemIngredient record
                obj, created = MenuItemIngredient.objects.update_or_create(
                    menu_item=menu_item,
                    ingredient=ingredient,
                    defaults={"quantity_required": quantity_required}
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f"Created {obj}"))
                else:
                    self.stdout.write(self.style.SUCCESS(f"Updated {obj}"))
