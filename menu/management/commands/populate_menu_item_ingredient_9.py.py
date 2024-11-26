from django.core.management.base import BaseCommand
from menu.models import MenuItem, Ingredient, MenuItemIngredient

class Command(BaseCommand):
    help = "Populate the MenuItemIngredient table with required ingredients for each menu item"

    def handle(self, *args, **kwargs):
        menu_item_ingredients_data = {
            "Beef Bulgogi": [
                {"ingredient_name": "Beef", "quantity_required": 200.00},
                {"ingredient_name": "Soy-Sauce", "quantity_required": 50.00},
                {"ingredient_name": "Sugar", "quantity_required": 10.00},
                {"ingredient_name": "Sesame-Oil", "quantity_required": 10.00},
                {"ingredient_name": "Garlic", "quantity_required": 5.00},
                {"ingredient_name": "Ginger", "quantity_required": 5.00},
                {"ingredient_name": "Onions", "quantity_required": 50.00},
                {"ingredient_name": "Black-Pepper", "quantity_required": 5.00},
                {"ingredient_name": "Rice-White", "quantity_required": 100.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
            ],
            "Chicken Tikka": [
                {"ingredient_name": "Chicken-Breast", "quantity_required": 200.00},
                {"ingredient_name": "Yogurt", "quantity_required": 100.00},
                {"ingredient_name": "Garlic", "quantity_required": 5.00},
                {"ingredient_name": "Ginger", "quantity_required": 5.00},
                {"ingredient_name": "Cumin", "quantity_required": 5.00},
                {"ingredient_name": "Coriander", "quantity_required": 5.00},
                {"ingredient_name": "Turmeric", "quantity_required": 5.00},
                {"ingredient_name": "Chili-Powder", "quantity_required": 5.00},
                {"ingredient_name": "Lemon-Juice", "quantity_required": 20.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
            ],
            "Pad Thai": [
                {"ingredient_name": "Noodles-Rice", "quantity_required": 200.00},
                {"ingredient_name": "Shrimp", "quantity_required": 200.00},
                {"ingredient_name": "Eggs", "quantity_required": 2},
                {"ingredient_name": "Tofu", "quantity_required": 100.00},
                {"ingredient_name": "Peanuts", "quantity_required": 50.00},
                {"ingredient_name": "Fish-Sauce", "quantity_required": 30.00},
                {"ingredient_name": "Chili-Powder", "quantity_required": 5.00},
                {"ingredient_name": "Olive-Oil-Light", "quantity_required": 10.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
            ],
            "Gyro Plate": [
                {"ingredient_name": "Beef", "quantity_required": 200.00},
                {"ingredient_name": "Bread", "quantity_required": 2},
                {"ingredient_name": "Tomatoes", "quantity_required": 100.00},
                {"ingredient_name": "Onions", "quantity_required": 50.00},
                {"ingredient_name": "Tzatziki-Sauce", "quantity_required": 50.00},
                {"ingredient_name": "Cucumber", "quantity_required": 50.00},
                {"ingredient_name": "Lettuce", "quantity_required": 30.00},
                {"ingredient_name": "Olive-Oil-Light", "quantity_required": 10.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
            ],
            "Beef Tacos": [
                {"ingredient_name": "Beef-Ground", "quantity_required": 200.00},
                {"ingredient_name": "Taco-Shells", "quantity_required": 4},
                {"ingredient_name": "Lettuce", "quantity_required": 50.00},
                {"ingredient_name": "Tomatoes", "quantity_required": 50.00},
                {"ingredient_name": "Cheddar-Cheese", "quantity_required": 50.00},
                {"ingredient_name": "Sour-Cream", "quantity_required": 30.00},
                {"ingredient_name": "Salsa-Hot", "quantity_required": 50.00},
                {"ingredient_name": "Olive-Oil-Light", "quantity_required": 10.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
            ],
            "Sushi Platter": [
                {"ingredient_name": "Sushi", "quantity_required": 200.00},
                {"ingredient_name": "Salmon", "quantity_required": 100.00},
                {"ingredient_name": "Cucumber", "quantity_required": 50.00},
                {"ingredient_name": "Avocado", "quantity_required": 50.00},
                {"ingredient_name": "Soy-Sauce", "quantity_required": 50.00},
                {"ingredient_name": "Wasabi", "quantity_required": 5.00},
                {"ingredient_name": "Vinegar", "quantity_required": 10.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
            ],
            "Chicken Shawarma": [
                {"ingredient_name": "Chicken-Thighs", "quantity_required": 200.00},
                {"ingredient_name": "Bread", "quantity_required": 2},
                {"ingredient_name": "Garlic", "quantity_required": 5.00},
                {"ingredient_name": "Yogurt", "quantity_required": 100.00},
                {"ingredient_name": "Lemon-Juice", "quantity_required": 20.00},
                {"ingredient_name": "Cumin", "quantity_required": 5.00},
                {"ingredient_name": "Paprika", "quantity_required": 5.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black-Pepper", "quantity_required": 5.00},
            ],
            "Falafel Wrap": [
                {"ingredient_name": "Falafel", "quantity_required": 200.00},
                {"ingredient_name": "Bread", "quantity_required": 2},
                {"ingredient_name": "Tahini-Sauce", "quantity_required": 50.00},
                {"ingredient_name": "Tomatoes", "quantity_required": 100.00},
                {"ingredient_name": "Lettuce", "quantity_required": 50.00},
                {"ingredient_name": "Cucumber", "quantity_required": 50.00},
                {"ingredient_name": "Olive-Oil-Light", "quantity_required": 10.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
            ],
            "Banh Mi": [
                {"ingredient_name": "Pork-Ground", "quantity_required": 200.00},
                {"ingredient_name": "Mixed-Vegetables", "quantity_required": 50.00},
                {"ingredient_name": "Cucumber", "quantity_required": 50.00},
                {"ingredient_name": "Cilantro", "quantity_required": 10.00},
                {"ingredient_name": "Mayonnaise", "quantity_required": 30.00},
                {"ingredient_name": "Sriracha-Sauce", "quantity_required": 20.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
            ],
            "Paella": [
                {"ingredient_name": "Rice-White", "quantity_required": 200.00},
                {"ingredient_name": "Chicken-Breast", "quantity_required": 200.00},
                {"ingredient_name": "Mussels", "quantity_required": 200.00},
                {"ingredient_name": "Bell-Peppers", "quantity_required": 50.00},
                {"ingredient_name": "Tomatoes", "quantity_required": 100.00},
                {"ingredient_name": "Garlic", "quantity_required": 5.00},
                {"ingredient_name": "Saffron", "quantity_required": 1.00},
                {"ingredient_name": "Olive-Oil-Light", "quantity_required": 20.00},
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
