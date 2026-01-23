recipe = {
    "pasta": 500,
    "tomatoes": 400,
    "basil": 20,
    "garlic": 15,
    "olive_oil": 30,
    "salt": 10,
}

pantry_stock = {
    "pasta": 100,
    "tomatoes": 1500,
    "basil": 20,
    "garlic": 10,
    "olive_oil": 10,
    "salt": 150,
}

# Create an empty shopping list
shopping_list = []

# Loop through each ingredient and required quantity
for ingredient, required_qty in recipe.items():
    # Check if we need more than what we have
    if required_qty > pantry_stock[ingredient]:
        # Add the ingredient to our shopping list
        shopping_list.append(ingredient)

# Display the shopping list
print("Shopping list:", shopping_list)
