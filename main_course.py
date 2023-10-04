
#dictionary of the recipe names and the list contains the ingrediants and link to the recipe
main_course_ingredients = {
    'salad': ['lettuce', 'tomatoes', 'cucumber', 'croutons', 'garlic', 'olive oil', 'salad dressing', 'https://natashaskitchen.com/caesar-salad-recipe/'],
    'pasta': ['pasta', 'tomato sauce', 'garlic', 'parsley', 'salt', 'ground pepper', 'olive oil', 'https://www.foodandwine.com/recipes/pasta-with-olive-oil-garlic-and-parsley'],
    'ravioli': ['flour' , 'salt' , 'eggs', 'water', 'olive oil', 'ricotta', 'cream cheese', 'mozzarella', 'tomato sauce', 'basil', 'parmesan', 'garlic', 'parsley', 'https://www.allrecipes.com/recipe/213131/homemade-four-cheese-ravioli/'],
    'chicken_parm': ['chicken breast', 'panko', 'parmesan', 'mozzarella', 'salt', 'pepper', 'egg', 'olive oil', 'basil', 'flour', 'tomato sauce', 'https://www.allrecipes.com/recipe/223042/chicken-parmesan/'],
    'risotto': ['arborio rice', 'chicken stock', 'onion', 'parmesan', 'butter', 'garlic', 'salt', 'pepper', 'parsley', 'olive oil', 'https://natashaskitchen.com/classic-risotto-recipe/'],
    'lasagna': ['meat', 'lasagna noodles', 'egg', 'ground beef', 'tomato sauce', 'mozzarella', 'parsley', 'garlic', 'onion', 'salt', 'italian seasoning', 'fennel seeds', 'black pepper', 'https://www.allrecipes.com/recipe/23600/worlds-best-lasagna/']}


#A filter added to see if the user correctly inputs vegetarian and non-vegetarian

#asking user to input either vegetrian or non-vegetarian
main_course_option = input("Enter the type of main course (vegetarian or non-vegetarian): ")


if main_course_option =='vegetarian' or main_course_option == 'non-vegetarian':
    #asking the user if they want to filter mozarella or parmesan from the recipe's
    question_filtering = input("Do you want to filter mozzarella or parmesan from the recipe's (yes or no): ") 
    if question_filtering == 'yes':
        #Choosing to find the recipe's that contain mozarella or parmesan
        cheese = input("Choose either mozzarella or parmesan: ")
           
         #dictionary and list of the recipe names and ingrediants  
        cheese_foods = {
            'salad': ['lettuce', 'tomatoes', 'cucumber', 'croutons', 'garlic', 'olive oil', 'salad dressing'],
            'pasta': ['pasta', 'tomato sauce', 'garlic', 'parsley', 'salt', 'ground pepper', 'olive oil'],
            'ravioli': [' flour' , 'salt' , 'eggs', 'water', 'olive oil', 'ricotta', 'cream cheese', 'mozzarella', 'tomato sauce', 'basil', 'parmesan', 'garlic', 'parsley'],
            'chicken_parm': ['chicken breast', 'panko', 'parmesan', 'mozzarella', 'salt', 'pepper', 'egg', 'olive oil', 'basil', 'flour', 'tomato sauce'],
            'risotto': ['arborio rice', 'chicken stock', 'onion', 'parmesan', 'butter', 'garlic', 'salt', 'pepper', 'parsley', 'olive oil'],
            'lasagna': ['meat', 'lasagna noodles', 'egg', 'ground beef', 'tomato sauce', 'mozzarella', 'parsley', 'garlic', 'onion', 'salt', 'italian seasoning', 'fennel seeds', 'black pepper']} 

        #logic of filtering mozarella/parmesan   
        filtered_cheese = [recipes for recipes, ingredients in cheese_foods.items()
        if cheese in ingredients]
        #printing the recipes that contain the chosen cheese
        print("Recipes with", cheese, ":")  
        for recipes in filtered_cheese:
            print(recipes)
    else:
        #prints if user does not want to filter
        print("Now choose your recipe") 
else:
    #prints if user did not correctly input vegetarian or non-vegetarian
    print("Main course type does not exist")
    exit()


#if statement to ask which recipe you would like either under vegetarian or non-vegetarian
if main_course_option == 'vegetarian':
    recipe_option = input("\n1) salad\n2) pasta\n3) ravioli \nEnter recipe name: ")
elif main_course_option == 'non-vegetarian':
    recipe_option = input("\n1) chicken_parm\n2) risotto\n3) lasagna \nEnter recipe name: ")
else:
    print("Invalid main course type")
    exit() #if it is an invalid name, it will exit out of loop


#given recipe options under the two main course types
if main_course_option == 'vegetarian':
    recipes_options = {'vegetarian': ['pasta', 'salad', 'ravioli']}
else:
    recipes_options = {'non-vegetarian': ['chicken_parm', 'risotto', 'lasagna']}

#if the recipe option name does not exist or spelled incorrectly, then it will print out Recipe option does not exist
if recipe_option not in recipes_options[main_course_option]:
    print("Recipe option does not exist")
    exit() 

#printing out the recipe and recipe name
print("\n\nYou have chosen the following:")
 #printing the category, recipe type, and food name
print(f"Category: main course\nRecipe Type: {main_course_option}\nFood Name: {recipe_option}\n")
#printing the recipe and ingredients
print(f"The ingredients for {recipe_option} {main_course_option} are:") 
for ingredient in main_course_ingredients[recipe_option]:
    print(ingredient)

