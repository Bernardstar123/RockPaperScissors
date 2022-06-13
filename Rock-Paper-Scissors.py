import random

# R = Rock, P = Paper and S = Scissors
while True:
    choices = ["R", "P", "S"]

    computer = random.choice(choices)
    player = None


    while player not in choices:
        player = input("R, P, or S?: ").upper()

    if player == computer:
        print("computer: ",computer)
        print("player: ",player)
        print("Tie!")
    elif player == "R":
        if computer == "P":
            print("computer: ",computer)
            print("player: ",player)
            print("You lose!")
        if computer == "S":
            print("computer: ",computer)
            print("player: ",player)
            print("Wow, You win!")
    elif player == "S":
        if computer == "R":
            print("computer: ",computer)
            print("player: ",player)
            print("You lose!")
        if computer == "P":
            print("computer: ",computer)
            print("player: ",player)
            print("Wow, You win!")
    elif player == "P":
        if computer == "S":
            print("computer: ",computer)
            print("player: ",player)
            print("You lose!")
        if computer == "R":
            print("computer: ",computer)
            print("player: ",player)
            print("Wow, You win!")

    play_again = input("play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("Bye, Thanks for your time!")