menu = {"burger":3.00,
        "hamburger":2.00,
        "salad": 5.50,
        "lavash": 6.50,
        "cola": 2.40,
        "coffee": 5.00}
total = 0
cart = []

print("-------- MENU -------")

for keys, values in menu.items():
    print(f"|  {keys:10}: {values:.2f}  |")


print("---------------------")

while True:
    food = input("Pick an item to buy (q to quit): ")
    if food.lower() == "q":
        break
    elif menu.get(food.lower()) is not None:
        cart.append(food)
        total += menu[food]
    elif menu.get(food) is None:
        print(f"No such an item named {food}")

if len(cart) == 0:
    print("You did not buy anything")
else:
    for food in cart:
        print(f"{food}", end="  ")
    print(f"Your total is ${total}")

