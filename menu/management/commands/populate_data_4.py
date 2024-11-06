from django.core.management.base import BaseCommand
from menu.models import MenuItem, Ingredient, MenuItemIngredient

class Command(BaseCommand):
    help = "Populate the MenuItemIngredient table with required ingredients for each menu item"

    def handle(self, *args, **kwargs):
        menu_item_ingredients_data = {
            "Grilled Salmon": [
                {"ingredient_name": "Salmon", "quantity_required": 200},
                {"ingredient_name": "Olive Oil", "quantity_required": 10},
                {"ingredient_name": "Lemon Juice", "quantity_required": 10},
                {"ingredient_name": "Garlic", "quantity_required": 5},
                {"ingredient_name": "Parsley", "quantity_required": 5},
                {"ingredient_name": "Black Pepper", "quantity_required": 5},
                {"ingredient_name": "Salt", "quantity_required": 2}
            ],
            "Fish & Chips": [
                {"ingredient_name": "White Fish Fillets", "quantity_required": 200},
                {"ingredient_name": "Potatoes", "quantity_required": 150},
                {"ingredient_name": "Flour", "quantity_required": 50},
                {"ingredient_name": "Baking Powder", "quantity_required": 5},
                {"ingredient_name": "Eggs", "quantity_required": 2},
                {"ingredient_name": "Salt", "quantity_required": 2},
                {"ingredient_name": "Black Pepper", "quantity_required": 5},
                {"ingredient_name": "Vegetable Oil", "quantity_required": 100}
            ],
            "Shrimp Scampi": [
                {"ingredient_name": "Shrimp", "quantity_required": 200},
                {"ingredient_name": "Olive Oil", "quantity_required": 10},
                {"ingredient_name": "Garlic", "quantity_required": 5},
                {"ingredient_name": "Lemon Juice", "quantity_required": 10},
                {"ingredient_name": "Parsley", "quantity_required": 5},
                {"ingredient_name": "White Wine", "quantity_required": 50},
                {"ingredient_name": "Black Pepper", "quantity_required": 5},
                {"ingredient_name": "Salt", "quantity_required": 2}
            ],
            "Seafood Paella": [
                {"ingredient_name": "Shrimp", "quantity_required": 100},
                {"ingredient_name": "Clams", "quantity_required": 100},
                {"ingredient_name": "Mussels", "quantity_required": 100},
                {"ingredient_name": "Rice", "quantity_required": 100},
                {"ingredient_name": "Olive Oil", "quantity_required": 10},
                {"ingredient_name": "Garlic", "quantity_required": 5},
                {"ingredient_name": "Onions", "quantity_required": 30},
                {"ingredient_name": "Saffron", "quantity_required": 5},
                {"ingredient_name": "Lemon Juice", "quantity_required": 10},
                {"ingredient_name": "Black Pepper", "quantity_required": 5},
                {"ingredient_name": "Salt", "quantity_required": 2}
            ],
            "Crab Cakes": [
                {"ingredient_name": "Crab Meat", "quantity_required": 200},
                {"ingredient_name": "Breadcrumbs", "quantity_required": 50},
                {"ingredient_name": "Eggs", "quantity_required": 2},
                {"ingredient_name": "Mayonnaise", "quantity_required": 20},
                {"ingredient_name": "Mustard", "quantity_required": 10},
                {"ingredient_name": "Garlic", "quantity_required": 5},
                {"ingredient_name": "Lemon Juice", "quantity_required": 10},
                {"ingredient_name": "Black Pepper", "quantity_required": 5},
                {"ingredient_name": "Salt", "quantity_required": 2}
            ],
            "Lobster Tail": [
                {"ingredient_name": "Lobster Tail", "quantity_required": 200},
                {"ingredient_name": "Olive Oil", "quantity_required": 10},
                {"ingredient_name": "Garlic", "quantity_required": 5},
                {"ingredient_name": "Lemon Juice", "quantity_required": 10},
                {"ingredient_name": "Parsley", "quantity_required": 5},
                {"ingredient_name": "Black Pepper", "quantity_required": 5},
                {"ingredient_name": "Salt", "quantity_required": 2}
            ],
            "Clam Chowder": [
                {"ingredient_name": "Clams", "quantity_required": 100},
                {"ingredient_name": "Potatoes", "quantity_required": 100},
                {"ingredient_name": "Heavy Cream", "quantity_required": 50},
                {"ingredient_name": "Onions", "quantity_required": 30},
                {"ingredient_name": "Garlic", "quantity_required": 5},
                {"ingredient_name": "Celery", "quantity_required": 30},
                {"ingredient_name": "Thyme", "quantity_required": 5},
                {"ingredient_name": "Bay Leaves", "quantity_required": 2},
                {"ingredient_name": "Butter", "quantity_required": 20},
                {"ingredient_name": "Black Pepper", "quantity_required": 5},
                {"ingredient_name": "Salt", "quantity_required": 2}
            ],
            "Grilled Shrimp Skewers": [
                {"ingredient_name": "Shrimp", "quantity_required": 200},
                {"ingredient_name": "Olive Oil", "quantity_required": 10},
                {"ingredient_name": "Garlic", "quantity_required": 5},
                {"ingredient_name": "Lemon Juice", "quantity_required": 10},
                {"ingredient_name": "Parsley", "quantity_required": 5},
                {"ingredient_name": "Black Pepper", "quantity_required": 5},
                {"ingredient_name": "Salt", "quantity_required": 2}
            ],
            "Mussels in White Wine": [
                {"ingredient_name": "Mussels", "quantity_required": 200},
                {"ingredient_name": "White Wine", "quantity_required": 50},
                {"ingredient_name": "Garlic", "quantity_required": 5},
                {"ingredient_name": "Onions", "quantity_required": 30},
                {"ingredient_name": "Olive Oil", "quantity_required": 10},
                {"ingredient_name": "Lemon Juice", "quantity_required": 10},
                {"ingredient_name": "Parsley", "quantity_required": 5},
                {"ingredient_name": "Black Pepper", "quantity_required": 5},
                {"ingredient_name": "Salt", "quantity_required": 2}
            ],
            "Seafood Risotto": [
                {"ingredient_name": "Shrimp", "quantity_required": 100},
                {"ingredient_name": "Clams", "quantity_required": 100},
                {"ingredient_name": "Mussels", "quantity_required": 100},
                {"ingredient_name": "Arborio Rice", "quantity_required": 100},
                {"ingredient_name": "Olive Oil", "quantity_required": 10},
                {"ingredient_name": "Garlic", "quantity_required": 5},
                {"ingredient_name": "Onions", "quantity_required": 30},
                {"ingredient_name": "White Wine", "quantity_required": 50},
                {"ingredient_name": "Parmesan Cheese", "quantity_required": 30},
                {"ingredient_name": "Lemon Juice", "quantity_required": 10},
                {"ingredient_name": "Black Pepper", "quantity_required": 5},
                {"ingredient_name": "Salt", "quantity_required": 2}
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
