from django.core.management.base import BaseCommand
from menu.models import MenuItem, Ingredient, MenuItemIngredient

class Command(BaseCommand):
    help = "Populate the MenuItemIngredient table with required ingredients for each menu item"

    def handle(self, *args, **kwargs):
        menu_item_ingredients_data = {
            "Margherita Pizza": [
                {"ingredient_name": "Pizza Dough", "quantity_required": 1},
                {"ingredient_name": "Tomato Sauce", "quantity_required": 100.00},
                {"ingredient_name": "Mozzarella Cheese", "quantity_required": 200.00},
                {"ingredient_name": "Basil", "quantity_required": 10.00},
                {"ingredient_name": "Olive Oil", "quantity_required": 10.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
            ],
            "Pepperoni Pizza": [
                {"ingredient_name": "Pizza Dough", "quantity_required": 1},
                {"ingredient_name": "Tomato Sauce", "quantity_required": 100.00},
                {"ingredient_name": "Mozzarella Cheese", "quantity_required": 200.00},
                {"ingredient_name": "Pepperoni", "quantity_required": 100.00},
                {"ingredient_name": "Olive Oil", "quantity_required": 10.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
            ],
            "BBQ Chicken Pizza": [
                {"ingredient_name": "Pizza Dough", "quantity_required": 1},
                {"ingredient_name": "BBQ Sauce", "quantity_required": 100.00},
                {"ingredient_name": "Chicken Breast", "quantity_required": 200.00},
                {"ingredient_name": "Red Onions", "quantity_required": 50.00},
                {"ingredient_name": "Mozzarella Cheese", "quantity_required": 200.00},
                {"ingredient_name": "Olive Oil", "quantity_required": 10.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
            ],
            "Four Cheese Pizza": [
                {"ingredient_name": "Pizza Dough", "quantity_required": 1},
                {"ingredient_name": "Tomato Sauce", "quantity_required": 100.00},
                {"ingredient_name": "Mozzarella Cheese", "quantity_required": 100.00},
                {"ingredient_name": "Parmesan Cheese", "quantity_required": 50.00},
                {"ingredient_name": "Gorgonzola Cheese", "quantity_required": 50.00},
                {"ingredient_name": "Cheddar Cheese", "quantity_required": 50.00},
                {"ingredient_name": "Olive Oil", "quantity_required": 10.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
            ],
            "Hawaiian Pizza": [
                {"ingredient_name": "Pizza Dough", "quantity_required": 1},
                {"ingredient_name": "Tomato Sauce", "quantity_required": 100.00},
                {"ingredient_name": "Mozzarella Cheese", "quantity_required": 200.00},
                {"ingredient_name": "Ham", "quantity_required": 100.00},
                {"ingredient_name": "Pineapple", "quantity_required": 100.00},
                {"ingredient_name": "Olive Oil", "quantity_required": 10.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
            ],
            "Veggie Pizza": [
                {"ingredient_name": "Pizza Dough", "quantity_required": 1},
                {"ingredient_name": "Tomato Sauce", "quantity_required": 100.00},
                {"ingredient_name": "Mozzarella Cheese", "quantity_required": 200.00},
                {"ingredient_name": "Bell Peppers", "quantity_required": 50.00},
                {"ingredient_name": "Onions", "quantity_required": 50.00},
                {"ingredient_name": "Olives", "quantity_required": 30.00},
                {"ingredient_name": "Olive Oil", "quantity_required": 10.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
            ],
            "Meat Lovers Pizza": [
                {"ingredient_name": "Pizza Dough", "quantity_required": 1},
                {"ingredient_name": "Tomato Sauce", "quantity_required": 100.00},
                {"ingredient_name": "Mozzarella Cheese", "quantity_required": 200.00},
                {"ingredient_name": "Pepperoni", "quantity_required": 100.00},
                {"ingredient_name": "Sausage", "quantity_required": 100.00},
                {"ingredient_name": "Ham", "quantity_required": 100.00},
                {"ingredient_name": "Olive Oil", "quantity_required": 10.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
            ],
            "White Pizza": [
                {"ingredient_name": "Pizza Dough", "quantity_required": 1},
                {"ingredient_name": "Ricotta Cheese", "quantity_required": 100.00},
                {"ingredient_name": "Mozzarella Cheese", "quantity_required": 200.00},
                {"ingredient_name": "Garlic", "quantity_required": 5.00},
                {"ingredient_name": "Olive Oil", "quantity_required": 10.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
            ],
            "Mushroom Pizza": [
                {"ingredient_name": "Pizza Dough", "quantity_required": 1},
                {"ingredient_name": "Tomato Sauce", "quantity_required": 100.00},
                {"ingredient_name": "Mozzarella Cheese", "quantity_required": 200.00},
                {"ingredient_name": "Fresh Mushrooms", "quantity_required": 100.00},
                {"ingredient_name": "Olive Oil", "quantity_required": 10.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
            ],
            "Buffalo Chicken Pizza": [
                {"ingredient_name": "Pizza Dough", "quantity_required": 1},
                {"ingredient_name": "Buffalo Sauce", "quantity_required": 100.00},
                {"ingredient_name": "Chicken Breast", "quantity_required": 200.00},
                {"ingredient_name": "Mozzarella Cheese", "quantity_required": 200.00},
                {"ingredient_name": "Olive Oil", "quantity_required": 10.00},
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
