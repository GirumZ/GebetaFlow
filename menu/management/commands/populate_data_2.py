from django.core.management.base import BaseCommand
from menu.models import MenuItem, Ingredient, MenuItemIngredient

class Command(BaseCommand):
    help = "Populate the MenuItemIngredient table with required ingredients for each menu item"

    def handle(self, *args, **kwargs):
        menu_item_ingredients_data = {
            "Spaghetti Carbonara": [
                {"ingredient_name": "Spaghetti", "quantity_required": 100},
                {"ingredient_name": "Pancetta", "quantity_required": 50},
                {"ingredient_name": "Eggs", "quantity_required": 2},
                {"ingredient_name": "Parmesan Cheese", "quantity_required": 30},
                {"ingredient_name": "Pecorino Romano Cheese", "quantity_required": 30},
                {"ingredient_name": "Garlic", "quantity_required": 5},
                {"ingredient_name": "Black Pepper", "quantity_required": 5},
                {"ingredient_name": "Salt", "quantity_required": 2},
                {"ingredient_name": "Olive Oil", "quantity_required": 10}
            ],
            "Fettuccine Alfredo": [
                {"ingredient_name": "Fettuccine", "quantity_required": 100},
                {"ingredient_name": "Heavy Cream", "quantity_required": 100},
                {"ingredient_name": "Butter", "quantity_required": 50},
                {"ingredient_name": "Parmesan Cheese", "quantity_required": 30},
                {"ingredient_name": "Pecorino Romano Cheese", "quantity_required": 20},
                {"ingredient_name": "Garlic", "quantity_required": 5},
                {"ingredient_name": "Black Pepper", "quantity_required": 5},
                {"ingredient_name": "Salt", "quantity_required": 2},
                {"ingredient_name": "Olive Oil", "quantity_required": 10}
            ],
            "Penne Arrabbiata": [
                {"ingredient_name": "Penne pasta", "quantity_required": 100},
                {"ingredient_name": "Tomato Sauce", "quantity_required": 150},
                {"ingredient_name": "Garlic", "quantity_required": 5},
                {"ingredient_name": "Onions", "quantity_required": 30},
                {"ingredient_name": "Red Chili Flakes", "quantity_required": 2},
                {"ingredient_name": "Parsley", "quantity_required": 5},
                {"ingredient_name": "Olive Oil", "quantity_required": 10},
                {"ingredient_name": "Salt", "quantity_required": 2},
                {"ingredient_name": "Black Pepper", "quantity_required": 5}
            ],
            "Lasagna": [
                {"ingredient_name": "Lasagna Noodles", "quantity_required": 200},
                {"ingredient_name": "Ground Beef", "quantity_required": 150},
                {"ingredient_name": "Ricotta Cheese", "quantity_required": 100},
                {"ingredient_name": "Mozzarella Cheese", "quantity_required": 100},
                {"ingredient_name": "Parmesan Cheese", "quantity_required": 30},
                {"ingredient_name": "Marinara Sauce", "quantity_required": 200},
                {"ingredient_name": "Onions", "quantity_required": 30},
                {"ingredient_name": "Garlic", "quantity_required": 5},
                {"ingredient_name": "Italian Seasoning", "quantity_required": 5},
                {"ingredient_name": "Salt", "quantity_required": 2},
                {"ingredient_name": "Black Pepper", "quantity_required": 5},
                {"ingredient_name": "Olive Oil", "quantity_required": 10}
            ],
            "Ravioli": [
                {"ingredient_name": "Ravioli", "quantity_required": 150},
                {"ingredient_name": "Marinara Sauce", "quantity_required": 100},
                {"ingredient_name": "Parmesan Cheese", "quantity_required": 30},
                {"ingredient_name": "Garlic", "quantity_required": 5},
                {"ingredient_name": "Olive Oil", "quantity_required": 10},
                {"ingredient_name": "Salt", "quantity_required": 2},
                {"ingredient_name": "Black Pepper", "quantity_required": 5}
            ],
            "Pasta Primavera": [
                {"ingredient_name": "spaghetti", "quantity_required": 100},
                {"ingredient_name": "Mixed Vegetables", "quantity_required": 150},
                {"ingredient_name": "Olive Oil", "quantity_required": 10},
                {"ingredient_name": "Garlic", "quantity_required": 5},
                {"ingredient_name": "Onions", "quantity_required": 30},
                {"ingredient_name": "Parmesan Cheese", "quantity_required": 30},
                {"ingredient_name": "Salt", "quantity_required": 2},
                {"ingredient_name": "Black Pepper", "quantity_required": 5},
                {"ingredient_name": "Basil", "quantity_required": 5},
                {"ingredient_name": "Parsley", "quantity_required": 5}
            ],
            "Linguine with Clams": [
                {"ingredient_name": "Linguine", "quantity_required": 100},
                {"ingredient_name": "Fresh Clams", "quantity_required": 150},
                {"ingredient_name": "White Wine", "quantity_required": 50},
                {"ingredient_name": "Garlic", "quantity_required": 5},
                {"ingredient_name": "Onions", "quantity_required": 30},
                {"ingredient_name": "Parsley", "quantity_required": 5},
                {"ingredient_name": "Olive Oil", "quantity_required": 10},
                {"ingredient_name": "Lemon Juice", "quantity_required": 10},
                {"ingredient_name": "Salt", "quantity_required": 2},
                {"ingredient_name": "Black Pepper", "quantity_required": 5}
            ],
            "Tortellini Alfredo": [
                {"ingredient_name": "Tortellini", "quantity_required": 150},
                {"ingredient_name": "Heavy Cream", "quantity_required": 100},
                {"ingredient_name": "Butter", "quantity_required": 50},
                {"ingredient_name": "Parmesan Cheese", "quantity_required": 30},
                {"ingredient_name": "Pecorino Romano Cheese", "quantity_required": 20},
                {"ingredient_name": "Garlic", "quantity_required": 5},
                {"ingredient_name": "Black Pepper", "quantity_required": 5},
                {"ingredient_name": "Salt", "quantity_required": 2},
                {"ingredient_name": "Olive Oil", "quantity_required": 10}
            ],
            "Pesto Penne": [
                {"ingredient_name": "Penne pasta", "quantity_required": 100},
                {"ingredient_name": "Basil Pesto", "quantity_required": 50},
                {"ingredient_name": "Parmesan Cheese", "quantity_required": 30},
                {"ingredient_name": "Pine Nuts", "quantity_required": 10},
                {"ingredient_name": "Olive Oil", "quantity_required": 10},
                {"ingredient_name": "Salt", "quantity_required": 2},
                {"ingredient_name": "Garlic", "quantity_required": 5},
                {"ingredient_name": "Black Pepper", "quantity_required": 5}
            ],
            "Gnocchi with Marinara": [
                {"ingredient_name": "Gnocchi", "quantity_required": 150},
                {"ingredient_name": "Marinara Sauce", "quantity_required": 100},
                {"ingredient_name": "Parmesan Cheese", "quantity_required": 30},
                {"ingredient_name": "Garlic", "quantity_required": 5},
                {"ingredient_name": "Olive Oil", "quantity_required": 10},
                {"ingredient_name": "Salt", "quantity_required": 2},
                {"ingredient_name": "Black Pepper", "quantity_required": 5},
                {"ingredient_name": "Basil", "quantity_required": 5}
            ]
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
