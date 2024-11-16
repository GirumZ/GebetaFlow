from django.core.management.base import BaseCommand
from menu.models import IngredientType

class Command(BaseCommand):
    help = "Populate IngredientType model with predefined data"

    def handle(self, *args, **kwargs):
        ingredient_types = [
            IngredientType(name="Meat", description="Animal-based protein ingredients used in main dishes."),
            IngredientType(name="Seafood", description="Marine-based ingredients, including fish and shellfish."),
            IngredientType(name="Dairy", description="Milk-derived products for cooking and flavor."),
            IngredientType(name="Vegetables", description="Plant-based ingredients for sides or main courses."),
            IngredientType(name="Fruits", description="Sweet or tart plant-based ingredients for various uses."),
            IngredientType(name="Grains & Starches", description="Staples providing carbohydrates, like rice and pasta."),
            IngredientType(name="Spices & Herbs", description="Flavor enhancers, dried or fresh, for seasoning dishes."),
            IngredientType(name="Oils & Fats", description="Ingredients for cooking, frying, or adding richness."),
            IngredientType(name="Sauces & Condiments", description="Prepared flavoring mixtures for enhancing dishes."),
            IngredientType(name="Baking Essentials", description="Key ingredients for creating baked goods."),
            IngredientType(name="Beverages", description="Ingredients for preparing or serving drinks."),
        ]

        IngredientType.objects.bulk_create(ingredient_types)

        self.stdout.write(self.style.SUCCESS("IngredientType data populated successfully using bulk_create!"))