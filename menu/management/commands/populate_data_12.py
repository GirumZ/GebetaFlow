from django.core.management.base import BaseCommand
from menu.models import MenuItem, Ingredient, MenuItemIngredient

class Command(BaseCommand):
    help = "Populate the MenuItemIngredient table with required ingredients for each menu item"

    def handle(self, *args, **kwargs):
        menu_item_ingredients_data = {
            "BBQ Ribs": [
                {"ingredient_name": "Pork Ribs", "quantity_required": 200.00},
                {"ingredient_name": "BBQ Sauce", "quantity_required": 100.00},
                {"ingredient_name": "Olive Oil", "quantity_required": 10.00},
                {"ingredient_name": "Garlic Powder", "quantity_required": 5.00},
                {"ingredient_name": "Onion Powder", "quantity_required": 5.00},
                {"ingredient_name": "Paprika", "quantity_required": 5.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
            ],
            "Grilled Lamb Chops": [
                {"ingredient_name": "Lamb Chops", "quantity_required": 200.00},
                {"ingredient_name": "Garlic", "quantity_required": 5.00},
                {"ingredient_name": "Rosemary", "quantity_required": 5.00},
                {"ingredient_name": "Olive Oil", "quantity_required": 10.00},
                {"ingredient_name": "Lemon Juice", "quantity_required": 20.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
            ],
            "Pork Belly Skewers": [
                {"ingredient_name": "Pork Belly", "quantity_required": 200.00},
                {"ingredient_name": "Soy Sauce", "quantity_required": 50.00},
                {"ingredient_name": "Honey", "quantity_required": 10.00},
                {"ingredient_name": "Garlic", "quantity_required": 5.00},
                {"ingredient_name": "Ginger", "quantity_required": 5.00},
                {"ingredient_name": "Skewers", "quantity_required": 4},
                {"ingredient_name": "Olive Oil", "quantity_required": 10.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
            ],
            "Grilled Chicken Wings": [
                {"ingredient_name": "Chicken Wings", "quantity_required": 300.00},
                {"ingredient_name": "BBQ Sauce", "quantity_required": 100.00},
                {"ingredient_name": "Olive Oil", "quantity_required": 10.00},
                {"ingredient_name": "Garlic Powder", "quantity_required": 5.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
            ],
            "Grilled Vegetable Platter": [
                {"ingredient_name": "Assorted Vegetables", "quantity_required": 300.00},
                {"ingredient_name": "Olive Oil", "quantity_required": 20.00},
                {"ingredient_name": "Vinegar", "quantity_required": 10.00},
                {"ingredient_name": "Garlic", "quantity_required": 5.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
            ],
            "BBQ Brisket": [
                {"ingredient_name": "Beef Brisket", "quantity_required": 300.00},
                {"ingredient_name": "BBQ Sauce", "quantity_required": 100.00},
                {"ingredient_name": "Garlic Powder", "quantity_required": 5.00},
                {"ingredient_name": "Onion Powder", "quantity_required": 5.00},
                {"ingredient_name": "Paprika", "quantity_required": 5.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
            ],
            "Grilled Shrimp Kabobs": [
                {"ingredient_name": "Shrimp", "quantity_required": 200.00},
                {"ingredient_name": "Bell Peppers", "quantity_required": 100.00},
                {"ingredient_name": "Onions", "quantity_required": 100.00},
                {"ingredient_name": "Olive Oil", "quantity_required": 10.00},
                {"ingredient_name": "Garlic", "quantity_required": 5.00},
                {"ingredient_name": "Lemon Juice", "quantity_required": 20.00},
                {"ingredient_name": "Skewers", "quantity_required": 4},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
            ],
            "Grilled Sausages": [
                {"ingredient_name": "Sausages", "quantity_required": 200.00},
                {"ingredient_name": "Onions", "quantity_required": 100.00},
                {"ingredient_name": "Bell Peppers", "quantity_required": 100.00},
                {"ingredient_name": "Olive Oil", "quantity_required": 10.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
            ],
            "Beef Skewers": [
                {"ingredient_name": "Beef", "quantity_required": 200.00},
                {"ingredient_name": "Bell Peppers", "quantity_required": 100.00},
                {"ingredient_name": "Onions", "quantity_required": 100.00},
                {"ingredient_name": "Olive Oil", "quantity_required": 10.00},
                {"ingredient_name": "Garlic", "quantity_required": 5.00},
                {"ingredient_name": "Skewers", "quantity_required": 4},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
            ],
            "Grilled Portobello Mushrooms": [
                {"ingredient_name": "Portobello Mushrooms", "quantity_required": 300.00},
                {"ingredient_name": "Olive Oil", "quantity_required": 10.00},
                {"ingredient_name": "Vinegar", "quantity_required": 10.00},
                {"ingredient_name": "Garlic", "quantity_required": 5.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
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
