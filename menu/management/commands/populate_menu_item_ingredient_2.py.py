from django.core.management.base import BaseCommand
from menu.models import MenuItem, Ingredient, MenuItemIngredient

class Command(BaseCommand):
    help = "Populate the MenuItemIngredient table with required ingredients for each menu item"

    def handle(self, *args, **kwargs):
        menu_item_ingredients_data = {
            "Grilled Chicken Breast": [
                {"ingredient_name": "Chicken-Breast", "quantity_required": 200},
                {"ingredient_name": "Olive-Oil-Light", "quantity_required": 10},
                {"ingredient_name": "Garlic", "quantity_required": 5},
                {"ingredient_name": "Lemon-Juice", "quantity_required": 10},
                {"ingredient_name": "Mixed-Herbs", "quantity_required": 5},
                {"ingredient_name": "Black-Pepper", "quantity_required": 5},
                {"ingredient_name": "Salt", "quantity_required": 2}
            ],
            "Chicken Parmesan": [
                {"ingredient_name": "Chicken-Breast", "quantity_required": 200},
                {"ingredient_name": "Parmesan-Cheese", "quantity_required": 30},
                {"ingredient_name": "Mozzarella-Cheese", "quantity_required": 100},
                {"ingredient_name": "Marinara-Sauce", "quantity_required": 100},
                {"ingredient_name": "Breadcrumbs", "quantity_required": 50},
                {"ingredient_name": "Eggs", "quantity_required": 2},
                {"ingredient_name": "Olive-Oil-Light", "quantity_required": 10},
                {"ingredient_name": "Garlic", "quantity_required": 5},
                {"ingredient_name": "Salt", "quantity_required": 2},
                {"ingredient_name": "Black-Pepper", "quantity_required": 5}
            ],
            "Honey Garlic Chicken": [
                {"ingredient_name": "Chicken-Breast", "quantity_required": 200},
                {"ingredient_name": "Honey", "quantity_required": 30},
                {"ingredient_name": "Garlic", "quantity_required": 5},
                {"ingredient_name": "Soy-Sauce", "quantity_required": 20},
                {"ingredient_name": "Olive-Oil-Light", "quantity_required": 10},
                {"ingredient_name": "Black-Pepper", "quantity_required": 5},
                {"ingredient_name": "Salt", "quantity_required": 2}
            ],
            "Lemon Herb Chicken": [
                {"ingredient_name": "Chicken-Breast", "quantity_required": 200},
                {"ingredient_name": "Lemon-Juice", "quantity_required": 10},
                {"ingredient_name": "Mixed-Herbs", "quantity_required": 5},
                {"ingredient_name": "Garlic", "quantity_required": 5},
                {"ingredient_name": "Olive-Oil-Light", "quantity_required": 10},
                {"ingredient_name": "Black-Pepper", "quantity_required": 5},
                {"ingredient_name": "Salt", "quantity_required": 2}
            ],
            "Chicken Marsala": [
                {"ingredient_name": "Chicken-Breast", "quantity_required": 200},
                {"ingredient_name": "Wine-White", "quantity_required": 50},
                {"ingredient_name": "Mushrooms", "quantity_required": 50},
                {"ingredient_name": "Olive-Oil-Light", "quantity_required": 10},
                {"ingredient_name": "Garlic", "quantity_required": 5},
                {"ingredient_name": "Butter-Salted", "quantity_required": 20},
                {"ingredient_name": "Black-Pepper", "quantity_required": 5},
                {"ingredient_name": "Salt", "quantity_required": 2}
            ],
            "BBQ Chicken Thighs": [
                {"ingredient_name": "Chicken-Thighs", "quantity_required": 200},
                {"ingredient_name": "BBQ-Sauce", "quantity_required": 50},
                {"ingredient_name": "Olive-Oil-Light", "quantity_required": 10},
                {"ingredient_name": "Garlic", "quantity_required": 5},
                {"ingredient_name": "Black-Pepper", "quantity_required": 5},
                {"ingredient_name": "Salt", "quantity_required": 2}
            ],
            "Butter Chicken": [
                {"ingredient_name": "Chicken-Breast", "quantity_required": 200},
                {"ingredient_name": "Tomato-Sauce", "quantity_required": 100},
                {"ingredient_name": "Heavy-Cream", "quantity_required": 50},
                {"ingredient_name": "Butter-Salted", "quantity_required": 50},
                {"ingredient_name": "Garlic", "quantity_required": 5},
                {"ingredient_name": "Ginger", "quantity_required": 5},
                {"ingredient_name": "Black-Pepper", "quantity_required": 5},
                {"ingredient_name": "Salt", "quantity_required": 2}
            ],
            "Cajun Chicken": [
                {"ingredient_name": "Chicken-Breast", "quantity_required": 200},
                {"ingredient_name": "Olive-Oil-Light", "quantity_required": 10},
                {"ingredient_name": "Garlic", "quantity_required": 5},
                {"ingredient_name": "Black-Pepper", "quantity_required": 5},
                {"ingredient_name": "Salt", "quantity_required": 2}
            ],
            "Chicken Tikka Masala": [
                {"ingredient_name": "Chicken-Breast", "quantity_required": 200},
                {"ingredient_name": "Tomato-Sauce", "quantity_required": 100},
                {"ingredient_name": "Heavy-Cream", "quantity_required": 50},
                {"ingredient_name": "Curry-Powder", "quantity_required": 5},
                {"ingredient_name": "Ginger", "quantity_required": 5},
                {"ingredient_name": "Garlic", "quantity_required": 5},
                {"ingredient_name": "Onions", "quantity_required": 30},
                {"ingredient_name": "Black-Pepper", "quantity_required": 5},
                {"ingredient_name": "Salt", "quantity_required": 2}
            ],
            "Stuffed Chicken Breast": [
                {"ingredient_name": "Chicken-Breast", "quantity_required": 200},
                {"ingredient_name": "Spinach", "quantity_required": 50},
                {"ingredient_name": "Ricotta-Cheese", "quantity_required": 100},
                {"ingredient_name": "Parmesan-Cheese", "quantity_required": 30},
                {"ingredient_name": "Olive-Oil-Light", "quantity_required": 10},
                {"ingredient_name": "Garlic", "quantity_required": 5},
                {"ingredient_name": "Black-Pepper", "quantity_required": 5},
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
