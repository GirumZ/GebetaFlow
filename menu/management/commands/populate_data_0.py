from django.core.management.base import BaseCommand
from menu.models import Category, Section, MenuItem

class Command(BaseCommand):
    help = "Populate the database with initial menu data"

    def handle(self, *args, **options):
        # Create categories
        main_course = Category.objects.create(name="Main Course", description="Dishes that make up the main portion of a meal, including various types of entrees and heavier fare.")
        appetizers = Category.objects.create(name="Appetizers", description="Small dishes served before the main course, perfect for starting the meal or sharing with others.")
        desserts = Category.objects.create(name="Desserts", description="Sweet treats and confections served at the end of a meal, including cakes, pastries, and ice creams.")
        beverages = Category.objects.create(name="Beverages", description="A selection of drinks, both hot and cold, including soft drinks, juices, teas, and coffee.")
        salads = Category.objects.create(name="Salads", description="Fresh and healthy salads made with a variety of greens, vegetables, and dressings.")
        sides = Category.objects.create(name="Sides", description="Smaller dishes to complement the main course, including fries, rice, and other side items.")

        # Create sections for Main Course
        pasta_section = Section.objects.create(name="Pasta", category=main_course, description="A variety of pasta dishes featuring classic Italian recipes, rich sauces, and fresh ingredients.")
        chicken_section = Section.objects.create(name="Chicken Dishes", category=main_course, description="Succulent chicken dishes prepared in various styles, from grilled and roasted to spiced and fried.")
        seafood_section = Section.objects.create(name="Seafood", category=main_course, description="Fresh and flavorful seafood options, including fish, shrimp, and shellfish prepared in diverse culinary styles.")
        steaks_section = Section.objects.create(name="Steaks", category=main_course, description="Juicy, hand-cut steaks cooked to perfection, with options for different cuts and accompanying sauces.")
        vegan_section = Section.objects.create(name="Vegan & Vegetarian", category=main_course, description="Plant-based main courses featuring fresh vegetables, legumes, and grains, suitable for vegan and vegetarian diets.")
        international_section = Section.objects.create(name="International Cuisine", category=main_course, description="A rotation of globally inspired dishes, from curries and stir-fries to Mediterranean and Latin American specialties.")
        grilled_section = Section.objects.create(name="Grilled Favorites", category=main_course, description="Hearty dishes from the grill, including grilled meats, skewers, and barbecue specials.")
        comfort_section = Section.objects.create(name="Comfort Classics", category=main_course, description="Comfort foods like pot pies, casseroles, and classic dishes with a homestyle feel.")
        pizzas_section = Section.objects.create(name="Pizzas", category=main_course, description="Artisan pizzas with a variety of toppings, from classic margherita to more creative combinations.")
        tacos_section = Section.objects.create(name="Tacos & Wraps", category=main_course, description="Delicious tacos and wraps filled with spiced meats, veggies, and sauces for a satisfying bite.")
        burgers_section = Section.objects.create(name="Burgers", category=main_course, description="Gourmet and classic burgers with a range of toppings, from cheese and bacon to avocado and specialty sauces.")
        chefs_specials_section = Section.objects.create(name="Chef's Specials", category=main_course, description="Exclusive dishes crafted by our chef, rotating based on seasonality and inspiration.")

        # Create sections for Appetizers
        appetizers_salads_section = Section.objects.create(name="Salads", category=appetizers, description="Fresh salads made with crisp greens, vegetables, and a variety of dressings.")
        finger_foods_section = Section.objects.create(name="Finger Foods", category=appetizers, description="Small, easy-to-eat dishes perfect for sharing or as starters.")

        # Create sections for Desserts
        ice_cream_section = Section.objects.create(name="Ice Cream", category=desserts, description="A variety of delicious ice creams in multiple flavors.")
        pastries_section = Section.objects.create(name="Pastries", category=desserts, description="Sweet pastries and desserts baked to perfection.")

        # Create sections for Beverages
        soft_drinks_section = Section.objects.create(name="Soft Drinks", category=beverages, description="A selection of carbonated and non-carbonated soft drinks.")
        hot_drinks_section = Section.objects.create(name="Hot Drinks", category=beverages, description="Coffee, tea, and other hot beverage options.")

        # Create sections for Salads
        leafy_greens_section = Section.objects.create(name="Leafy Greens", category=salads, description="Salads featuring a variety of fresh leafy greens.")
        protein_salads_section = Section.objects.create(name="Protein Salads", category=salads, description="Salads enriched with protein sources like chicken, tofu, or beans.")

        # Create sections for Sides
        fries_section = Section.objects.create(name="Fries", category=sides, description="Crispy and golden fries, perfect as a side dish.")
        rice_grains_section = Section.objects.create(name="Rice & Grains", category=sides, description="Delicious rice and grain options to accompany your meal.")

        # Create MenuItems for the Main Course Category and all its sections

        # Pasta Section
        MenuItem.objects.create(name="Spaghetti Carbonara", price=11.99, description="Classic Italian pasta with egg, cheese, and pancetta.", section=pasta_section, category=main_course)
        MenuItem.objects.create(name="Fettuccine Alfredo", price=12.99, description="Creamy Alfredo sauce with fettuccine pasta.", section=pasta_section, category=main_course)
        MenuItem.objects.create(name="Penne Arrabbiata", price=10.49, description="Spicy tomato-based sauce with penne pasta.", section=pasta_section, category=main_course)
        MenuItem.objects.create(name="Lasagna", price=13.99, description="Layered pasta with beef, ricotta, and marinara sauce.", section=pasta_section, category=main_course)
        MenuItem.objects.create(name="Ravioli", price=14.99, description="Stuffed pasta pockets with spinach and ricotta.", section=pasta_section, category=main_course)
        MenuItem.objects.create(name="Pasta Primavera", price=12.49, description="Mixed vegetables in a light garlic sauce.", section=pasta_section, category=main_course)
        MenuItem.objects.create(name="Linguine with Clams", price=15.99, description="Fresh clams in a white wine sauce.", section=pasta_section, category=main_course)
        MenuItem.objects.create(name="Tortellini Alfredo", price=13.49, description="Cheese-stuffed tortellini in Alfredo sauce.", section=pasta_section, category=main_course)
        MenuItem.objects.create(name="Pesto Penne", price=11.49, description="Penne pasta in fresh basil pesto sauce.", section=pasta_section, category=main_course)
        MenuItem.objects.create(name="Gnocchi with Marinara", price=12.99, description="Soft potato gnocchi in a rich marinara sauce.", section=pasta_section, category=main_course)

        # Chicken Dishes Section
        MenuItem.objects.create(name="Grilled Chicken Breast", price=13.99, description="Seasoned and grilled to perfection.", section=chicken_section, category=main_course)
        MenuItem.objects.create(name="Chicken Parmesan", price=15.99, description="Breaded chicken breast with marinara and mozzarella.", section=chicken_section, category=main_course)
        MenuItem.objects.create(name="Honey Garlic Chicken", price=14.49, description="Chicken breast in a honey garlic glaze.", section=chicken_section, category=main_course)
        MenuItem.objects.create(name="Lemon Herb Chicken", price=13.49, description="Chicken breast marinated in lemon and herbs.", section=chicken_section, category=main_course)
        MenuItem.objects.create(name="Chicken Marsala", price=16.49, description="Pan-fried chicken with a Marsala wine sauce.", section=chicken_section, category=main_course)
        MenuItem.objects.create(name="BBQ Chicken Thighs", price=13.99, description="Chicken thighs with smoky BBQ sauce.", section=chicken_section, category=main_course)
        MenuItem.objects.create(name="Butter Chicken", price=15.49, description="Indian-style chicken in a creamy spiced sauce.", section=chicken_section, category=main_course)
        MenuItem.objects.create(name="Cajun Chicken", price=13.99, description="Spicy Cajun-seasoned grilled chicken.", section=chicken_section, category=main_course)
        MenuItem.objects.create(name="Chicken Tikka Masala", price=15.99, description="Marinated chicken in a spiced tomato sauce.", section=chicken_section, category=main_course)
        MenuItem.objects.create(name="Stuffed Chicken Breast", price=16.99, description="Chicken breast stuffed with spinach and cheese.", section=chicken_section, category=main_course)

        # Seafood Section
        MenuItem.objects.create(name="Grilled Salmon", price=18.99, description="Fresh salmon fillet grilled to perfection with a lemon butter sauce.", section=seafood_section, category=main_course)
        MenuItem.objects.create(name="Fish & Chips", price=15.49, description="Crispy battered fish served with fries and tartar sauce.", section=seafood_section, category=main_course)
        MenuItem.objects.create(name="Shrimp Scampi", price=17.99, description="Shrimp in a garlic butter sauce over linguine.", section=seafood_section, category=main_course)
        MenuItem.objects.create(name="Seafood Paella", price=19.99, description="Traditional Spanish rice dish with assorted seafood.", section=seafood_section, category=main_course)
        MenuItem.objects.create(name="Crab Cakes", price=16.49, description="Homemade crab cakes served with remoulade sauce.", section=seafood_section, category=main_course)
        MenuItem.objects.create(name="Lobster Tail", price=24.99, description="Grilled lobster tail with garlic herb butter.", section=seafood_section, category=main_course)
        MenuItem.objects.create(name="Clam Chowder", price=9.99, description="Creamy New England-style clam chowder.", section=seafood_section, category=main_course)
        MenuItem.objects.create(name="Grilled Shrimp Skewers", price=14.99, description="Shrimp skewers marinated and grilled.", section=seafood_section, category=main_course)
        MenuItem.objects.create(name="Mussels in White Wine", price=15.99, description="Steamed mussels in a white wine and garlic sauce.", section=seafood_section, category=main_course)
        MenuItem.objects.create(name="Seafood Risotto", price=18.49, description="Creamy risotto with a variety of seafood.", section=seafood_section, category=main_course)

        # Steaks Section
        MenuItem.objects.create(name="Filet Mignon", price=28.99, description="Tender cut of beef cooked to your preference.", section=steaks_section, category=main_course)
        MenuItem.objects.create(name="Ribeye Steak", price=26.99, description="Juicy ribeye grilled with a seasoned crust.", section=steaks_section, category=main_course)
        MenuItem.objects.create(name="T-Bone Steak", price=29.99, description="Classic T-bone steak for a hearty meal.", section=steaks_section, category=main_course)
        MenuItem.objects.create(name="Sirloin Steak", price=22.99, description="Lean sirloin steak, grilled to your liking.", section=steaks_section, category=main_course)
        MenuItem.objects.create(name="Steak Diane", price=27.49, description="Filet medallions with a creamy mushroom sauce.", section=steaks_section, category=main_course)
        MenuItem.objects.create(name="Steak Frites", price=24.99, description="Grilled steak served with crispy fries.", section=steaks_section, category=main_course)
        MenuItem.objects.create(name="New York Strip", price=25.99, description="Classic cut with great flavor and marbling.", section=steaks_section, category=main_course)
        MenuItem.objects.create(name="Bistro Steak", price=23.99, description="Seared steak topped with herb butter.", section=steaks_section, category=main_course)
        MenuItem.objects.create(name="Surf & Turf", price=32.99, description="Filet with lobster tail for a seafood and steak combo.", section=steaks_section, category=main_course)
        MenuItem.objects.create(name="Peppercorn Steak", price=26.99, description="Steak with a rich peppercorn sauce.", section=steaks_section, category=main_course)

        # Vegan & Vegetarian Section
        MenuItem.objects.create(name="Vegan Buddha Bowl", price=12.99, description="Healthy bowl with quinoa, veggies, and chickpeas.", section=vegan_section, category=main_course)
        MenuItem.objects.create(name="Vegetable Stir-Fry", price=11.49, description="Fresh vegetables stir-fried with tofu and sauce.", section=vegan_section, category=main_course)
        MenuItem.objects.create(name="Mushroom Risotto", price=13.49, description="Creamy risotto with mushrooms.", section=vegan_section, category=main_course)
        MenuItem.objects.create(name="Vegan Burrito", price=10.99, description="Tortilla filled with rice, beans, and veggies.", section=vegan_section, category=main_course)
        MenuItem.objects.create(name="Falafel Plate", price=12.49, description="Homemade falafel served with hummus and pita.", section=vegan_section, category=main_course)
        MenuItem.objects.create(name="Stuffed Bell Peppers", price=13.49, description="Peppers filled with rice and vegetables.", section=vegan_section, category=main_course)
        MenuItem.objects.create(name="Eggplant Parmesan", price=14.99, description="Baked eggplant with marinara and mozzarella.", section=vegan_section, category=main_course)
        MenuItem.objects.create(name="Chickpea Curry", price=12.49, description="Spicy chickpea curry with rice.", section=vegan_section, category=main_course)
        MenuItem.objects.create(name="Lentil Shepherd’s Pie", price=14.49, description="Mashed potatoes over savory lentils and veggies.", section=vegan_section, category=main_course)
        MenuItem.objects.create(name="Vegan Mac & Cheese", price=10.99, description="Macaroni with a dairy-free cheese sauce.", section=vegan_section, category=main_course)

        # International Cuisine Section
        MenuItem.objects.create(name="Beef Bulgogi", price=16.49, description="Korean marinated beef with rice.", section=international_section, category=main_course)
        MenuItem.objects.create(name="Chicken Tikka", price=15.49, description="Indian spiced chicken with naan bread.", section=international_section, category=main_course)
        MenuItem.objects.create(name="Pad Thai", price=13.99, description="Thai rice noodles with shrimp.", section=international_section, category=main_course)
        MenuItem.objects.create(name="Gyro Plate", price=12.99, description="Greek gyro with pita and tzatziki.", section=international_section, category=main_course)
        MenuItem.objects.create(name="Sushi Platter", price=19.99, description="Japanese sushi assortment.", section=international_section, category=main_course)
        MenuItem.objects.create(name="Chicken Shawarma", price=14.99, description="Middle Eastern wrap with pickled veggies.", section=international_section, category=main_course)
        MenuItem.objects.create(name="Banh Mi", price=11.49, description="Vietnamese sandwich with pork and pickled veggies.", section=international_section, category=main_course)
        MenuItem.objects.create(name="Paella", price=18.99, description="Spanish rice with seafood and sausage.", section=international_section, category=main_course)

        # Grilled Favorites Section
        MenuItem.objects.create(name="BBQ Ribs", price=19.99, description="Tender ribs with a smoky BBQ glaze.", section=grilled_section, category=main_course)
        MenuItem.objects.create(name="Grilled Lamb Chops", price=24.99, description="Marinated lamb chops with a rosemary garlic rub.", section=grilled_section, category=main_course)
        MenuItem.objects.create(name="Pork Belly Skewers", price=13.99, description="Juicy pork belly skewers with a tangy sauce.", section=grilled_section, category=main_course)
        MenuItem.objects.create(name="Grilled Chicken Wings", price=11.49, description="Classic wings with BBQ or spicy sauce.", section=grilled_section, category=main_course)
        MenuItem.objects.create(name="Grilled Vegetable Platter", price=10.99, description="Assorted vegetables grilled with herbs.", section=grilled_section, category=main_course)
        MenuItem.objects.create(name="BBQ Brisket", price=18.49, description="Slow-cooked brisket with BBQ sauce.", section=grilled_section, category=main_course)
        MenuItem.objects.create(name="Grilled Shrimp Kabobs", price=14.99, description="Skewered shrimp with garlic butter.", section=grilled_section, category=main_course)
        MenuItem.objects.create(name="Grilled Sausages", price=12.99, description="Assorted sausages with grilled onions.", section=grilled_section, category=main_course)
        MenuItem.objects.create(name="Beef Skewers", price=15.49, description="Marinated beef skewers served with tzatziki.", section=grilled_section, category=main_course)
        MenuItem.objects.create(name="Grilled Portobello Mushrooms", price=11.99, description="Marinated mushrooms grilled to perfection.", section=grilled_section, category=main_course)

        # Comfort Classics Section
        MenuItem.objects.create(name="Chicken Pot Pie", price=12.99, description="Classic pot pie with chicken and vegetables.", section=comfort_section, category=main_course)
        MenuItem.objects.create(name="Mac & Cheese", price=9.99, description="Creamy mac & cheese with a crispy top.", section=comfort_section, category=main_course)
        MenuItem.objects.create(name="Beef Stew", price=13.99, description="Slow-cooked stew with tender beef and veggies.", section=comfort_section, category=main_course)
        MenuItem.objects.create(name="Shepherd's Pie", price=12.49, description="Mashed potatoes over a savory meat filling.", section=comfort_section, category=main_course)
        MenuItem.objects.create(name="Meatloaf", price=11.99, description="Classic meatloaf with a sweet glaze.", section=comfort_section, category=main_course)
        MenuItem.objects.create(name="Baked Ziti", price=12.49, description="Pasta baked with marinara, meat, and cheese.", section=comfort_section, category=main_course)
        MenuItem.objects.create(name="Chicken Fried Steak", price=13.99, description="Breaded steak with country gravy.", section=comfort_section, category=main_course)
        MenuItem.objects.create(name="Mashed Potatoes & Gravy", price=6.99, description="Creamy mashed potatoes with brown gravy.", section=comfort_section, category=main_course)
        MenuItem.objects.create(name="Beef Lasagna", price=13.99, description="Layers of pasta, beef, and cheese.", section=comfort_section, category=main_course)
        MenuItem.objects.create(name="Classic Chili", price=9.99, description="Hearty chili with beans and ground beef.", section=comfort_section, category=main_course)

        # Pizzas Section
        MenuItem.objects.create(name="Margherita Pizza", price=10.99, description="Classic pizza with mozzarella, tomato, and basil.", section=pizzas_section, category=main_course)
        MenuItem.objects.create(name="Pepperoni Pizza", price=11.99, description="Pizza topped with pepperoni slices.", section=pizzas_section, category=main_course)
        MenuItem.objects.create(name="BBQ Chicken Pizza", price=12.49, description="Pizza with BBQ chicken and red onions.", section=pizzas_section, category=main_course)
        MenuItem.objects.create(name="Four Cheese Pizza", price=13.49, description="Pizza with mozzarella, cheddar, parmesan, and blue cheese.", section=pizzas_section, category=main_course)
        MenuItem.objects.create(name="Hawaiian Pizza", price=11.99, description="Pizza with ham and pineapple.", section=pizzas_section, category=main_course)
        MenuItem.objects.create(name="Veggie Pizza", price=12.49, description="Pizza topped with assorted vegetables.", section=pizzas_section, category=main_course)
        MenuItem.objects.create(name="Meat Lovers Pizza", price=14.49, description="Loaded with pepperoni, sausage, and bacon.", section=pizzas_section, category=main_course)
        MenuItem.objects.create(name="White Pizza", price=13.99, description="Pizza with ricotta, mozzarella, and garlic.", section=pizzas_section, category=main_course)
        MenuItem.objects.create(name="Mushroom Pizza", price=12.99, description="Pizza with fresh mushrooms.", section=pizzas_section, category=main_course)
        MenuItem.objects.create(name="Buffalo Chicken Pizza", price=12.99, description="Pizza with spicy buffalo chicken and ranch.", section=pizzas_section, category=main_course)

        # Tacos & Wraps Section
        MenuItem.objects.create(name="Chicken Tacos", price=9.99, description="Tacos with shredded chicken and toppings.", section=tacos_section, category=main_course)
        MenuItem.objects.create(name="Beef Tacos", price=10.99, description="Tacos filled with seasoned ground beef.", section=tacos_section, category=main_course)
        MenuItem.objects.create(name="Fish Tacos", price=11.99, description="Tacos with fried fish and slaw.", section=tacos_section, category=main_course)
        MenuItem.objects.create(name="Shrimp Tacos", price=12.49, description="Tacos with grilled shrimp and spicy sauce.", section=tacos_section, category=main_course)
        MenuItem.objects.create(name="Vegan Tacos", price=10.49, description="Plant-based tacos with beans and veggies.", section=tacos_section, category=main_course)
        MenuItem.objects.create(name="Steak Tacos", price=12.99, description="Tacos with marinated steak and salsa.", section=tacos_section, category=main_course)
        MenuItem.objects.create(name="Pulled Pork Wrap", price=11.49, description="Wrap with pulled pork and BBQ sauce.", section=tacos_section, category=main_course)
        MenuItem.objects.create(name="Falafel Wrap", price=9.99, description="Wrap with falafel and tzatziki sauce.", section=tacos_section, category=main_course)
        MenuItem.objects.create(name="Buffalo Chicken Wrap", price=11.49, description="Wrap with buffalo chicken and ranch.", section=tacos_section, category=main_course)
        MenuItem.objects.create(name="Mediterranean Wrap", price=10.49, description="Wrap with hummus, veggies, and feta cheese.", section=tacos_section, category=main_course)

        # Burgers Section
        MenuItem.objects.create(name="Classic Cheeseburger", price=11.49, description="Beef patty with cheese, lettuce, and tomato.", section=burgers_section, category=main_course)
        MenuItem.objects.create(name="Bacon Burger", price=12.99, description="Burger topped with crispy bacon.", section=burgers_section, category=main_course)
        MenuItem.objects.create(name="BBQ Burger", price=13.49, description="Burger with BBQ sauce and fried onions.", section=burgers_section, category=main_course)
        MenuItem.objects.create(name="Mushroom Swiss Burger", price=13.99, description="Burger topped with mushrooms and Swiss cheese.", section=burgers_section, category=main_course)
        MenuItem.objects.create(name="Veggie Burger", price=10.99, description="Plant-based burger patty with toppings.", section=burgers_section, category=main_course)
        MenuItem.objects.create(name="Avocado Burger", price=12.49, description="Burger topped with fresh avocado.", section=burgers_section, category=main_course)
        MenuItem.objects.create(name="Spicy Jalapeño Burger", price=12.99, description="Burger with jalapeños and pepper jack cheese.", section=burgers_section, category=main_course)
        MenuItem.objects.create(name="Double Cheeseburger", price=14.99, description="Burger with two beef patties and cheese.", section=burgers_section, category=main_course)
        MenuItem.objects.create(name="Teriyaki Burger", price=12.49, description="Burger with teriyaki sauce and pineapple.", section=burgers_section, category=main_course)
        MenuItem.objects.create(name="Black & Blue Burger", price=13.49, description="Burger with blue cheese and blackened seasoning.", section=burgers_section, category=main_course)

        # Chef's Specials Section
        MenuItem.objects.create(name="Duck Confit", price=25.99, description="Tender duck leg slow-cooked in its own fat.", section=chefs_specials_section, category=main_course)
        MenuItem.objects.create(name="Rack of Lamb", price=29.99, description="Grilled lamb rack with herb crust.", section=chefs_specials_section, category=main_course)
        MenuItem.objects.create(name="Sea Bass with Lemon Caper Sauce", price=27.99, description="Pan-seared sea bass with a tangy sauce.", section=chefs_specials_section, category=main_course)
        MenuItem.objects.create(name="Wagyu Steak", price=39.99, description="Premium wagyu steak, cooked to perfection.", section=chefs_specials_section, category=main_course)
        MenuItem.objects.create(name="Truffle Risotto", price=22.99, description="Creamy risotto with truffle oil.", section=chefs_specials_section, category=main_course)
        MenuItem.objects.create(name="Foie Gras", price=31.99, description="Delicate foie gras served with fruit compote.", section=chefs_specials_section, category=main_course)
        MenuItem.objects.create(name="Lobster Thermidor", price=34.99, description="Classic French-style lobster with a creamy sauce.", section=chefs_specials_section, category=main_course)
        MenuItem.objects.create(name="Short Rib Ravioli", price=24.49, description="Ravioli stuffed with braised short rib.", section=chefs_specials_section, category=main_course)
        MenuItem.objects.create(name="Osso Buco", price=28.99, description="Italian-style braised veal shank.", section=chefs_specials_section, category=main_course)
        MenuItem.objects.create(name="Beef Wellington", price=32.99, description="Beef tenderloin wrapped in puff pastry.", section=chefs_specials_section, category=main_course)

        # Appetizers - Salads Section
        MenuItem.objects.create(name="Caesar Salad", price=7.99, description="Crisp romaine lettuce with Caesar dressing, croutons, and Parmesan.", section=appetizers_salads_section, category=appetizers)
        MenuItem.objects.create(name="Greek Salad", price=8.49, description="Mixed greens with feta, olives, cucumber, and Greek vinaigrette.", section=appetizers_salads_section, category=appetizers)
        MenuItem.objects.create(name="Caprese Salad", price=9.49, description="Tomato, fresh mozzarella, and basil drizzled with balsamic glaze.", section=appetizers_salads_section, category=appetizers)
        MenuItem.objects.create(name="Garden Salad", price=6.99, description="Fresh lettuce, carrots, cucumber, and tomatoes with choice of dressing.", section=appetizers_salads_section, category=appetizers)
        MenuItem.objects.create(name="Asian Slaw Salad", price=7.49, description="Shredded cabbage with sesame dressing and crispy wonton strips.", section=appetizers_salads_section, category=appetizers)

        # Appetizers - Finger Foods Section
        MenuItem.objects.create(name="Mozzarella Sticks", price=6.99, description="Breaded mozzarella sticks with marinara sauce.", section=finger_foods_section, category=appetizers)
        MenuItem.objects.create(name="Stuffed Jalapeños", price=7.49, description="Jalapeños stuffed with cream cheese and wrapped in bacon.", section=finger_foods_section, category=appetizers)
        MenuItem.objects.create(name="Chicken Tenders", price=8.99, description="Crispy chicken tenders served with honey mustard.", section=finger_foods_section, category=appetizers)
        MenuItem.objects.create(name="Spring Rolls", price=5.99, description="Vegetable spring rolls with sweet chili dipping sauce.", section=finger_foods_section, category=appetizers)
        MenuItem.objects.create(name="Potato Skins", price=6.49, description="Potato halves loaded with cheese and bacon.", section=finger_foods_section, category=appetizers)

        # Desserts - Ice Cream Section
        MenuItem.objects.create(name="Vanilla Ice Cream", price=3.99, description="Classic vanilla ice cream with a creamy texture.", section=ice_cream_section, category=desserts)
        MenuItem.objects.create(name="Chocolate Ice Cream", price=3.99, description="Rich chocolate ice cream for chocolate lovers.", section=ice_cream_section, category=desserts)
        MenuItem.objects.create(name="Strawberry Ice Cream", price=3.99, description="Creamy ice cream with real strawberry pieces.", section=ice_cream_section, category=desserts)
        MenuItem.objects.create(name="Mint Chocolate Chip", price=4.49, description="Cool mint ice cream with chocolate chunks.", section=ice_cream_section, category=desserts)
        MenuItem.objects.create(name="Rocky Road", price=4.49, description="Chocolate ice cream with nuts and marshmallows.", section=ice_cream_section, category=desserts)

        # Desserts - Pastries Section
        MenuItem.objects.create(name="Chocolate Cake", price=5.99, description="Moist chocolate cake with rich frosting.", section=pastries_section, category=desserts)
        MenuItem.objects.create(name="Cheesecake", price=6.49, description="Creamy cheesecake with a graham cracker crust.", section=pastries_section, category=desserts)
        MenuItem.objects.create(name="Apple Pie", price=5.49, description="Classic apple pie with a flaky crust.", section=pastries_section, category=desserts)
        MenuItem.objects.create(name="Lemon Tart", price=5.99, description="Tangy lemon filling in a buttery tart shell.", section=pastries_section, category=desserts)
        MenuItem.objects.create(name="Éclair", price=4.99, description="Choux pastry filled with cream and topped with chocolate.", section=pastries_section, category=desserts)

        # Beverages - Soft Drinks Section
        MenuItem.objects.create(name="Coke", price=1.99, description="Classic Coca-Cola served chilled.", section=soft_drinks_section, category=beverages)
        MenuItem.objects.create(name="Sprite", price=1.99, description="Refreshing lemon-lime soda.", section=soft_drinks_section, category=beverages)
        MenuItem.objects.create(name="Ginger Ale", price=2.29, description="Zesty ginger-flavored soda.", section=soft_drinks_section, category=beverages)
        MenuItem.objects.create(name="Root Beer", price=2.29, description="Traditional root beer flavor.", section=soft_drinks_section, category=beverages)
        MenuItem.objects.create(name="Lemonade", price=2.49, description="Freshly squeezed lemonade.", section=soft_drinks_section, category=beverages)

        # Beverages - Hot Drinks Section
        MenuItem.objects.create(name="Americano", price=2.99, description="Espresso diluted with hot water.", section=hot_drinks_section, category=beverages)
        MenuItem.objects.create(name="Latte", price=3.49, description="Espresso with steamed milk.", section=hot_drinks_section, category=beverages)
        MenuItem.objects.create(name="Cappuccino", price=3.49, description="Espresso with steamed milk and foam.", section=hot_drinks_section, category=beverages)
        MenuItem.objects.create(name="Herbal Tea", price=2.49, description="A variety of caffeine-free herbal teas.", section=hot_drinks_section, category=beverages)
        MenuItem.objects.create(name="Hot Chocolate", price=2.99, description="Rich and creamy hot chocolate.", section=hot_drinks_section, category=beverages)

        # Salads - Leafy Greens Section
        MenuItem.objects.create(name="Arugula Salad", price=8.49, description="Fresh arugula with shaved Parmesan and vinaigrette.", section=leafy_greens_section, category=salads)
        MenuItem.objects.create(name="Spinach Salad", price=8.99, description="Baby spinach with strawberries and poppyseed dressing.", section=leafy_greens_section, category=salads)
        MenuItem.objects.create(name="Kale Caesar", price=9.49, description="Kale with Caesar dressing, croutons, and Parmesan.", section=leafy_greens_section, category=salads)
        MenuItem.objects.create(name="Mixed Greens", price=7.99, description="Assorted leafy greens with balsamic vinaigrette.", section=leafy_greens_section, category=salads)
        MenuItem.objects.create(name="Watercress Salad", price=8.49, description="Peppery watercress with lemon vinaigrette.", section=leafy_greens_section, category=salads)

        # Salads - Protein Salads Section
        MenuItem.objects.create(name="Chicken Caesar", price=10.99, description="Classic Caesar with grilled chicken.", section=protein_salads_section, category=salads)
        MenuItem.objects.create(name="Tuna Salad", price=11.49, description="Mixed greens with tuna and balsamic dressing.", section=protein_salads_section, category=salads)
        MenuItem.objects.create(name="Quinoa Salad", price=9.99, description="Protein-packed quinoa with veggies and herbs.", section=protein_salads_section, category=salads)
        MenuItem.objects.create(name="Tofu Salad", price=10.49, description="Crispy tofu with mixed greens and sesame dressing.", section=protein_salads_section, category=salads)
        MenuItem.objects.create(name="Shrimp Salad", price=12.49, description="Fresh shrimp with greens and mango salsa.", section=protein_salads_section, category=salads)

        # Sides - Fries Section
        MenuItem.objects.create(name="Classic French Fries", price=3.99, description="Golden, crispy French fries.", section=fries_section, category=sides)
        MenuItem.objects.create(name="Sweet Potato Fries", price=4.49, description="Crispy sweet potato fries with a hint of cinnamon.", section=fries_section, category=sides)
        MenuItem.objects.create(name="Curly Fries", price=4.29, description="Seasoned curly fries, a fun twist on a classic.", section=fries_section, category=sides)
        MenuItem.objects.create(name="Garlic Parmesan Fries", price=4.99, description="Fries tossed with garlic and Parmesan cheese.", section=fries_section, category=sides)
        MenuItem.objects.create(name="Truffle Fries", price=5.99, description="Fries with truffle oil and Parmesan.", section=fries_section, category=sides)

        # Sides - Rice & Grains Section
        MenuItem.objects.create(name="Steamed Rice", price=2.99, description="Simple, fluffy steamed rice.", section=rice_grains_section, category=sides)
        MenuItem.objects.create(name="Fried Rice", price=4.99, description="Rice stir-fried with veggies and soy sauce.", section=rice_grains_section, category=sides)
        MenuItem.objects.create(name="Quinoa Pilaf", price=5.49, description="Quinoa with veggies and herbs.", section=rice_grains_section, category=sides)
        MenuItem.objects.create(name="Couscous", price=4.99, description="Fluffy couscous with fresh herbs.", section=rice_grains_section, category=sides)
        MenuItem.objects.create(name="Barley Risotto", price=5.99, description="Creamy barley risotto with mushrooms.", section=rice_grains_section, category=sides)



        # Print success message
        self.stdout.write(self.style.SUCCESS("Categories, sections, and menu items populated successfully."))