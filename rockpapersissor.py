import random

while True:

    computer = random.choice(["rock", "paper", "scissors"])

    user = input("rock, paper or scissors? ")

    print("The computer chose", computer,"and the user chose", user +".")

    # TODO - Implement the if statements that prints who wins

    if user == computer: 
        print("Draw")

    elif user == "rock" and computer == "scissors":
        print(user, "win")

    elif user == "paper" and computer == "rock":
        print(user, "win")

    elif user == "scissors" and computer == "rock":
        print(user, "win")

    else:
        print(user, "lost, computer won")

        endrake=input("vill du köra igen?")

        if endrake != "ja":
         break