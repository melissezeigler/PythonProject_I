import random

game_on = True
while game_on:
    player = input('Please type "Rock", "Paper", "Scissors", or "I quit": ')
    computer = random.randint(1, 3)

#Let the random integer 1 = Rock, 2 = Paper, and 3 = Scissors

    if (player == 'Rock' and computer == 1):
        print("Game Tied")
    elif (player == 'Paper' and computer == 2):
        print("Game Tied")
    elif (player == 'Scissors' and computer == 3):
        print("Game Tied")
    elif (player == 'Rock' and computer == 2):
        print("You Lose")
    elif (player == 'Paper' and computer == 3):
        print("You Lose")
    elif (player == 'Scissors' and computer == 1):
        print("You Lose")
    elif (player == 'Paper' and computer == 1):
        print("You Win")
    elif (player == 'Scissors' and computer == 2):
        print("You Win")
    elif (player == 'Rock' and computer == 3):
        print("You Win")
    elif (player == "I quit"):
        print("Thank you for playing")
        game_on = False
    else:
        print("Please enter a valid input Rock/Paper/Scissors/I quit")
