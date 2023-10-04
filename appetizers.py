
import csv

class Appetizers_cat:
    def __init__(self, food_name, category, recipe_type, ingredients):
        self.food_name = food_name
        self.category = category
        self.recipe_type = recipe_type
        self.ingredients = ingredients
        
def read_csv(filename):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip the header row
        appetizers = []
        for row in reader:
            try:
                appetizers.append(Appetizers_cat(row[0], row[1], row[2], row[3].split(", ")))
            except IndexError:
                print(f"Skipping row {row}: not enough columns")
        return appetizers