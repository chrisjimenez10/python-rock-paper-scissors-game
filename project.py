#Rock, Paper, Scissors
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

def gameStart():
    optionList = [rock, paper, scissors]
    while True:
        while True:
            playerInput = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n")
            try:
                playerInput = int(playerInput)
                if playerInput in [0, 1, 2]:
                    playerChoice = optionList[playerInput]
                    computerChoice = optionList[random.randint(0, 2)]
                    break
                else:
                    print("Not a valid choice")
            except ValueError:
                print("Please provide a valid number: 0, 1, or 2")

        if playerChoice == rock and computerChoice == scissors:
            print(F"You chose:\n{rock}\nComputer chose:\n{scissors}\nYou win")
        elif computerChoice == rock and playerChoice == scissors:
            print(F"You chose:\n{scissors}\nComputer chose:\n{rock}\nYou lose")
        elif playerChoice == paper and computerChoice == rock:
            print(F"You chose:\n{paper}\nComputer chose:\n{rock}\nYou win")
        elif computerChoice == paper and playerChoice == rock:
            print(F"You chose:\n{rock}\nComputer chose:\n{paper}\nYou lose")
        elif playerChoice == scissors and computerChoice == paper:
            print(F"You chose:\n{scissors}\nComputer chose:\n{paper}\nYou win")
        elif computerChoice == scissors and playerChoice == paper:
            print(F"You chose:\n{paper}\nComputer chose:\n{scissors}\nYou lose")
        elif playerChoice == computerChoice:
            print(F"You chose:\n{playerChoice}\nComputer chose:\n{computerChoice}\nIt's a tie")
        
        while True:
            reset = input("Whould you like to play again? - Y / N: ").lower()
            if reset == "y":
                #Here, we use "break" to exit this current while loop and continue with the code AFTER, which is the Main while loop at the start of the game (function call)
                break
            elif reset == "n":
                print("Thanks for playing!")
                #Here, we use "return" to exit the function gameStart() entirely, which stops any further code execution within this function
                return
            else:
                print("Invalid input. Please type Y or N")

gameStart()