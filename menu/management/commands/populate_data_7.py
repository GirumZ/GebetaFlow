from django.core.management.base import BaseCommand
from menu.models import MenuItem, Ingredient, MenuItemIngredient

class Command(BaseCommand):
    help = "Populate the MenuItemIngredient table with required ingredients for each menu item"

    def handle(self, *args, **kwargs):
        menu_item_ingredients_data = {
            "Mac & Cheese": [
                {"ingredient_name": "Macaroni Pasta", "quantity_required": 100.00},
                {"ingredient_name": "Cheddar Cheese", "quantity_required": 200.00},
                {"ingredient_name": "Milk", "quantity_required": 100.00},
                {"ingredient_name": "Butter", "quantity_required": 50.00},
                {"ingredient_name": "Flour", "quantity_required": 20.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
                {"ingredient_name": "Garlic Powder", "quantity_required": 5.00},
            ],
            "Chicken Fried Steak": [
                {"ingredient_name": "Beef Steak", "quantity_required": 200.00},
                {"ingredient_name": "Flour", "quantity_required": 50.00},
                {"ingredient_name": "Eggs", "quantity_required": 2},
                {"ingredient_name": "Milk", "quantity_required": 50.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
                {"ingredient_name": "Vegetable Oil", "quantity_required": 100.00},
                {"ingredient_name": "Gravy", "quantity_required": 100.00},
            ],
            "Shepherd's Pie": [
                {"ingredient_name": "Ground Beef", "quantity_required": 200.00},
                {"ingredient_name": "Potatoes", "quantity_required": 300.00},
                {"ingredient_name": "Carrots", "quantity_required": 100.00},
                {"ingredient_name": "Onions", "quantity_required": 100.00},
                {"ingredient_name": "Butter", "quantity_required": 50.00},
                {"ingredient_name": "Milk", "quantity_required": 50.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
            ],
            "Beef Stew": [
                {"ingredient_name": "Beef", "quantity_required": 300.00},
                {"ingredient_name": "Carrots", "quantity_required": 100.00},
                {"ingredient_name": "Potatoes", "quantity_required": 200.00},
                {"ingredient_name": "Onions", "quantity_required": 100.00},
                {"ingredient_name": "Beef Broth", "quantity_required": 500.00},
                {"ingredient_name": "Garlic", "quantity_required": 5.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
                {"ingredient_name": "Thyme", "quantity_required": 5.00},
            ],
            "Meatloaf": [
                {"ingredient_name": "Ground Beef", "quantity_required": 300.00},
                {"ingredient_name": "Breadcrumbs", "quantity_required": 100.00},
                {"ingredient_name": "Eggs", "quantity_required": 2},
                {"ingredient_name": "Onions", "quantity_required": 50.00},
                {"ingredient_name": "Ketchup", "quantity_required": 100.00},
                {"ingredient_name": "Milk", "quantity_required": 50.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
            ],
            "Baked Ziti": [
                {"ingredient_name": "Ziti Pasta", "quantity_required": 200.00},
                {"ingredient_name": "Marinara Sauce", "quantity_required": 200.00},
                {"ingredient_name": "Ricotta Cheese", "quantity_required": 100.00},
                {"ingredient_name": "Mozzarella Cheese", "quantity_required": 200.00},
                {"ingredient_name": "Parmesan Cheese", "quantity_required": 50.00},
                {"ingredient_name": "Garlic", "quantity_required": 5.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
                {"ingredient_name": "Italian Seasoning", "quantity_required": 5.00},
            ],
            "Chicken Pot Pie": [
                {"ingredient_name": "Chicken Breast", "quantity_required": 200.00},
                {"ingredient_name": "Pie Crust", "quantity_required": 1},
                {"ingredient_name": "Mixed Vegetables", "quantity_required": 200.00},
                {"ingredient_name": "Cream", "quantity_required": 100.00},
                {"ingredient_name": "Onions", "quantity_required": 50.00},
                {"ingredient_name": "Garlic", "quantity_required": 5.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
            ],
            "Mashed Potatoes & Gravy": [
                {"ingredient_name": "Potatoes", "quantity_required": 400.00},
                {"ingredient_name": "Butter", "quantity_required": 50.00},
                {"ingredient_name": "Milk", "quantity_required": 100.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
                {"ingredient_name": "Gravy", "quantity_required": 100.00},
            ],
            "Classic Chili": [
                {"ingredient_name": "Ground Beef", "quantity_required": 300.00},
                {"ingredient_name": "Tomato Sauce", "quantity_required": 200.00},
                {"ingredient_name": "Kidney Beans", "quantity_required": 200.00},
                {"ingredient_name": "Onions", "quantity_required": 100.00},
                {"ingredient_name": "Garlic", "quantity_required": 5.00},
                {"ingredient_name": "Chili Powder", "quantity_required": 10.00},
                {"ingredient_name": "Cumin", "quantity_required": 5.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
            ],
            "Eggplant Parmesan": [
                {"ingredient_name": "Eggplant", "quantity_required": 200.00},
                {"ingredient_name": "Marinara Sauce", "quantity_required": 200.00},
                {"ingredient_name": "Mozzarella Cheese", "quantity_required": 200.00},
                {"ingredient_name": "Parmesan Cheese", "quantity_required": 50.00},
                {"ingredient_name": "Breadcrumbs", "quantity_required": 100.00},
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
