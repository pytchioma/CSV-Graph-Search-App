


import csv
import random

foods = [
    "Rice", "Beans", "Bread", "Chicken", "Beef", "Fish", "Egg", "Milk",
    "Cheese", "Apple", "Banana", "Orange", "Pasta", "Pizza", "Yam",
    "Potato", "Tomato", "Carrot", "Cabbage", "Pepper"
]

with open("foods_150k.csv", "w", newline="") as file:
    writer = csv.writer(file)
    
    # Header
    writer.writerow(["ID", "Food_Name", "Category", "Calories"])

    for i in range(150000):
        food = random.choice(foods)
        category = random.choice(["Fruit", "Vegetable", "Protein", "Grain"])
        calories = random.randint(50, 800)

        writer.writerow([i+1, food, category, calories])

print("CSV file with 150,000 rows created successfully!")