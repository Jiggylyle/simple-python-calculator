# Shopping Cart Programme

food_items = []
prices = []
total = 0

while True:
    food_item = input("Enter a food item (q to quit): ")
    if food_item.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of {food_item}: R"))
        food_items.append(food_item)
        prices.append(price)

print("-----Your Shopping Cart-----")

for food_item in food_items:
    print(food_item)

print("-----Invoice-----")
for x in range(len(food_items)):
    print(f"{food_items[x]}: R{prices[x]:.2f}")
    total += prices[x]
print(f"Total: R{total:.2f}")
