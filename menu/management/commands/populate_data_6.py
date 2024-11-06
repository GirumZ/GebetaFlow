from django.core.management.base import BaseCommand
from menu.models import MenuItem, Ingredient, MenuItemIngredient

class Command(BaseCommand):
    help = "Populate the MenuItemIngredient table with required ingredients for each menu item"

    def handle(self, *args, **kwargs):
        menu_item_ingredients_data = {
            "Vegan Buddha Bowl": [
                {"ingredient_name": "Quinoa", "quantity_required": 100.00},
                {"ingredient_name": "Chickpeas", "quantity_required": 100.00},
                {"ingredient_name": "Spinach", "quantity_required": 50.00},
                {"ingredient_name": "Carrots", "quantity_required": 50.00},
                {"ingredient_name": "Cucumber", "quantity_required": 30.00},
                {"ingredient_name": "Avocado", "quantity_required": 50.00},
                {"ingredient_name": "Tahini", "quantity_required": 20.00},
                {"ingredient_name": "Olive Oil", "quantity_required": 10.00},
                {"ingredient_name": "Lemon Juice", "quantity_required": 10.00},
                {"ingredient_name": "Cilantro", "quantity_required": 5.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
            ],
            "Vegetable Stir-Fry": [
                {"ingredient_name": "Mixed Vegetables", "quantity_required": 200.00},
                {"ingredient_name": "Tofu", "quantity_required": 100.00},
                {"ingredient_name": "Soy Sauce", "quantity_required": 20.00},
                {"ingredient_name": "Ginger", "quantity_required": 5.00},
                {"ingredient_name": "Garlic", "quantity_required": 5.00},
                {"ingredient_name": "Sesame Oil", "quantity_required": 10.00},
                {"ingredient_name": "Cilantro", "quantity_required": 5.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
            ],
            "Mushroom Risotto": [
                {"ingredient_name": "Arborio Rice", "quantity_required": 100.00},
                {"ingredient_name": "Mushrooms", "quantity_required": 100.00},
                {"ingredient_name": "Olive Oil", "quantity_required": 10.00},
                {"ingredient_name": "Garlic", "quantity_required": 5.00},
                {"ingredient_name": "Onions", "quantity_required": 30.00},
                {"ingredient_name": "Vegetable Broth", "quantity_required": 100.00},
                {"ingredient_name": "Parmesan Cheese", "quantity_required": 30.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
            ],
            "Vegan Burrito": [
                {"ingredient_name": "Flour Tortillas", "quantity_required": 1},
                {"ingredient_name": "Rice", "quantity_required": 100.00},
                {"ingredient_name": "Black Beans", "quantity_required": 100.00},
                {"ingredient_name": "Guacamole", "quantity_required": 50.00},
                {"ingredient_name": "Salsa", "quantity_required": 50.00},
                {"ingredient_name": "Lettuce", "quantity_required": 50.00},
                {"ingredient_name": "Cilantro", "quantity_required": 5.00},
                {"ingredient_name": "Lemon Juice", "quantity_required": 10.00},
                {"ingredient_name": "Olive Oil", "quantity_required": 10.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
            ],
            "Falafel Plate": [
                {"ingredient_name": "Falafel", "quantity_required": 200.00},
                {"ingredient_name": "Hummus", "quantity_required": 100.00},
                {"ingredient_name": "Tabbouleh", "quantity_required": 100.00},
                {"ingredient_name": "Olive Oil", "quantity_required": 10.00},
                {"ingredient_name": "Lemon Juice", "quantity_required": 10.00},
                {"ingredient_name": "Garlic", "quantity_required": 5.00},
                {"ingredient_name": "Cilantro", "quantity_required": 5.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
            ],
            "Stuffed Bell Peppers": [
                {"ingredient_name": "Bell Peppers", "quantity_required": 4},
                {"ingredient_name": "Rice", "quantity_required": 100.00},
                {"ingredient_name": "Black Beans", "quantity_required": 100.00},
                {"ingredient_name": "Corn", "quantity_required": 50.00},
                {"ingredient_name": "Onions", "quantity_required": 30.00},
                {"ingredient_name": "Olive Oil", "quantity_required": 10.00},
                {"ingredient_name": "Garlic", "quantity_required": 5.00},
                {"ingredient_name": "Cilantro", "quantity_required": 5.00},
                {"ingredient_name": "Lemon Juice", "quantity_required": 10.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
            ],
            "Eggplant Parmesan": [
                {"ingredient_name": "Eggplant", "quantity_required": 200.00},
                {"ingredient_name": "Breadcrumbs", "quantity_required": 50.00},
                {"ingredient_name": "Ricotta Cheese", "quantity_required": 100.00},
                {"ingredient_name": "Mozzarella Cheese", "quantity_required": 100.00},
                {"ingredient_name": "Parmesan Cheese", "quantity_required": 30.00},
                {"ingredient_name": "Tomato Sauce", "quantity_required": 100.00},
                {"ingredient_name": "Olive Oil", "quantity_required": 10.00},
                {"ingredient_name": "Garlic", "quantity_required": 5.00},
                {"ingredient_name": "Basil", "quantity_required": 5.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
            ],
            "Chickpea Curry": [
                {"ingredient_name": "Chickpeas", "quantity_required": 200.00},
                {"ingredient_name": "Coconut Milk", "quantity_required": 100.00},
                {"ingredient_name": "Curry Powder", "quantity_required": 10.00},
                {"ingredient_name": "Onions", "quantity_required": 30.00},
                {"ingredient_name": "Garlic", "quantity_required": 5.00},
                {"ingredient_name": "Ginger", "quantity_required": 5.00},
                {"ingredient_name": "Tomatoes", "quantity_required": 50.00},
                {"ingredient_name": "Olive Oil", "quantity_required": 10.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
            ],
            "Lentil Shepherd’s Pie": [
                {"ingredient_name": "Lentils", "quantity_required": 200.00},
                {"ingredient_name": "Potatoes", "quantity_required": 200.00},
                {"ingredient_name": "Carrots", "quantity_required": 50.00},
                {"ingredient_name": "Onions", "quantity_required": 30.00},
                {"ingredient_name": "Garlic", "quantity_required": 5.00},
                {"ingredient_name": "Olive Oil", "quantity_required": 10.00},
                {"ingredient_name": "Tomato Sauce", "quantity_required": 100.00},
                {"ingredient_name": "Thyme", "quantity_required": 5.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
            ],
            "Vegan Mac & Cheese": [
                {"ingredient_name": "Penne Pasta", "quantity_required": 100.00},
                {"ingredient_name": "Dairy-Free Cheese", "quantity_required": 100.00},
                {"ingredient_name": "Coconut Milk", "quantity_required": 50.00},
                {"ingredient_name": "Nutritional Yeast", "quantity_required": 10.00},
                {"ingredient_name": "Garlic", "quantity_required": 5.00},
                {"ingredient_name": "Olive Oil", "quantity_required": 10.00},
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
