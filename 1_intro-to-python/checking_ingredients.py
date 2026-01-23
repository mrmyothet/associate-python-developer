pantry_stock = {"tomatoes": 500, "basil": 80, "fusilli": 1000, "garlic": 12}
ingredients_needed = {
    "fusilli": 1000,
    "tomatoes": 800,
    "basil": 40,
    "garlic": 30,
    "olive oil": 30,
    "salt": 15,
}

# Check if you have enough tomatoes for the full party
if pantry_stock["tomatoes"] >= ingredients_needed["tomatoes"]:
    print("Enough tomatoes for the party!")

# Check if you have enough for a smaller gathering
elif pantry_stock["tomatoes"] >= 800:
    print("Only enough tomatoes for a smaller gathering.")

# Handle the case where you need to buy more
else:
    print("Need to buy tomatoes before the party.")
