from django.core.management.base import BaseCommand
from menu.models import MenuItem, Ingredient, MenuItemIngredient

class Command(BaseCommand):
    help = "Populate the MenuItemIngredient table with required ingredients for each menu item"

    def handle(self, *args, **kwargs):
        menu_item_ingredients_data = {
            "Classic Cheeseburger": [
                {"ingredient_name": "Beef Patty", "quantity_required": 200.00},
                {"ingredient_name": "Cheddar Cheese", "quantity_required": 50.00},
                {"ingredient_name": "Lettuce", "quantity_required": 30.00},
                {"ingredient_name": "Tomato", "quantity_required": 20.00},
                {"ingredient_name": "Onions", "quantity_required": 15.00},
                {"ingredient_name": "Pickles", "quantity_required": 10.00},
                {"ingredient_name": "Burger Bun", "quantity_required": 1},
                {"ingredient_name": "Ketchup", "quantity_required": 10.00},
                {"ingredient_name": "Mustard", "quantity_required": 5.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00}
            ],
            "Bacon Burger": [
                {"ingredient_name": "Beef Patty", "quantity_required": 200.00},
                {"ingredient_name": "Bacon", "quantity_required": 50.00},
                {"ingredient_name": "Cheddar Cheese", "quantity_required": 50.00},
                {"ingredient_name": "Lettuce", "quantity_required": 30.00},
                {"ingredient_name": "Tomato", "quantity_required": 20.00},
                {"ingredient_name": "Burger Bun", "quantity_required": 1},
                {"ingredient_name": "Mayonnaise", "quantity_required": 10.00},
                {"ingredient_name": "Ketchup", "quantity_required": 10.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00}
            ],
            "BBQ Burger": [
                {"ingredient_name": "Beef Patty", "quantity_required": 200.00},
                {"ingredient_name": "Cheddar Cheese", "quantity_required": 50.00},
                {"ingredient_name": "BBQ Sauce", "quantity_required": 20.00},
                {"ingredient_name": "Onions", "quantity_required": 15.00},
                {"ingredient_name": "Pickles", "quantity_required": 10.00},
                {"ingredient_name": "Lettuce", "quantity_required": 30.00},
                {"ingredient_name": "Burger Bun", "quantity_required": 1},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00}
            ],
            "Mushroom Swiss Burger": [
                {"ingredient_name": "Beef Patty", "quantity_required": 200.00},
                {"ingredient_name": "Swiss Cheese", "quantity_required": 50.00},
                {"ingredient_name": "Mushrooms", "quantity_required": 50.00},
                {"ingredient_name": "Onions", "quantity_required": 15.00},
                {"ingredient_name": "Burger Bun", "quantity_required": 1},
                {"ingredient_name": "Garlic", "quantity_required": 5.00},
                {"ingredient_name": "Butter", "quantity_required": 10.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00}
            ],
            "Veggie Burger": [
                {"ingredient_name": "Veggie Patty", "quantity_required": 200.00},
                {"ingredient_name": "Lettuce", "quantity_required": 30.00},
                {"ingredient_name": "Tomato", "quantity_required": 20.00},
                {"ingredient_name": "Onions", "quantity_required": 15.00},
                {"ingredient_name": "Pickles", "quantity_required": 10.00},
                {"ingredient_name": "Avocado", "quantity_required": 50.00},
                {"ingredient_name": "Burger Bun", "quantity_required": 1},
                {"ingredient_name": "Mayonnaise", "quantity_required": 10.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00}
            ],
            "Avocado Burger": [
                {"ingredient_name": "Beef Patty", "quantity_required": 200.00},
                {"ingredient_name": "Cheddar Cheese", "quantity_required": 50.00},
                {"ingredient_name": "Avocado", "quantity_required": 50.00},
                {"ingredient_name": "Lettuce", "quantity_required": 30.00},
                {"ingredient_name": "Tomato", "quantity_required": 20.00},
                {"ingredient_name": "Burger Bun", "quantity_required": 1},
                {"ingredient_name": "Mayonnaise", "quantity_required": 10.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00}
            ],
            "Spicy Jalapeño Burger": [
                {"ingredient_name": "Beef Patty", "quantity_required": 200.00},
                {"ingredient_name": "Pepper Jack Cheese", "quantity_required": 50.00},
                {"ingredient_name": "Jalapeños", "quantity_required": 20.00},
                {"ingredient_name": "Lettuce", "quantity_required": 30.00},
                {"ingredient_name": "Onions", "quantity_required": 15.00},
                {"ingredient_name": "Burger Bun", "quantity_required": 1},
                {"ingredient_name": "Sriracha Sauce", "quantity_required": 10.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00}
            ],
            "Double Cheeseburger": [
                {"ingredient_name": "Beef Patty", "quantity_required": 400.00},  # Two patties
                {"ingredient_name": "Cheddar Cheese", "quantity_required": 100.00},  # Double cheese
                {"ingredient_name": "Lettuce", "quantity_required": 30.00},
                {"ingredient_name": "Tomato", "quantity_required": 20.00},
                {"ingredient_name": "Onions", "quantity_required": 15.00},
                {"ingredient_name": "Pickles", "quantity_required": 10.00},
                {"ingredient_name": "Burger Bun", "quantity_required": 1},
                {"ingredient_name": "Ketchup", "quantity_required": 10.00},
                {"ingredient_name": "Mustard", "quantity_required": 5.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00}
            ],
            "Teriyaki Burger": [
                {"ingredient_name": "Beef Patty", "quantity_required": 200.00},
                {"ingredient_name": "Swiss Cheese", "quantity_required": 50.00},
                {"ingredient_name": "Pineapple Slice", "quantity_required": 30.00},
                {"ingredient_name": "Teriyaki Sauce", "quantity_required": 20.00},
                {"ingredient_name": "Lettuce", "quantity_required": 30.00},
                {"ingredient_name": "Onions", "quantity_required": 15.00},
                {"ingredient_name": "Burger Bun", "quantity_required": 1},
                {"ingredient_name": "Salt", "quantity_required": 2.00},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00}
            ],
            "Black & Blue Burger": [
                {"ingredient_name": "Beef Patty", "quantity_required": 200.00},
                {"ingredient_name": "Blue Cheese", "quantity_required": 50.00},
                {"ingredient_name": "Lettuce", "quantity_required": 30.00},
                {"ingredient_name": "Tomato", "quantity_required": 20.00},
                {"ingredient_name": "Onions", "quantity_required": 15.00},
                {"ingredient_name": "Burger Bun", "quantity_required": 1},
                {"ingredient_name": "Black Pepper", "quantity_required": 5.00},
                {"ingredient_name": "Salt", "quantity_required": 2.00}
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
