
desserts=['ice_cream', 'cookies', 'cakes']

#dictionary and list of the dessert and dessert flavor
def list_ingredients_desserts():
    desserts = {
        'cakes': {
            'chocolate_cake': ['Flour', 'Sugar', 'Unsweetened cocoa powder', 'Baking powder', 'Baking soda', 'Salt', 'Espresso powder', 'Milk', 'Oil', 'Eggs', 'Vanilla', 'Water', 'https://addapinch.com/the-best-chocolate-cake-recipe-ever/'],
            'red_velvet': ['Flour', 'Baking soda', 'Cocoa powder', 'Salt', 'Unsalted butter', 'Sugar', 'Oil', 'Eggs', 'Vanilla', 'White vinegar', 'Red food coloring', 'Buttermilk', 'https://sallysbakingaddiction.com/red-velvet-layer-cake-with-cream-cheese-frosting/'],
            'cheesecake': ['Graham cracker crumbs', 'Sugar', 'Brown sugar', 'Butter', 'Cream cheese', 'Sour cream', 'Vanilla', 'Salt', 'Eggs', 'https://sugarspunrun.com/best-cheesecake-recipe/']
        },
        'cookies': {
            'chocolate_chip_cookies': ['Butter', 'White sugar', 'Brown sugar', 'Flour', 'Sea salt', 'Chocolate chips', 'https://joyfoodsunshine.com/the-most-amazing-chocolate-chip-cookies/'],
            'snickerdoodle': ['Flour', 'Cream of tartar', 'Baking soda', 'Salt', 'Unsalted butter', 'Sugar', 'Eggs', 'Vanilla extract', 'Cinnamon', 'https://lilluna.com/snickerdoodles/'],
            'lemon_crinkle': ['Butter', 'Sugar', 'Vanilla', 'Egg', 'Lemon Zest', 'Lemon juice', 'Salt', 'Baking powder', 'Baking soda', 'Flour', 'Powdered sugar', 'https://laurenslatest.com/lemon-crinkle-cookies/']
        },
        'ice_cream': {
            'chocolate_ice_cream': ['Heavy cream', 'Cocoa powder', 'Semisweet chocolate', 'Whole milk', 'Granulated sugar', 'Egg yolks', 'Vanilla extract', 'https://joyfoodsunshine.com/chocolate-ice-cream/'],
            'vanilla': ['Heavy cream', 'Half-and-half cream', 'Sugar', 'Vanilla extract', 'https://www.tasteofhome.com/recipes/homemade-vanilla-ice-cream/'],
            'strawberry': ['Heavy cream', 'Half-and-half cream', 'Sugar', 'Vanilla extract', 'Strawberries', 'Honey', 'Lemon juice', 'https://www.alattefood.com/homemade-strawberry-ice-cream/']
        }
    }
#asking for the type of dessert through input()
    dessert_type = input("Enter the type of dessert (cakes, cookies, or ice_cream): ")
#asking about what type of flavor of dessert using if/else statement and bool
    if dessert_type == 'cakes':
        flavor = input("Enter the flavor of cakes (chocolate_cake, red_velvet, cheesecake): ")
    elif dessert_type == 'cookies':
        flavor = input("Enter the flavor of cookies (chocolate_chip_cookies, snickerdoodle, lemon_crinkle): ")
    elif dessert_type == 'ice_cream':
        flavor = input("Enter the flavor of ice cream (chocolate_ice_cream, vanilla, strawberry): ")
    else:
        print("Invalid dessert type")
        return
#makes sure that the flavor is in the specified dessert and print out the ingrediants
#for loop to print out ingrediants
    if dessert_type in desserts and flavor in desserts[dessert_type]:
        ingredients = desserts[dessert_type][flavor]
        print(f"The ingredients for {flavor} {dessert_type} are:")
        for ingredient in ingredients:
            print(ingredient)
    else:
        return("Invalid dessert")
    
#using variables and expressions to calculate serving size and amount of ingrediants. Casting actual_servings from int to float.
#Using logical equiv and assert statement at the end to correctly give correct ratio of ingrediants
    wanted_servings = float(input("Enter the number of servings you want to make: "))
    if dessert_type == 'cakes' and flavor == 'chocolate_cake':
        actual_servings=24
    elif dessert_type == 'cakes' and flavor == 'red_velvet':
        actual_servings=12
    elif dessert_type == 'cakes' and flavor == 'cheesecake':
        actual_servings=12
    elif dessert_type == 'cookies' and flavor == 'chocolate_chip_cookies':
        actual_servings=36
    elif dessert_type == 'cookies' and flavor == 'snickerdoodle':
        actual_servings=36
    elif dessert_type == 'cookies' and flavor == 'lemon_crinkle':
        actual_servings=24
    elif dessert_type == 'ice_cream' and flavor == 'chocolate_ice_cream':
        actual_servings=12
    elif dessert_type == 'ice_cream' and flavor == 'vanilla':
        actual_servings=10
    elif dessert_type == 'ice_cream' and flavor == 'strawberry':
        actual_servings=6
    else :
        print("Invalid dessert type or flavor")
    assert wanted_servings > 0, "Number of servings must be more than 0"
    ratio = float(wanted_servings)/float(actual_servings)
    return (print(f'Please multiply ingredient quantity by: {ratio}'))




list_ingredients_desserts()