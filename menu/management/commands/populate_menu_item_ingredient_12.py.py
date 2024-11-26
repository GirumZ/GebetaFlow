from django.core.management.base import BaseCommand
from menu.models import MenuItem, Ingredient, MenuItemIngredient

class Command(BaseCommand):
    help = "Populate the MenuItemIngredient table with required ingredients for each menu item"

    def handle(self, *args, **kwargs):
        menu_item_ingredients_data = {
            "Caesar Salad": [
                {"ingredient_name": "Lettuce", "quantity_required": 50},
                {"ingredient_name": "Parmesan-Cheese", "quantity_required": 20},
                {"ingredient_name": "Olive-Oil-Light", "quantity_required": 10},
                {"ingredient_name": "Lemon-Juice", "quantity_required": 5},
                {"ingredient_name": "Garlic", "quantity_required": 2},
                {"ingredient_name": "Salt", "quantity_required": 1},
                {"ingredient_name": "Black-Pepper", "quantity_required": 1},
                {"ingredient_name": "Chicken-Breast", "quantity_required": 100},
            ],
            "Greek Salad": [
                {"ingredient_name": "Cucumber", "quantity_required": 40},
                {"ingredient_name": "Tomatoes", "quantity_required": 50},
                {"ingredient_name": "Onions", "quantity_required": 20},
                {"ingredient_name": "Feta-Cheese", "quantity_required": 30},
                {"ingredient_name": "Olives", "quantity_required": 15},
                {"ingredient_name": "Olive-Oil-Light", "quantity_required": 10},
                {"ingredient_name": "Oregano", "quantity_required": 1},
                {"ingredient_name": "Salt", "quantity_required": 1},
                {"ingredient_name": "Black-Pepper", "quantity_required": 1},
            ],
            "Caprese Salad": [
                {"ingredient_name": "Tomatoes", "quantity_required": 60},
                {"ingredient_name": "Mozzarella-Cheese", "quantity_required": 50},
                {"ingredient_name": "Basil", "quantity_required": 5},
                {"ingredient_name": "Olive-Oil-Light", "quantity_required": 10},
                {"ingredient_name": "Salt", "quantity_required": 1},
                {"ingredient_name": "Black-Pepper", "quantity_required": 1},
            ],
            "Garden Salad": [
                {"ingredient_name": "Lettuce", "quantity_required": 50},
                {"ingredient_name": "Cucumber", "quantity_required": 30},
                {"ingredient_name": "Tomatoes", "quantity_required": 40},
                {"ingredient_name": "Carrots", "quantity_required": 20},
                {"ingredient_name": "Bell-Peppers-Red", "quantity_required": 20},
                {"ingredient_name": "Olive-Oil-Light", "quantity_required": 10},
                {"ingredient_name": "Lemon-Juice", "quantity_required": 5},
                {"ingredient_name": "Salt", "quantity_required": 1},
                {"ingredient_name": "Black-Pepper", "quantity_required": 1},
            ],
            "Asian Slaw Salad": [
                {"ingredient_name": "Cabbage-Green", "quantity_required": 50},
                {"ingredient_name": "Carrots", "quantity_required": 20},
                {"ingredient_name": "Cabbage-Red", "quantity_required": 20},
                {"ingredient_name": "Onions", "quantity_required": 10},
                {"ingredient_name": "Sesame-Seeds", "quantity_required": 5},
                {"ingredient_name": "Sesame-Oil", "quantity_required": 5},
                {"ingredient_name": "Salt", "quantity_required": 1},
                {"ingredient_name": "Black-Pepper", "quantity_required": 1},
            ],
            "Mozzarella Sticks": [
                {"ingredient_name": "Mozzarella-Cheese", "quantity_required": 50},
                {"ingredient_name": "Breadcrumbs", "quantity_required": 20},
                {"ingredient_name": "All-Purpose-Flour", "quantity_required": 15},
                {"ingredient_name": "Eggs", "quantity_required": 1},
                {"ingredient_name": "Salt", "quantity_required": 1},
                {"ingredient_name": "Black-Pepper", "quantity_required": 1},
                {"ingredient_name": "Vegetable-Oil", "quantity_required": 100},
            ],
            "Stuffed Jalapeños": [
                {"ingredient_name": "Jalapenos", "quantity_required": 200},
                {"ingredient_name": "Cream-Cheese", "quantity_required": 30},
                {"ingredient_name": "Cheddar-Cheese", "quantity_required": 20},
                {"ingredient_name": "Breadcrumbs", "quantity_required": 10},
                {"ingredient_name": "Salt", "quantity_required": 1},
                {"ingredient_name": "Black-Pepper", "quantity_required": 1},
                {"ingredient_name": "Vegetable-Oil", "quantity_required": 100},
            ],
            "Chicken Tenders": [
                {"ingredient_name": "Chicken-Breast", "quantity_required": 100},
                {"ingredient_name": "Breadcrumbs", "quantity_required": 20},
                {"ingredient_name": "All-Purpose-Flour", "quantity_required": 15},
                {"ingredient_name": "Eggs", "quantity_required": 1},
                {"ingredient_name": "Salt", "quantity_required": 1},
                {"ingredient_name": "Black-Pepper", "quantity_required": 1},
                {"ingredient_name": "Paprika", "quantity_required": 1},
                {"ingredient_name": "Garlic", "quantity_required": 1},
                {"ingredient_name": "Vegetable-Oil", "quantity_required": 100},
            ],
            "Spring Rolls": [
                {"ingredient_name": "Cabbage-Green", "quantity_required": 30},
                {"ingredient_name": "Carrots", "quantity_required": 10},
                {"ingredient_name": "Onions", "quantity_required": 5},
                {"ingredient_name": "Soy-Sauce", "quantity_required": 5},
                {"ingredient_name": "Sesame-Oil", "quantity_required": 2},
                {"ingredient_name": "Salt", "quantity_required": 1},
                {"ingredient_name": "Black-Pepper", "quantity_required": 1},
                {"ingredient_name": "Vegetable-Oil", "quantity_required": 100},
            ],
            "Potato Skins": [
                {"ingredient_name": "Potatoes", "quantity_required": 200},
                {"ingredient_name": "Cheddar-Cheese", "quantity_required": 30},
                {"ingredient_name": "Onions", "quantity_required": 5},
                {"ingredient_name": "Sour-Cream", "quantity_required": 20},
                {"ingredient_name": "Salt", "quantity_required": 1},
                {"ingredient_name": "Black-Pepper", "quantity_required": 1},
                {"ingredient_name": "Vegetable-Oil", "quantity_required": 100},
            ],
            "Vanilla Ice Cream": [
                {"ingredient_name": "Vanilla Ice Cream", "quantity_required": 100},
            ],
            "Chocolate Ice Cream": [
                {"ingredient_name": "Chocolate Ice Cream", "quantity_required": 100},
            ],
            "Strawberry Ice Cream": [
                {"ingredient_name": "Strawberry Ice Cream", "quantity_required": 100},
            ],
            "Mint Chocolate Chip": [
                {"ingredient_name": "Mint Chocolate Chip", "quantity_required": 100},
            ],
            "Rocky Road": [
                {"ingredient_name": "Rocky Road Ice Cream", "quantity_required": 100},
            ],
            "Chocolate Cake": [
                {"ingredient_name": "All-Purpose-Flour", "quantity_required": 100},
                {"ingredient_name": "Sugar", "quantity_required": 80},
                {"ingredient_name": "Cocoa-Powder", "quantity_required": 30},
                {"ingredient_name": "Baking-Powder", "quantity_required": 5},
                {"ingredient_name": "Baking-Soda", "quantity_required": 3},
                {"ingredient_name": "Salt", "quantity_required": 1},
                {"ingredient_name": "Eggs", "quantity_required": 2},
                {"ingredient_name": "Milk", "quantity_required": 50},
                {"ingredient_name": "Vegetable-Oil", "quantity_required": 20},
                {"ingredient_name": "Vanilla-Extract", "quantity_required": 2},
            ],
            "Cheesecake": [
                {"ingredient_name": "Cream-Cheese", "quantity_required": 200},
                {"ingredient_name": "Sugar", "quantity_required": 50},
                {"ingredient_name": "Eggs", "quantity_required": 2},
                {"ingredient_name": "Vanilla-Extract", "quantity_required": 2},
                {"ingredient_name": "Sour-Cream", "quantity_required": 30},
                {"ingredient_name": "Butter-Unsalted", "quantity_required": 20},
                {"ingredient_name": "Salt", "quantity_required": 1},
            ],
            "Apple Pie": [
                {"ingredient_name": "Apples", "quantity_required": 150},
                {"ingredient_name": "Sugar", "quantity_required": 50},
                {"ingredient_name": "Cinnamon", "quantity_required": 2},
                {"ingredient_name": "Nutmeg", "quantity_required": 1},
                {"ingredient_name": "Salt", "quantity_required": 1},
                {"ingredient_name": "All-Purpose-Flour", "quantity_required": 100},
                {"ingredient_name": "Butter-Unsalted", "quantity_required": 50}, 
            ],
            "Lemon Tart": [
                {"ingredient_name": "All-Purpose-Flour", "quantity_required": 80},
                {"ingredient_name": "Butter-Unsalted", "quantity_required": 40},
                {"ingredient_name": "Sugar", "quantity_required": 30},
                {"ingredient_name": "Eggs", "quantity_required": 2},
                {"ingredient_name": "Lemon-Juice", "quantity_required": 30},
                {"ingredient_name": "Lemons", "quantity_required": 2},
                {"ingredient_name": "Salt", "quantity_required": 1},
            ],
            "Éclair": [
                {"ingredient_name": "All-Purpose-Flour", "quantity_required": 50},
                {"ingredient_name": "Butter-Salted", "quantity_required": 25},
                {"ingredient_name": "Eggs", "quantity_required": 2},
                {"ingredient_name": "Salt", "quantity_required": 1},
                {"ingredient_name": "Milk", "quantity_required": 100},
                {"ingredient_name": "Sugar", "quantity_required": 20}, 
                {"ingredient_name": "Vanilla-Extract", "quantity_required": 2},
                {"ingredient_name": "Chocolate-Chips", "quantity_required": 30}, 
            ],
            "Americano": [
                {"ingredient_name": "Coffee-Ground", "quantity_required": 30},
            ],
            "Latte": [
                {"ingredient_name": "Coffee-Ground", "quantity_required": 30},
                {"ingredient_name": "Milk", "quantity_required": 170},
            ],
            "Cappuccino": [
                {"ingredient_name": "Coffee-Ground", "quantity_required": 30},
                {"ingredient_name": "Milk", "quantity_required": 100},
            ],
            "Herbal Tea": [
                {"ingredient_name": "Herbal-Tea-Bag", "quantity_required": 1},
                {"ingredient_name": "Honey", "quantity_required": 10},
            ],
            "Hot Chocolate": [
                {"ingredient_name": "Cocoa-Powder", "quantity_required": 20},
                {"ingredient_name": "Sugar", "quantity_required": 15},
                {"ingredient_name": "Milk", "quantity_required": 200},
                {"ingredient_name": "Heavy-Cream", "quantity_required": 30},
            ],
            "Coke": [
                {"ingredient_name": "Coke", "quantity_required": 1},
            ],
            "Sprite": [
                {"ingredient_name": "Sprite", "quantity_required": 1},
            ],
            "Ginger Ale": [
                {"ingredient_name": "Ginger Ale", "quantity_required": 1},
            ],
            "Root Beer": [
                {"ingredient_name": "Root Beer", "quantity_required": 1},
            ],
            "Lemonade": [
                {"ingredient_name": "Lemonade", "quantity_required": 1},
            ],
            "Arugula Salad": [
                {"ingredient_name": "Parmesan-Cheese", "quantity_required": 15},
                {"ingredient_name": "Lemon-Juice", "quantity_required": 5},
                {"ingredient_name": "Olive-Oil-Light", "quantity_required": 10},
                {"ingredient_name": "Salt", "quantity_required": 1},
                {"ingredient_name": "Black-Pepper", "quantity_required": 1},
            ],
            "Spinach Salad": [
                {"ingredient_name": "Spinach", "quantity_required": 50},
                {"ingredient_name": "Onions", "quantity_required": 10},
                {"ingredient_name": "Mushrooms", "quantity_required": 15},
                {"ingredient_name": "Eggs", "quantity_required": 1},
                {"ingredient_name": "Olive-Oil-Light", "quantity_required": 10},
                {"ingredient_name": "Balsamic-Vinegar", "quantity_required": 5},
                {"ingredient_name": "Salt", "quantity_required": 1},
                {"ingredient_name": "Black-Pepper", "quantity_required": 1},
            ],
            "Kale Caesar": [
                {"ingredient_name": "Kale", "quantity_required": 50},
                {"ingredient_name": "Parmesan-Cheese", "quantity_required": 15},
                {"ingredient_name": "Caesar-Dressing", "quantity_required": 25},
                {"ingredient_name": "Lemon-Juice", "quantity_required": 5},
                {"ingredient_name": "Salt", "quantity_required": 1},
                {"ingredient_name": "Black-Pepper", "quantity_required": 1},
            ],
            "Mixed Greens": [
                {"ingredient_name": "Mixed-Salad-Greens", "quantity_required": 50},
                {"ingredient_name": "Cherry-Tomatoes", "quantity_required": 20},
                {"ingredient_name": "Cucumber", "quantity_required": 15},
                {"ingredient_name": "Onions", "quantity_required": 10},
                {"ingredient_name": "Olive-Oil-Light", "quantity_required": 10},
                {"ingredient_name": "Wine-Red", "quantity_required": 5},
                {"ingredient_name": "Salt", "quantity_required": 1},
                {"ingredient_name": "Black-Pepper", "quantity_required": 1},
            ],
            "Watercress Salad": [
                {"ingredient_name": "Radishes", "quantity_required": 10},
                {"ingredient_name": "Cucumber", "quantity_required": 15},
                {"ingredient_name": "Lemon-Juice", "quantity_required": 5},
                {"ingredient_name": "Olive-Oil-Light", "quantity_required": 10},
                {"ingredient_name": "Salt", "quantity_required": 1},
                {"ingredient_name": "Black-Pepper", "quantity_required": 1},
            ],
            "Chicken Caesar": [
                {"ingredient_name": "Lettuce", "quantity_required": 50},
                {"ingredient_name": "Chicken-Breast", "quantity_required": 100},
                {"ingredient_name": "Parmesan-Cheese", "quantity_required": 15},
                {"ingredient_name": "Caesar-Dressing", "quantity_required": 25},
                {"ingredient_name": "Lemon-Juice", "quantity_required": 5},
                {"ingredient_name": "Salt", "quantity_required": 1},
                {"ingredient_name": "Black-Pepper", "quantity_required": 1},
            ],
            "Tuna Salad": [
                {"ingredient_name": "Tuna", "quantity_required": 80},
                {"ingredient_name": "Mixed-Salad-Greens", "quantity_required": 50},
                {"ingredient_name": "Cherry-Tomatoes", "quantity_required": 20},
                {"ingredient_name": "Cucumber", "quantity_required": 15},
                {"ingredient_name": "Onions", "quantity_required": 10},
                {"ingredient_name": "Olive-Oil-Light", "quantity_required": 10},
                {"ingredient_name": "Lemon-Juice", "quantity_required": 5},
                {"ingredient_name": "Salt", "quantity_required": 1},
                {"ingredient_name": "Black-Pepper", "quantity_required": 1},
            ],
            "Quinoa Salad": [
                {"ingredient_name": "Quinoa", "quantity_required": 50},
                {"ingredient_name": "Mixed-Salad-Greens", "quantity_required": 50},
                {"ingredient_name": "Cherry-Tomatoes", "quantity_required": 20},
                {"ingredient_name": "Cucumber", "quantity_required": 15},
                {"ingredient_name": "Bell-Peppers-Red", "quantity_required": 10},
                {"ingredient_name": "Olive-Oil-Light", "quantity_required": 10},
                {"ingredient_name": "Lemon-Juice", "quantity_required": 5},
                {"ingredient_name": "Salt", "quantity_required": 1},
                {"ingredient_name": "Black-Pepper", "quantity_required": 1},
            ],
            "Tofu Salad": [
                {"ingredient_name": "Tofu", "quantity_required": 80},
                {"ingredient_name": "Mixed-Salad-Greens", "quantity_required": 50},
                {"ingredient_name": "Carrots", "quantity_required": 15},
                {"ingredient_name": "Cucumber", "quantity_required": 15},
                {"ingredient_name": "Bell-Peppers-Red", "quantity_required": 10},
                {"ingredient_name": "Sesame-Seeds", "quantity_required": 5},
                {"ingredient_name": "Sesame-Oil", "quantity_required": 5},
                {"ingredient_name": "Soy-Sauce", "quantity_required": 5},
                {"ingredient_name": "Salt", "quantity_required": 1},
                {"ingredient_name": "Black-Pepper", "quantity_required": 1},
            ],
            "Shrimp Salad": [
                {"ingredient_name": "Shrimp", "quantity_required": 80},
                {"ingredient_name": "Mixed-Salad-Greens", "quantity_required": 50},
                {"ingredient_name": "Cherry-Tomatoes", "quantity_required": 20},
                {"ingredient_name": "Cucumber", "quantity_required": 15},
                {"ingredient_name": "Avocado", "quantity_required": 30},
                {"ingredient_name": "Olive-Oil-Light", "quantity_required": 10},
                {"ingredient_name": "Lemon-Juice", "quantity_required": 5},
                {"ingredient_name": "Salt", "quantity_required": 1},
                {"ingredient_name": "Black-Pepper", "quantity_required": 1},
            ],
            "Classic French Fries": [
                {"ingredient_name": "Potatoes", "quantity_required": 150},
                {"ingredient_name": "Vegetable-Oil", "quantity_required": 100},
                {"ingredient_name": "Salt", "quantity_required": 2},
            ],
            "Sweet Potato Fries": [
                {"ingredient_name": "Sweet-Potatoes", "quantity_required": 150},
                {"ingredient_name": "Vegetable-Oil", "quantity_required": 100},
                {"ingredient_name": "Salt", "quantity_required": 2},
            ],
            "Curly Fries": [
                {"ingredient_name": "Potatoes", "quantity_required": 150},
                {"ingredient_name": "Vegetable-Oil", "quantity_required": 100},
                {"ingredient_name": "Salt", "quantity_required": 2},
                {"ingredient_name": "Paprika", "quantity_required": 1},
                {"ingredient_name": "Garlic", "quantity_required": 1},
                {"ingredient_name": "Onions", "quantity_required": 1},
            ],
            "Garlic Parmesan Fries": [
                {"ingredient_name": "Potatoes", "quantity_required": 150},
                {"ingredient_name": "Vegetable-Oil", "quantity_required": 100},
                {"ingredient_name": "Garlic", "quantity_required": 5},
                {"ingredient_name": "Parmesan-Cheese", "quantity_required": 15},
                {"ingredient_name": "Salt", "quantity_required": 2},
                {"ingredient_name": "Parsley", "quantity_required": 2},
            ],
            "Truffle Fries": [
                {"ingredient_name": "Potatoes", "quantity_required": 150},
                {"ingredient_name": "Vegetable-Oil", "quantity_required": 100},
                {"ingredient_name": "Salt", "quantity_required": 2},
                {"ingredient_name": "Parmesan-Cheese", "quantity_required": 15},
                {"ingredient_name": "Parsley", "quantity_required": 2},
            ],
            "Steamed Rice": [
                {"ingredient_name": "Rice-white", "quantity_required": 100},
                {"ingredient_name": "Salt", "quantity_required": 1},
            ],
            "Fried Rice": [
                {"ingredient_name": "Rice-White", "quantity_required": 100},
                {"ingredient_name": "Vegetable-Oil", "quantity_required": 20},
                {"ingredient_name": "Eggs", "quantity_required": 1},
                {"ingredient_name": "Carrots", "quantity_required": 10},
                {"ingredient_name": "Green-Peas", "quantity_required": 10},
                {"ingredient_name": "Soy-Sauce", "quantity_required": 15},
                {"ingredient_name": "Garlic", "quantity_required": 2},
                {"ingredient_name": "Onions", "quantity_required": 10},
                {"ingredient_name": "Salt", "quantity_required": 1},
                {"ingredient_name": "Black-Pepper", "quantity_required": 1},
            ],
            "Quinoa Pilaf": [
                {"ingredient_name": "Quinoa", "quantity_required": 100},
                {"ingredient_name": "Olive-Oil-Light", "quantity_required": 10},
                {"ingredient_name": "Onions", "quantity_required": 10},
                {"ingredient_name": "Garlic", "quantity_required": 2},
                {"ingredient_name": "Parsley", "quantity_required": 5},
                {"ingredient_name": "Salt", "quantity_required": 1},
                {"ingredient_name": "Black-Pepper", "quantity_required": 1},
            ],
            "Couscous": [
                {"ingredient_name": "Couscous", "quantity_required": 100},
                {"ingredient_name": "Olive-Oil-Light", "quantity_required": 10},
                {"ingredient_name": "Lemon-Juice", "quantity_required": 5},
                {"ingredient_name": "Salt", "quantity_required": 1},
                {"ingredient_name": "Black-Pepper", "quantity_required": 1},
            ],
            "Barley Risotto": [
                {"ingredient_name": "Barley", "quantity_required": 100},
                {"ingredient_name": "Olive-Oil-Light", "quantity_required": 10},
                {"ingredient_name": "Onions", "quantity_required": 10},
                {"ingredient_name": "Garlic", "quantity_required": 2},
                {"ingredient_name": "Parmesan-Cheese", "quantity_required": 15},
                {"ingredient_name": "Thyme", "quantity_required": 2},
                {"ingredient_name": "Salt", "quantity_required": 1},
                {"ingredient_name": "Black-Pepper", "quantity_required": 1},
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