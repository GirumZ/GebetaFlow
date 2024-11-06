from django.core.management.base import BaseCommand
from menu.models import MenuItem, Ingredient, MenuItemIngredient

class Command(BaseCommand):
    help = "Populate the MenuItemIngredient table with required ingredients for each menu item"

    def handle(self, *args, **kwargs):
        menu_item_ingredients_data = {
            "Filet Mignon": [
                {"ingredient_name": "Filet Mignon", "quantity_required": 200.00},
                {"ingredient_name": "Olive Oil", "quantity_required": 10.00},
                {"ingredient_name": "Garlic", "quantity_required": 5.00},
                {"ingredient_name": "Rosemary", "quantity_required": 5.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
            ],
            "Ribeye Steak": [
                {"ingredient_name": "Ribeye Steak", "quantity_required": 200.00},
                {"ingredient_name": "Olive Oil", "quantity_required": 10.00},
                {"ingredient_name": "Garlic", "quantity_required": 5.00},
                {"ingredient_name": "Rosemary", "quantity_required": 5.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
            ],
            "T-Bone Steak": [
                {"ingredient_name": "T-Bone Steak", "quantity_required": 200.00},
                {"ingredient_name": "Olive Oil", "quantity_required": 10.00},
                {"ingredient_name": "Garlic", "quantity_required": 5.00},
                {"ingredient_name": "Rosemary", "quantity_required": 5.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
            ],
            "Sirloin Steak": [
                {"ingredient_name": "Sirloin Steak", "quantity_required": 200.00},
                {"ingredient_name": "Olive Oil", "quantity_required": 10.00},
                {"ingredient_name": "Garlic", "quantity_required": 5.00},
                {"ingredient_name": "Rosemary", "quantity_required": 5.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
            ],
            "Steak Diane": [
                {"ingredient_name": "Beef Steak", "quantity_required": 200.00},
                {"ingredient_name": "Olive Oil", "quantity_required": 10.00},
                {"ingredient_name": "Butter", "quantity_required": 20.00},
                {"ingredient_name": "Garlic", "quantity_required": 5.00},
                {"ingredient_name": "Onions", "quantity_required": 30.00},
                {"ingredient_name": "Marsala Wine", "quantity_required": 50.00},
                {"ingredient_name": "Parsley", "quantity_required": 5.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
            ],
            "Steak Frites": [
                {"ingredient_name": "Beef Steak", "quantity_required": 200.00},
                {"ingredient_name": "Olive Oil", "quantity_required": 10.00},
                {"ingredient_name": "Garlic", "quantity_required": 5.00},
                {"ingredient_name": "Rosemary", "quantity_required": 5.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Potatoes", "quantity_required": 150.00},
            ],
            "New York Strip": [
                {"ingredient_name": "New York Strip Steak", "quantity_required": 200.00},
                {"ingredient_name": "Olive Oil", "quantity_required": 10.00},
                {"ingredient_name": "Garlic", "quantity_required": 5.00},
                {"ingredient_name": "Rosemary", "quantity_required": 5.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
            ],
            "Bistro Steak": [
                {"ingredient_name": "Bistro Steak", "quantity_required": 200.00},
                {"ingredient_name": "Olive Oil", "quantity_required": 10.00},
                {"ingredient_name": "Garlic", "quantity_required": 5.00},
                {"ingredient_name": "Rosemary", "quantity_required": 5.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
            ],
            "Surf & Turf": [
                {"ingredient_name": "Filet Mignon", "quantity_required": 200.00},
                {"ingredient_name": "Lobster Tail", "quantity_required": 200.00},
                {"ingredient_name": "Olive Oil", "quantity_required": 10.00},
                {"ingredient_name": "Garlic", "quantity_required": 5.00},
                {"ingredient_name": "Lemon Juice", "quantity_required": 10.00},
                {"ingredient_name": "Rosemary", "quantity_required": 5.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
            ],
            "Peppercorn Steak": [
                {"ingredient_name": "Beef Steak", "quantity_required": 200.00},
                {"ingredient_name": "Peppercorns", "quantity_required": 5.00},
                {"ingredient_name": "Olive Oil", "quantity_required": 10.00},
                {"ingredient_name": "Garlic", "quantity_required": 5.00},
                {"ingredient_name": "Butter", "quantity_required": 20.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
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
