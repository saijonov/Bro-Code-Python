foods = []
prices = []
total = 0

while True:
    food = input("Enter the food you wanna buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = input("Enter the price of the {food}: ")
        foods.append(food)
        prices.append(price)

print("\n---------- YOUR CART ----------\n")
for food in foods:
    print(food, end="  ")

for price in prices:
    total = total + int(price)

print("\n----------COST----------\n") 
print(f"${total}")