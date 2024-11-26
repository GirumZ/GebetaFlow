from django.core.management.base import BaseCommand
from menu.models import Ingredient, IngredientType, IngredientTag

class Command(BaseCommand):
    help = "Populate Ingredient model with predefined data"

    def handle(self, *args, **kwargs):
        # Ensure related models are populated first
        vegetable_type = IngredientType.objects.get(name="Vegetables")
        fruit_type = IngredientType.objects.get(name="Fruits")
        meat_type = IngredientType.objects.get(name="Meat & Poultry")
        seafood_type = IngredientType.objects.get(name="Seafood")
        grains_starches_type = IngredientType.objects.get(name="Grains & Starches")
        dairy_type = IngredientType.objects.get(name="Dairy")
        egg_type = IngredientType.objects.get(name="Egg")
        spices_herbs_type = IngredientType.objects.get(name="Spices & Herbs")
        condiments_sauces_type = IngredientType.objects.get(name="Condiments & Sauces")
        oils_vinegares_type = IngredientType.objects.get(name="Oils & Vinegars")
        legumes_pulses_type = IngredientType.objects.get(name="Legumes & Pulses")
        beverages_type = IngredientType.objects.get(name="Beverages")
        nuts_seeds_type = IngredientType.objects.get(name="Nuts & Seeds")
        sweeteners_baking_essentials_type = IngredientType.objects.get(name="Sweeteners & Baking Essentials")
        frozen_foods_type = IngredientType.objects.get(name="Frozen Foods")
        miscellaneous_type = IngredientType.objects.get(name="Miscellaneous")

        # Ensure ingredient tags are populated
        spicy_tag = IngredientTag.objects.get(name="Spicy")
        gluten_free_tag = IngredientTag.objects.get(name="Gluten-Free")
        vegan_tag = IngredientTag.objects.get(name="Vegan")
        dairy_free_tag = IngredientTag.objects.get(name="Dairy-Free")
        nut_free_tag = IngredientTag.objects.get(name="Nut-Free")
        low_carb_tag = IngredientTag.objects.get(name="Low-Carb")
        high_protein_tag = IngredientTag.objects.get(name="High-Protein")
        organic_tag = IngredientTag.objects.get(name="Organic")
        local_tag = IngredientTag.objects.get(name="Local")
        sustainable_tag = IngredientTag.objects.get(name="Sustainable")
        halal_tag = IngredientTag.objects.get(name="Halal")
        kosher_tag = IngredientTag.objects.get(name="Kosher")
        paleo_tag = IngredientTag.objects.get(name="Paleo")
        low_sodium_tag = IngredientTag.objects.get(name="Low-Sodium")
        raw_tag = IngredientTag.objects.get(name="Raw")
        caffeinated_tag = IngredientTag.objects.get(name="Caffeinated")
        sweet_tag = IngredientTag.objects.get(name="Sweet")
        savory_tag = IngredientTag.objects.get(name="Savory")
        fermented_tag = IngredientTag.objects.get(name="Fermented")
        processed_tag = IngredientTag.objects.get(name="Processed")
        superfood_tag = IngredientTag.objects.get(name="Superfood")

        # Predefined ingredients
        ingredients = [
            # vegetables
            Ingredient(name="Lettuce", ingredient_type=vegetable_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Lettuce-Romaine", ingredient_type=vegetable_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Carrots", ingredient_type=vegetable_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Cucumbers", ingredient_type=vegetable_type, quantity_in_stock=4000, unit="g"),
            Ingredient(name="Bell-Peppers-Red", ingredient_type=vegetable_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Bell-Peppers-Green", ingredient_type=vegetable_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Bell-Peppers-Yellow", ingredient_type=vegetable_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Onions", ingredient_type=vegetable_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Onions-Red", ingredient_type=vegetable_type, quantity_in_stock=4000, unit="g"),
            Ingredient(name="Onions-White", ingredient_type=vegetable_type, quantity_in_stock=4000, unit="g"),
            Ingredient(name="Garlic", ingredient_type=vegetable_type, quantity_in_stock=4000, unit="g"),
            Ingredient(name="Spinach", ingredient_type=vegetable_type, quantity_in_stock=3500, unit="g"),
            Ingredient(name="Kale", ingredient_type=vegetable_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Broccoli", ingredient_type=vegetable_type, quantity_in_stock=4000, unit="g"),
            Ingredient(name="Mushrooms", ingredient_type=vegetable_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Mushrooms-Portobello", ingredient_type=vegetable_type, quantity_in_stock=2000, unit="g"),
            Ingredient(name="Mushrooms-Shiitake", ingredient_type=vegetable_type, quantity_in_stock=2000, unit="g"),
            Ingredient(name="Zucchini", ingredient_type=vegetable_type, quantity_in_stock=3500, unit="g"),
            Ingredient(name="Eggplant", ingredient_type=vegetable_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Sweet-Potatoes", ingredient_type=vegetable_type, quantity_in_stock=4000, unit="g"),
            Ingredient(name="Potatoes", ingredient_type=vegetable_type, quantity_in_stock=4000, unit="g"),            
            Ingredient(name="Asparagus", ingredient_type=vegetable_type, quantity_in_stock=2500, unit="g"),
            Ingredient(name="Cabbage-Green", ingredient_type=vegetable_type, quantity_in_stock=3500, unit="g"),
            Ingredient(name="Cabbage-Red", ingredient_type=vegetable_type, quantity_in_stock=3500, unit="g"),
            Ingredient(name="Avocado", ingredient_type=vegetable_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Leeks", ingredient_type=vegetable_type, quantity_in_stock=2500, unit="g"),
            Ingredient(name="Celery", ingredient_type=vegetable_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Beets", ingredient_type=vegetable_type, quantity_in_stock=2500, unit="g"),
            Ingredient(name="Radishes", ingredient_type=vegetable_type, quantity_in_stock=2000, unit="g"),
            Ingredient(name="Mixed-Vegetables", ingredient_type=vegetable_type, quantity_in_stock=2000, unit="g"),
            Ingredient(name="Tomatoes", ingredient_type=vegetable_type, quantity_in_stock=2000, unit="g"),
            Ingredient(name="Chickpeas", ingredient_type=vegetable_type, quantity_in_stock=2000, unit="g"),
            Ingredient(name="Cilantro", ingredient_type=vegetable_type, quantity_in_stock=2000, unit="g"),
            Ingredient(name="Corn", ingredient_type=vegetable_type, quantity_in_stock=2000, unit="g"),
            Ingredient(name="Cucumber", ingredient_type=vegetable_type, quantity_in_stock=2000, unit="g"),
            Ingredient(name="Olives", ingredient_type=vegetable_type, quantity_in_stock=2000, unit="g"),
            Ingredient(name="Cabbbage", ingredient_type=vegetable_type, quantity_in_stock=2000, unit="g"),
            Ingredient(name="Pickles", ingredient_type=vegetable_type, quantity_in_stock=2000, unit="g"),
            Ingredient(name="Veggie-Patty", ingredient_type=vegetable_type, quantity_in_stock=2000, unit="g"),
            Ingredient(name="Jalapenos", ingredient_type=vegetable_type, quantity_in_stock=2000, unit="g"),
            Ingredient(name="Green-Peas", ingredient_type=vegetable_type, quantity_in_stock=2000, unit="g"),
            Ingredient(name="Mixed-Salad-Greens", ingredient_type=vegetable_type, quantity_in_stock=2000, unit="g"),
            Ingredient(name="Cherry-Tomatoes", ingredient_type=vegetable_type, quantity_in_stock=2000, unit="g"),

            # fruits
            Ingredient(name="Bananas", ingredient_type=fruit_type, quantity_in_stock=4000, unit="g"),
            Ingredient(name="Oranges", ingredient_type=fruit_type, quantity_in_stock=4500, unit="g"),
            Ingredient(name="Lemons", ingredient_type=fruit_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Strawberries", ingredient_type=fruit_type, quantity_in_stock=3500, unit="g"),
            Ingredient(name="Blueberries", ingredient_type=fruit_type, quantity_in_stock=2500, unit="g"),
            Ingredient(name="Grapes-Red", ingredient_type=fruit_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Grapes-Green", ingredient_type=fruit_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Pineapple", ingredient_type=fruit_type, quantity_in_stock=2500, unit="g"),
            Ingredient(name="Mangoes", ingredient_type=fruit_type, quantity_in_stock=3500, unit="g"),
            Ingredient(name="Pears", ingredient_type=fruit_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Peaches", ingredient_type=fruit_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Plums", ingredient_type=fruit_type, quantity_in_stock=2500, unit="g"),
            Ingredient(name="Pomegranate", ingredient_type=fruit_type, quantity_in_stock=2500, unit="g"),
            Ingredient(name="Raspberries", ingredient_type=fruit_type, quantity_in_stock=2000, unit="g"),
            Ingredient(name="Cherries", ingredient_type=fruit_type, quantity_in_stock=2500, unit="g"),
            Ingredient(name="Apples-Granny-Smith", ingredient_type=fruit_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Apples-Fuji", ingredient_type=fruit_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Apples", ingredient_type=fruit_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Limes", ingredient_type=fruit_type, quantity_in_stock=2500, unit="g"),
            Ingredient(name="Kiwi", ingredient_type=fruit_type, quantity_in_stock=2000, unit="g"),
            Ingredient(name="Apricots", ingredient_type=fruit_type, quantity_in_stock=2500, unit="g"),

            # meat and poultry
            Ingredient(name="Beef-Ground", ingredient_type=meat_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Beef-Steak", ingredient_type=meat_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Beef", ingredient_type=meat_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Beef-Sirloin", ingredient_type=meat_type, quantity_in_stock=4000, unit="g"),
            Ingredient(name="Beef-Ribeye", ingredient_type=meat_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="T-bone", ingredient_type=meat_type, quantity_in_stock=3000, unit="g"),            
            Ingredient(name="Pork-Chops", ingredient_type=meat_type, quantity_in_stock=4000, unit="g"),
            Ingredient(name="Pork-Belly", ingredient_type=meat_type, quantity_in_stock=4000, unit="g"),
            Ingredient(name="Pork-Ribs", ingredient_type=meat_type, quantity_in_stock=4000, unit="g"),
            Ingredient(name="Pork-Ground", ingredient_type=meat_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Pork-Tenderloin", ingredient_type=meat_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Bacon", ingredient_type=meat_type, quantity_in_stock=2500, unit="g"),
            Ingredient(name="Lamb-Chops", ingredient_type=meat_type, quantity_in_stock=2000, unit="g"),
            Ingredient(name="Lamb-Ground", ingredient_type=meat_type, quantity_in_stock=2000, unit="g"),
            Ingredient(name="Lamb-Leg", ingredient_type=meat_type, quantity_in_stock=2000, unit="g"),
            Ingredient(name="Chicken-Breast", ingredient_type=meat_type, quantity_in_stock=4000, unit="g"),
            Ingredient(name="Chicken-Thighs", ingredient_type=meat_type, quantity_in_stock=4000, unit="g"),
            Ingredient(name="Chicken-Drumsticks", ingredient_type=meat_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Chicken-Wings", ingredient_type=meat_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Turkey-Ground", ingredient_type=meat_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Turkey-Breast", ingredient_type=meat_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Turkey-Legs", ingredient_type=meat_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Sausages-Italian", ingredient_type=meat_type, quantity_in_stock=2000, unit="g"),
            Ingredient(name="Sausages", ingredient_type=meat_type, quantity_in_stock=2000, unit="g"),
            Ingredient(name="Sausages-Chorizo", ingredient_type=meat_type, quantity_in_stock=2000, unit="g"),
            Ingredient(name="Sausages-Bratwurst", ingredient_type=meat_type, quantity_in_stock=2000, unit="g"),
            Ingredient(name="Duck", ingredient_type=meat_type, quantity_in_stock=1500, unit="g"),
            Ingredient(name="Ham", ingredient_type=meat_type, quantity_in_stock=2500, unit="g"),
            Ingredient(name="Eggs", ingredient_type=meat_type, quantity_in_stock=2500, unit="g"),
            Ingredient(name="Pepperoni", ingredient_type=meat_type, quantity_in_stock=2500, unit="g"),
            Ingredient(name="Sausage", ingredient_type=meat_type, quantity_in_stock=2500, unit="g"),
            


            # sea foods
            Ingredient(name="Shrimp", ingredient_type=seafood_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Salmon", ingredient_type=seafood_type, quantity_in_stock=4500, unit="g"),
            Ingredient(name="Tuna", ingredient_type=seafood_type, quantity_in_stock=4000, unit="g"),
            Ingredient(name="Cod", ingredient_type=seafood_type, quantity_in_stock=3500, unit="g"),
            Ingredient(name="Halibut", ingredient_type=seafood_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Mahi-Mahi", ingredient_type=seafood_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Mussels", ingredient_type=seafood_type, quantity_in_stock=2500, unit="g"),
            Ingredient(name="Clams", ingredient_type=seafood_type, quantity_in_stock=2500, unit="g"),
            Ingredient(name="Scallops", ingredient_type=seafood_type, quantity_in_stock=2000, unit="g"),
            Ingredient(name="Crab-Lump", ingredient_type=seafood_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Crab-King", ingredient_type=seafood_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Lobster", ingredient_type=seafood_type, quantity_in_stock=2000, unit="g"),
            Ingredient(name="Anchovies", ingredient_type=seafood_type, quantity_in_stock=1500, unit="g"),
            Ingredient(name="Squid-Calamari", ingredient_type=seafood_type, quantity_in_stock=2000, unit="g"),
            Ingredient(name="White-Fish", ingredient_type=seafood_type, quantity_in_stock=2000, unit="g"),
            Ingredient(name="Sushi", ingredient_type=seafood_type, quantity_in_stock=2000, unit="g"),
            Ingredient(name="Wasabi", ingredient_type=seafood_type, quantity_in_stock=2000, unit="g"),


            # dairy
            Ingredient(name="Butter-Salted", ingredient_type=dairy_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Butter-Unsalted", ingredient_type=dairy_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Heavy-Cream", ingredient_type=dairy_type, quantity_in_stock=2000, unit="ml"),
            Ingredient(name="Sour-Cream", ingredient_type=dairy_type, quantity_in_stock=2000, unit="ml"),
            Ingredient(name="Cream-Cheese", ingredient_type=dairy_type, quantity_in_stock=2500, unit="g"),
            Ingredient(name="Cheddar-Cheese", ingredient_type=dairy_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Gorgonzola-Cheese", ingredient_type=dairy_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Mozzarella-Cheese", ingredient_type=dairy_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Parmesan-Cheese", ingredient_type=dairy_type, quantity_in_stock=2000, unit="g"),
            Ingredient(name="Goat-Cheese", ingredient_type=dairy_type, quantity_in_stock=1500, unit="g"),
            Ingredient(name="Ricotta-Cheese", ingredient_type=dairy_type, quantity_in_stock=2000, unit="g"),
            Ingredient(name="Feta-Cheese", ingredient_type=dairy_type, quantity_in_stock=2000, unit="g"),
            Ingredient(name="Brie", ingredient_type=dairy_type, quantity_in_stock=1500, unit="g"),
            Ingredient(name="Blue-Cheese", ingredient_type=dairy_type, quantity_in_stock=1000, unit="g"),
            Ingredient(name="Swiss-Cheese", ingredient_type=dairy_type, quantity_in_stock=2000, unit="g"),
            Ingredient(name="Milk", ingredient_type=dairy_type, quantity_in_stock=5000, unit="ml"),
            Ingredient(name="Milk-Skim", ingredient_type=dairy_type, quantity_in_stock=4000, unit="ml"),
            Ingredient(name="Milk-Plant-Based", ingredient_type=dairy_type, quantity_in_stock=3500, unit="ml"),
            Ingredient(name="Yogurt-Greek", ingredient_type=dairy_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Yogurt", ingredient_type=dairy_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Yogurt-Flavored", ingredient_type=dairy_type, quantity_in_stock=3000, unit="g"),

            # grains and starchs
            Ingredient(name="Rice-White", ingredient_type=grains_starches_type, quantity_in_stock=10000, unit="g"),
            Ingredient(name="Rice-Brown", ingredient_type=grains_starches_type, quantity_in_stock=8000, unit="g"),
            Ingredient(name="Rice-Jasmine", ingredient_type=grains_starches_type, quantity_in_stock=7000, unit="g"),
            Ingredient(name="Rice-Basmati", ingredient_type=grains_starches_type, quantity_in_stock=7000, unit="g"),
            Ingredient(name="Quinoa", ingredient_type=grains_starches_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Couscous", ingredient_type=grains_starches_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Barley", ingredient_type=grains_starches_type, quantity_in_stock=4000, unit="g"),
            Ingredient(name="Farro", ingredient_type=grains_starches_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Polenta", ingredient_type=grains_starches_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Oats", ingredient_type=grains_starches_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Bread-Baguette", ingredient_type=grains_starches_type, quantity_in_stock=1000, unit="pcs"),
            Ingredient(name="Bread-Sourdough", ingredient_type=grains_starches_type, quantity_in_stock=800, unit="pcs"),
            Ingredient(name="Bread", ingredient_type=grains_starches_type, quantity_in_stock=800, unit="pcs"),
            Ingredient(name="Bread-Focaccia", ingredient_type=grains_starches_type, quantity_in_stock=500, unit="pcs"),
            Ingredient(name="Breadcrumbs", ingredient_type=grains_starches_type, quantity_in_stock=500, unit="pcs"),
            Ingredient(name="Noodles-Egg", ingredient_type=grains_starches_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Noodles-Rice", ingredient_type=grains_starches_type, quantity_in_stock=4000, unit="g"),
            Ingredient(name="Noodles-Udon", ingredient_type=grains_starches_type, quantity_in_stock=4000, unit="g"),
            Ingredient(name="Tortillas", ingredient_type=grains_starches_type, quantity_in_stock=3000, unit="pcs"),
            Ingredient(name="Spaghetti", ingredient_type=grains_starches_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Penne", ingredient_type=grains_starches_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Fusilli", ingredient_type=grains_starches_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Farfalle", ingredient_type=grains_starches_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Macaroni", ingredient_type=grains_starches_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Rigatoni", ingredient_type=grains_starches_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Pappardelle", ingredient_type=grains_starches_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Fettuccine", ingredient_type=grains_starches_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Tagliatelle", ingredient_type=grains_starches_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Lasagna-Sheets", ingredient_type=grains_starches_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Gnocchi", ingredient_type=grains_starches_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Tortellini", ingredient_type=grains_starches_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Linguine", ingredient_type=grains_starches_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Ravioli", ingredient_type=grains_starches_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Falafel", ingredient_type=grains_starches_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Hummus", ingredient_type=grains_starches_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Tofu", ingredient_type=grains_starches_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Taco-Shells", ingredient_type=grains_starches_type, quantity_in_stock=5000, unit="g"),


            # spices and herbs
            Ingredient(name="Salt-Table", ingredient_type=spices_herbs_type, quantity_in_stock=10000, unit="g"),
            Ingredient(name="Salt-Kosher", ingredient_type=spices_herbs_type, quantity_in_stock=8000, unit="g"),
            Ingredient(name="Salt-Sea", ingredient_type=spices_herbs_type, quantity_in_stock=8000, unit="g"),
            Ingredient(name="Black-Pepper", ingredient_type=spices_herbs_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Garlic-Powder", ingredient_type=spices_herbs_type, quantity_in_stock=4000, unit="g"),
            Ingredient(name="Onion-Powder", ingredient_type=spices_herbs_type, quantity_in_stock=4000, unit="g"),
            Ingredient(name="Paprika-Sweet", ingredient_type=spices_herbs_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Paprika-Smoked", ingredient_type=spices_herbs_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Paprika-Hot", ingredient_type=spices_herbs_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Cumin", ingredient_type=spices_herbs_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Coriander", ingredient_type=spices_herbs_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Turmeric", ingredient_type=spices_herbs_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Chili-Powder", ingredient_type=spices_herbs_type, quantity_in_stock=4000, unit="g"),
            Ingredient(name="Chili-Flakes", ingredient_type=spices_herbs_type, quantity_in_stock=4000, unit="g"),
            Ingredient(name="Cinnamon", ingredient_type=spices_herbs_type, quantity_in_stock=4000, unit="g"),
            Ingredient(name="Nutmeg", ingredient_type=spices_herbs_type, quantity_in_stock=2000, unit="g"),
            Ingredient(name="Thyme", ingredient_type=spices_herbs_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Rosemary", ingredient_type=spices_herbs_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Oregano", ingredient_type=spices_herbs_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Basil", ingredient_type=spices_herbs_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Parsley", ingredient_type=spices_herbs_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Dill", ingredient_type=spices_herbs_type, quantity_in_stock=2000, unit="g"),
            Ingredient(name="Bay-Leaves", ingredient_type=spices_herbs_type, quantity_in_stock=2000, unit="g"),
            Ingredient(name="Sage", ingredient_type=spices_herbs_type, quantity_in_stock=2000, unit="g"),
            Ingredient(name="Tarragon", ingredient_type=spices_herbs_type, quantity_in_stock=2000, unit="g"),
            Ingredient(name="Mint", ingredient_type=spices_herbs_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Salt", ingredient_type=spices_herbs_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Italian-Seasoning", ingredient_type=spices_herbs_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Mixed-Herbs", ingredient_type=spices_herbs_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Ginger", ingredient_type=spices_herbs_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Curry-Powder", ingredient_type=spices_herbs_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Saffron", ingredient_type=spices_herbs_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Paprika", ingredient_type=spices_herbs_type, quantity_in_stock=3000, unit="g"),

            # oils and vinegars
            Ingredient(name="Olive-Oil-Extra-Virgin", ingredient_type=oils_vinegares_type, quantity_in_stock=5000, unit="ml"),
            Ingredient(name="Olive-Oil-Light", ingredient_type=oils_vinegares_type, quantity_in_stock=5000, unit="ml"),
            Ingredient(name="Vegetable-Oil", ingredient_type=oils_vinegares_type, quantity_in_stock=5000, unit="ml"),
            Ingredient(name="Coconut-Oil", ingredient_type=oils_vinegares_type, quantity_in_stock=5000, unit="ml"),
            Ingredient(name="Canola-Oil", ingredient_type=oils_vinegares_type, quantity_in_stock=5000, unit="ml"),
            Ingredient(name="Sesame-Oil", ingredient_type=oils_vinegares_type, quantity_in_stock=5000, unit="ml"),
            Ingredient(name="Peanut-Oil", ingredient_type=oils_vinegares_type, quantity_in_stock=5000, unit="ml"),
            Ingredient(name="Truffle-Oil", ingredient_type=oils_vinegares_type, quantity_in_stock=5000, unit="ml"),
            Ingredient(name="Balsamic-Vinegar", ingredient_type=oils_vinegares_type, quantity_in_stock=5000, unit="ml"),
            Ingredient(name="Red-Wine-Vinegar", ingredient_type=oils_vinegares_type, quantity_in_stock=5000, unit="ml"),
            Ingredient(name="White-Wine-Vinegar", ingredient_type=oils_vinegares_type, quantity_in_stock=5000, unit="ml"),
            Ingredient(name="Apple-Cider-Vinegar", ingredient_type=oils_vinegares_type, quantity_in_stock=5000, unit="ml"),
            Ingredient(name="Rice-Vinegar", ingredient_type=oils_vinegares_type, quantity_in_stock=5000, unit="ml"),
            Ingredient(name="Sherry-Vinegar", ingredient_type=oils_vinegares_type, quantity_in_stock=5000, unit="ml"),
            Ingredient(name="Vinegar", ingredient_type=oils_vinegares_type, quantity_in_stock=5000, unit="ml"),
            Ingredient(name="Lemon-Juice", ingredient_type=oils_vinegares_type, quantity_in_stock=5000, unit="ml"),

            # condiments and sauces
            Ingredient(name="Ketchup", ingredient_type=condiments_sauces_type, quantity_in_stock=10000, unit="g"),
            Ingredient(name="Mustard", ingredient_type=condiments_sauces_type, quantity_in_stock=8000, unit="g"),
            Ingredient(name="Mustard-Dijon", ingredient_type=condiments_sauces_type, quantity_in_stock=8000, unit="g"),
            Ingredient(name="Mustard-Spicy-Brown", ingredient_type=condiments_sauces_type, quantity_in_stock=8000, unit="g"),
            Ingredient(name="Mayonnaise", ingredient_type=condiments_sauces_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Hot-Sauce", ingredient_type=condiments_sauces_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Soy-Sauce", ingredient_type=condiments_sauces_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Worcestershire-Sauce", ingredient_type=condiments_sauces_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="BBQ-Sauce", ingredient_type=condiments_sauces_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Buffalo-Sauce", ingredient_type=condiments_sauces_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Honey-Mustard", ingredient_type=condiments_sauces_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Tartar-Sauce", ingredient_type=condiments_sauces_type, quantity_in_stock=4000, unit="g"),
            Ingredient(name="Ranch-Dressing", ingredient_type=condiments_sauces_type, quantity_in_stock=4000, unit="g"),
            Ingredient(name="Caesar-Dressing", ingredient_type=condiments_sauces_type, quantity_in_stock=4000, unit="g"),
            Ingredient(name="Blue-Cheese-Dressing", ingredient_type=condiments_sauces_type, quantity_in_stock=4000, unit="g"),
            Ingredient(name="Pesto-Basil", ingredient_type=condiments_sauces_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Pesto-Sun-Dried-Tomato", ingredient_type=condiments_sauces_type, quantity_in_stock=3000, unit="g"),
            Ingredient(name="Teriyaki-Sauce", ingredient_type=condiments_sauces_type, quantity_in_stock=4000, unit="g"),
            Ingredient(name="Chimichurri", ingredient_type=condiments_sauces_type, quantity_in_stock=4000, unit="g"),
            Ingredient(name="Salsa-Mild", ingredient_type=condiments_sauces_type, quantity_in_stock=4000, unit="g"),
            Ingredient(name="Salsa-Hot", ingredient_type=condiments_sauces_type, quantity_in_stock=4000, unit="g"),
            Ingredient(name="Salsa-Pico-de-Gallo", ingredient_type=condiments_sauces_type, quantity_in_stock=4000, unit="g"),
            Ingredient(name="Guacamole", ingredient_type=condiments_sauces_type, quantity_in_stock=4000, unit="g"),
            Ingredient(name="Tahini", ingredient_type=condiments_sauces_type, quantity_in_stock=4000, unit="g"),
            Ingredient(name="Tomato-Sauce", ingredient_type=condiments_sauces_type, quantity_in_stock=4000, unit="g"),
            Ingredient(name="Marinara-Sauce", ingredient_type=condiments_sauces_type, quantity_in_stock=4000, unit="g"),
            Ingredient(name="Sriracha-Sauce", ingredient_type=condiments_sauces_type, quantity_in_stock=4000, unit="g"),
            Ingredient(name="Tahini-Sauce", ingredient_type=condiments_sauces_type, quantity_in_stock=4000, unit="g"),
            Ingredient(name="Tzatziki-Sauce", ingredient_type=condiments_sauces_type, quantity_in_stock=4000, unit="g"),
            Ingredient(name="Fish-Sauce", ingredient_type=condiments_sauces_type, quantity_in_stock=4000, unit="g"),
            Ingredient(name="Fig-Jam", ingredient_type=condiments_sauces_type, quantity_in_stock=4000, unit="g"),

            # legumes and pulses
            Ingredient(name="Lentil", ingredient_type=legumes_pulses_type, quantity_in_stock=10000, unit="g"),
            Ingredient(name="Lentils-Green", ingredient_type=legumes_pulses_type, quantity_in_stock=10000, unit="g"),
            Ingredient(name="Lentils-Brown", ingredient_type=legumes_pulses_type, quantity_in_stock=10000, unit="g"),
            Ingredient(name="Chickpeas-Garbanzo-Beans", ingredient_type=legumes_pulses_type, quantity_in_stock=8000, unit="g"),
            Ingredient(name="Black-Beans", ingredient_type=legumes_pulses_type, quantity_in_stock=8000, unit="g"),
            Ingredient(name="Kidney-Beans", ingredient_type=legumes_pulses_type, quantity_in_stock=8000, unit="g"),
            Ingredient(name="Pinto-Beans", ingredient_type=legumes_pulses_type, quantity_in_stock=8000, unit="g"),
            Ingredient(name="Navy-Beans", ingredient_type=legumes_pulses_type, quantity_in_stock=8000, unit="g"),
            Ingredient(name="Cannellini-Beans", ingredient_type=legumes_pulses_type, quantity_in_stock=8000, unit="g"),
            Ingredient(name="Split-Peas", ingredient_type=legumes_pulses_type, quantity_in_stock=8000, unit="g"),
            Ingredient(name="Soybeans", ingredient_type=legumes_pulses_type, quantity_in_stock=8000, unit="g"),
            Ingredient(name="Edamame", ingredient_type=legumes_pulses_type, quantity_in_stock=8000, unit="g"),

            # sweetners and backing_essentials
            Ingredient(name="Sugar", ingredient_type=sweeteners_baking_essentials_type, quantity_in_stock=10000, unit="g"),
            Ingredient(name="Sugar-Brown", ingredient_type=sweeteners_baking_essentials_type, quantity_in_stock=10000, unit="g"),
            Ingredient(name="Sugar-Powdered", ingredient_type=sweeteners_baking_essentials_type, quantity_in_stock=10000, unit="g"),
            Ingredient(name="Honey", ingredient_type=sweeteners_baking_essentials_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Maple-Syrup", ingredient_type=sweeteners_baking_essentials_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Molasses", ingredient_type=sweeteners_baking_essentials_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Agave-Syrup", ingredient_type=sweeteners_baking_essentials_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Cornstarch", ingredient_type=sweeteners_baking_essentials_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Baking-Powder", ingredient_type=sweeteners_baking_essentials_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Baking-Soda", ingredient_type=sweeteners_baking_essentials_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Vanilla-Extract", ingredient_type=sweeteners_baking_essentials_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Cocoa-Powder", ingredient_type=sweeteners_baking_essentials_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Chocolate-Chips", ingredient_type=sweeteners_baking_essentials_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Marshmallows", ingredient_type=sweeteners_baking_essentials_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Almond-Flour", ingredient_type=sweeteners_baking_essentials_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="All-Purpose-Flour", ingredient_type=sweeteners_baking_essentials_type, quantity_in_stock=10000, unit="g"),
            Ingredient(name="Whole-Wheat-Flour", ingredient_type=sweeteners_baking_essentials_type, quantity_in_stock=10000, unit="g"),
            Ingredient(name="Yeast", ingredient_type=sweeteners_baking_essentials_type, quantity_in_stock=10000, unit="g"),
            
            # nuts and seeds
            Ingredient(name="Almonds-Whole", ingredient_type=nuts_seeds_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Almonds-Sliced", ingredient_type=nuts_seeds_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Almonds-Chopped", ingredient_type=nuts_seeds_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Walnuts", ingredient_type=nuts_seeds_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Cashews", ingredient_type=nuts_seeds_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Pecans", ingredient_type=nuts_seeds_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Hazelnuts", ingredient_type=nuts_seeds_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Pistachios", ingredient_type=nuts_seeds_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Sunflower-Seeds", ingredient_type=nuts_seeds_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Pumpkin-Seeds", ingredient_type=nuts_seeds_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Flaxseeds", ingredient_type=nuts_seeds_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Chia-Seeds", ingredient_type=nuts_seeds_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Sesame-Seeds", ingredient_type=nuts_seeds_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Pine-Nuts", ingredient_type=nuts_seeds_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Macadamia-Nuts", ingredient_type=nuts_seeds_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Peanuts", ingredient_type=nuts_seeds_type, quantity_in_stock=5000, unit="g"),

            # frozen foods
            Ingredient(name="Frozen-Vegetables-Peas", ingredient_type=frozen_foods_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Frozen-Vegetables-Mixed", ingredient_type=frozen_foods_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Frozen-Vegetables-Spinach", ingredient_type=frozen_foods_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Frozen-Berries-Strawberries", ingredient_type=frozen_foods_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Frozen-Berries-Blueberries", ingredient_type=frozen_foods_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Frozen-French-Fries", ingredient_type=frozen_foods_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Frozen-Pizza", ingredient_type=frozen_foods_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Frozen-Chicken-Nuggets", ingredient_type=frozen_foods_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Frozen-Waffles", ingredient_type=frozen_foods_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Frozen-Dumplings", ingredient_type=frozen_foods_type, quantity_in_stock=5000, unit="g"),

            # beverages
            Ingredient(name="Coffee-Ground", ingredient_type=beverages_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Coffee-Whole-Bean", ingredient_type=beverages_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Tea-Black", ingredient_type=beverages_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Tea-Green", ingredient_type=beverages_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Tea-Herbal", ingredient_type=beverages_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Soda-Cola", ingredient_type=beverages_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Soda-Lemonade", ingredient_type=beverages_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Soda-Ginger-Ale", ingredient_type=beverages_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Orange-Juice", ingredient_type=beverages_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Apple-Juice", ingredient_type=beverages_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Cranberry-Juice", ingredient_type=beverages_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Iced-Tea", ingredient_type=beverages_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Bottled-Water", ingredient_type=beverages_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Wine-Red", ingredient_type=beverages_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Wine-White", ingredient_type=beverages_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Wine-Rosé", ingredient_type=beverages_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Beer", ingredient_type=beverages_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Liquor-Vodka", ingredient_type=beverages_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Liquor-Rum", ingredient_type=beverages_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Liquor-Whiskey", ingredient_type=beverages_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Liquor-Tequila", ingredient_type=beverages_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Cocktail-Mixes-Margarita", ingredient_type=beverages_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Cocktail-Mixes-Mojito", ingredient_type=beverages_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Coconut-Milk", ingredient_type=beverages_type, quantity_in_stock=5000, unit="g"),
            Ingredient(name="Coke", ingredient_type=beverages_type, quantity_in_stock=500, unit="pcs"),
            Ingredient(name="Sprite", ingredient_type=beverages_type, quantity_in_stock=500, unit="pcs"),
            Ingredient(name="Ginger Ale", ingredient_type=beverages_type, quantity_in_stock=500, unit="pcs"),
            Ingredient(name="Root Beer", ingredient_type=beverages_type, quantity_in_stock=500, unit="pcs"),
            Ingredient(name="Lemonade", ingredient_type=beverages_type, quantity_in_stock=500, unit="pcs"),
            Ingredient(name="Herbal-Tea-Bag", ingredient_type=beverages_type, quantity_in_stock=500, unit="pcs"),

            
            # ice creame
            Ingredient(name="Vanilla Ice Cream", ingredient_type=beverages_type, quantity_in_stock=2000, unit="g"),
            Ingredient(name="Chocolate Ice Cream", ingredient_type=beverages_type, quantity_in_stock=2000, unit="g"),
            Ingredient(name="Strawberry Ice Cream", ingredient_type=beverages_type, quantity_in_stock=2000, unit="g"),
            Ingredient(name="Mint Chocolate Chip", ingredient_type=beverages_type, quantity_in_stock=2000, unit="g"),
            Ingredient(name="Rocky Road Ice Cream", ingredient_type=beverages_type, quantity_in_stock=2000, unit="g"),
        
        
        ]

        # Bulk create the ingredients
        Ingredient.objects.bulk_create(ingredients)

        self.stdout.write(self.style.SUCCESS("Ingredient data populated successfully!"))
        # Add tags to ingredients
