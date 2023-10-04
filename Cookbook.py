

#ask which option of the three appetizers, main_course or dessert the user wants to choose 
choose_category = input("What category do you want to choose your recipe's from (appetizer, main course, or dessert): ")

#if statement 
if choose_category == 'main course':
    import main_course
elif choose_category == 'dessert':
    import dessert
elif choose_category == 'appetizer':
    import main_appetizer
else:
    print("Invalid category type")
    exit() #if it is an invalid name, it will exit out of loop


