from django.core.management.base import BaseCommand
from menu.models import IngredientTag

class Command(BaseCommand):
    help = "Populate IngredientTag model with predefined data"

    def handle(self, *args, **kwargs):
        ingredient_tags = [
            IngredientTag(name="Spicy", description="Ingredients that add heat or spiciness to a dish."),
            IngredientTag(name="Gluten-Free", description="Ingredients that do not contain gluten."),
            IngredientTag(name="Vegan", description="Ingredients that are plant-based and do not contain animal products."),
            IngredientTag(name="Dairy-Free", description="Ingredients that do not contain dairy products."),
            IngredientTag(name="Nut-Free", description="Ingredients that do not contain any type of nuts."),
            IngredientTag(name="Low-Carb", description="Ingredients that are low in carbohydrates."),
            IngredientTag(name="High-Protein", description="Ingredients that are rich in protein."),
            IngredientTag(name="Organic", description="Ingredients that are grown without the use of synthetic pesticides or fertilizers."),
            IngredientTag(name="Local", description="Ingredients that are sourced locally, usually within a specific region."),
            IngredientTag(name="Sustainable", description="Ingredients that are grown or produced in an environmentally sustainable way."),
            IngredientTag(name="Halal", description="Ingredients that comply with Islamic dietary laws."),
            IngredientTag(name="Kosher", description="Ingredients that comply with Jewish dietary laws."),
            IngredientTag(name="Paleo", description="Ingredients that adhere to the Paleo diet, typically excluding processed foods and grains."),
            IngredientTag(name="Low-Sodium", description="Ingredients that are low in sodium content."),
            IngredientTag(name="Raw", description="Ingredients that are not cooked and are in their natural state."),
            IngredientTag(name="Caffeinated", description="Ingredients that contain caffeine, such as coffee or tea."),
            IngredientTag(name="Sweet", description="Ingredients that are sweet in taste, such as sugar, honey, or fruit."),
            IngredientTag(name="Savory", description="Ingredients that are salty or umami-flavored, such as soy sauce or mushrooms."),
            IngredientTag(name="Fermented", description="Ingredients that are produced through fermentation, like kimchi, yogurt, or kombucha."),
            IngredientTag(name="Processed", description="Ingredients that have been altered from their natural state for preservation or convenience."),
            IngredientTag(name="Superfood", description="Ingredients that are nutrient-dense and considered to have health benefits, such as kale or chia seeds."),
        ]

        IngredientTag.objects.bulk_create(ingredient_tags)
        self.stdout.write(self.style.SUCCESS("IngredientTag data populated successfully using bulk_create!"))