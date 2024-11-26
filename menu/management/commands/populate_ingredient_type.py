from django.core.management.base import BaseCommand
from menu.models import IngredientType

class Command(BaseCommand):
    help = "Populate IngredientType model with predefined data"

    def handle(self, *args, **kwargs):
        ingredient_types = [
            IngredientType(name="Vegetables", description="Fresh produce like tomatoes, onions, garlic, etc."),
            IngredientType(name="Fruits", description="Sweet, fleshy products of plants such as apples, bananas, citrus fruits, etc."),
            IngredientType(name="Meat & Poultry", description="Animal flesh consumed as food such as chicken, beef, pork, etc."),
            IngredientType(name="Seafood", description="Fish, shellfish, and other sea creatures like shrimp, scallops, etc."),
            IngredientType(name="Grains & Starches", description="Grains like rice, quinoa, and various starch types."),
            IngredientType(name="Dairy", description="Milk, cheese, butter, and other milk-based products."),
            IngredientType(name="Egg", description="Edible eggs from various poultry, including free-range and organic."),
            IngredientType(name="Spices & Herbs", description="Seasonings like salt, pepper, basil, thyme, etc."),
            IngredientType(name="Condiments & Sauces", description="Condiments and sauces like soy sauce, ketchup, mustard, etc."),
            IngredientType(name="Oils & Vinegars", description="Cooking oils and fats like olive oil, sunflower oil, butter, etc."),
            IngredientType(name="Legumes & Pulses", description="Beans, lentils, chickpeas, and other legumes."),
            IngredientType(name="Beverages", description="Drinks like coffee, tea, juices, and soft drinks."),
            IngredientType(name="Nuts & Seeds", description="Edible seeds and nuts like almonds, chia seeds, and walnuts."),
            IngredientType(name="Sweeteners & Baking Essentials", description="Natural and artificial sweeteners like honey, maple syrup, stevia, etc. And Ingredients for baking, including flour, sugar, and yeast."),
            IngredientType(name="Frozen Foods", description="Frozen ingredients such as vegetables, fruits, and meats."),
            IngredientType(name="Miscellaneous", description="Any ingredient that doesn’t fit into the above categories."),
        ]

        # Bulk create the ingredient types
        IngredientType.objects.bulk_create(ingredient_types)

        self.stdout.write(self.style.SUCCESS("IngredientType data populated successfully!"))
