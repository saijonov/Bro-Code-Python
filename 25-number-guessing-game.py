import random

lowest = 1
highest = 100
is_running = True
tries = 0

random_number = random.randint(lowest, highest)
print(f"Enter a number between {lowest} and {highest}")

while is_running:
    if tries == 5:
        print("Lost")
        is_running = False
    print(f"You have {5-tries} tries")
    choice = input("Enter a number: ")
    if choice.isdigit():
        choice = int(choice)
        if choice > highest or choice < lowest:
            print(f"Your number must be between {lowest} and {highest}")
        else:
            tries += 1
            if choice > random_number:
                print("Your guess is high")
            elif choice < random_number:
                print("Your guess is low")
            else:
                print("cangets")
                is_running = False
    else:
        print("Please enter a number")