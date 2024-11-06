from django.core.management.base import BaseCommand
from menu.models import MenuItem, Ingredient, MenuItemIngredient

class Command(BaseCommand):
    help = "Populate the MenuItemIngredient table with required ingredients for each menu item"

    def handle(self, *args, **kwargs):
        menu_item_ingredients_data = {
            "Duck Confit": [
                {"ingredient_name": "Duck Legs", "quantity_required": 200.00},
                {"ingredient_name": "Duck Fat", "quantity_required": 100.00},
                {"ingredient_name": "Garlic", "quantity_required": 5.00},
                {"ingredient_name": "Thyme", "quantity_required": 5.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
            ],
            "Rack of Lamb": [
                {"ingredient_name": "Lamb", "quantity_required": 300.00},
                {"ingredient_name": "Garlic", "quantity_required": 5.00},
                {"ingredient_name": "Rosemary", "quantity_required": 5.00},
                {"ingredient_name": "Olive Oil", "quantity_required": 10.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
            ],
            "Sea Bass with Lemon Caper Sauce": [
                {"ingredient_name": "Sea Bass Fillets", "quantity_required": 200.00},
                {"ingredient_name": "Capers", "quantity_required": 50.00},
                {"ingredient_name": "Lemon Juice", "quantity_required": 20.00},
                {"ingredient_name": "Butter", "quantity_required": 50.00},
                {"ingredient_name": "Garlic", "quantity_required": 5.00},
                {"ingredient_name": "Olive Oil", "quantity_required": 10.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
            ],
            "Wagyu Steak": [
                {"ingredient_name": "Wagyu Beef", "quantity_required": 300.00},
                {"ingredient_name": "Olive Oil", "quantity_required": 10.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
            ],
            "Truffle Risotto": [
                {"ingredient_name": "Arborio Rice", "quantity_required": 200.00},
                {"ingredient_name": "Truffle Oil", "quantity_required": 20.00},
                {"ingredient_name": "Chicken Stock", "quantity_required": 500.00},
                {"ingredient_name": "Parmesan Cheese", "quantity_required": 50.00},
                {"ingredient_name": "Butter", "quantity_required": 50.00},
                {"ingredient_name": "Shallots", "quantity_required": 50.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
            ],
            "Foie Gras": [
                {"ingredient_name": "Foie Gras", "quantity_required": 100.00},
                {"ingredient_name": "Brioche", "quantity_required": 50.00},
                {"ingredient_name": "Fig Jam", "quantity_required": 30.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
            ],
            "Lobster Thermidor": [
                {"ingredient_name": "Lobster Meat", "quantity_required": 200.00},
                {"ingredient_name": "Heavy Cream", "quantity_required": 100.00},
                {"ingredient_name": "Parmesan Cheese", "quantity_required": 50.00},
                {"ingredient_name": "Mustard", "quantity_required": 20.00},
                {"ingredient_name": "Shallots", "quantity_required": 50.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
                {"ingredient_name": "Paprika", "quantity_required": 5.00},
            ],
            "Short Rib Ravioli": [
                {"ingredient_name": "Ravioli", "quantity_required": 300.00},
                {"ingredient_name": "Short Rib Filling", "quantity_required": 200.00},
                {"ingredient_name": "Tomato Sauce", "quantity_required": 100.00},
                {"ingredient_name": "Parmesan Cheese", "quantity_required": 50.00},
                {"ingredient_name": "Olive Oil", "quantity_required": 10.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
            ],
            "Osso Buco": [
                {"ingredient_name": "Veal Shanks", "quantity_required": 300.00},
                {"ingredient_name": "White Wine", "quantity_required": 100.00},
                {"ingredient_name": "Chicken Stock", "quantity_required": 500.00},
                {"ingredient_name": "Onions", "quantity_required": 50.00},
                {"ingredient_name": "Carrots", "quantity_required": 50.00},
                {"ingredient_name": "Celery", "quantity_required": 50.00},
                {"ingredient_name": "Garlic", "quantity_required": 5.00},
                {"ingredient_name": "Thyme", "quantity_required": 5.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
            ],
            "Beef Wellington": [
                {"ingredient_name": "Beef Tenderloin", "quantity_required": 300.00},
                {"ingredient_name": "Puff Pastry", "quantity_required": 200.00},
                {"ingredient_name": "Mushrooms", "quantity_required": 100.00},
                {"ingredient_name": "Prosciutto", "quantity_required": 100.00},
                {"ingredient_name": "Eggs", "quantity_required": 10.00},
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
