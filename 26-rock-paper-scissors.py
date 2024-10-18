import random

options = ('rock', 'paper', 'scissors')
running = True

while running:
    player = None

    while player not in options and player != 'q':
        player = input("Pick a choice (rock, paper, scissors or 'q' to quit): ")

    if player == 'q':
        print("Quit")
        break

    computer = random.choice(options)  
    print(f"Player: {player}")
    print(f"Computer: {computer}")

    # Determine the outcome
    if player == computer:
        print("Draw")
    elif (player == "paper" and computer == "rock") or \
         (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper"):
        print("Player won")
    else:
        print("Computer won")












