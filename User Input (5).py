                    #Rock, Paper Scissors
import sys
import random
from enum import Enum


def play_rps():

    class RPS(Enum):
        ROCK = 1                    #Constant data is always in caps
        PAPER = 2                   #Rock = Enum name
        SCISSORS = 3

    #playagain = True
                            #13 & 14 is for rps class
    #while playagain:

    playerchoice = input("\nEnter ...\n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n")

    if playerchoice not in ["1","2","3"]:
        print("You must enter 1, 2, or 3.")
        return play_rps()

    player = int(playerchoice)


    computerchoice = random.choice("123")

    computer = int(computerchoice)


    print("\nYou chose " + str(RPS(player)).replace('RPS.', ''),
    print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".\n"))


    if player == 1 and computer ==3:             #You can only have 1 Else and if
        print("You win!🙌")                       #but can have infinite elifs
    elif player ==2 and computer ==1:
        print("You win!🙌")
    elif player ==3 and computer ==2:
        print("You win!🙌")
    elif player == computer:
        print("Tie game!👌")
    else:
        print("Python wins!😁")

    print("\nPlay_again?")

    while True:
        playagain = input("\nY for Yes or \nQ to Quit\n")
        if playagain.lower() not in ["y","q"]:
            continue
        else:
             break

    if playagain.lower() == "y":
        return play_rps()
    else:
        print("\n🥳🥳🥳")
        print("Thank you for playing!!!\n")
        sys.exit("Bye! 😒")


play_rps()