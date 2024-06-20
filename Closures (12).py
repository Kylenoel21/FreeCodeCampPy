                                    #Closures

#Closure is a function having access to the scope of its parent function after the parent function
#has returned
#Nested functions have access to their parents functions
            #Closure is created when the parent function returns
# def parent_function(person, coins):
#    # coins = 3
#
#     def play_game():
#         nonlocal coins
#         coins -= 1
#
#         if coins > 1:
#             print("\n" + person + " has " + str(coins) + " coins left.")
#         elif coins == 1:
#             print("\n" + person + " has " + str(coins) + " coin left.")
#         else:
#             print("\n" + person + " is out of coins.")
#
#     return play_game
#
# tommy = parent_function("Tommy", 3)
# jenny = parent_function("Jenny", 5)
#
# tommy()
# tommy()
#
# jenny()
#
# tommy()












                            #RPS 5

import sys
import random
from enum import Enum

def rps():
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal player_wins
        nonlocal python_wins

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

        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer ==3:             #You can only have 1 Else and if
                player_wins +=1
                return"You win!🙌"                    #but can have infinite elifs
            elif player ==2 and computer ==1:
                player_wins += 1
                return"You win!🙌"
            elif player ==3 and computer ==2:
                player_wins += 1
                return"You win!🙌"
            elif player == computer:
                return"Tie game!👌"
            else:
                python_wins += 1
                return"Python wins!😁"

        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print("\nGame count: " + str(game_count))
        print("\nPlayer wins: " + str(player_wins))
        print("\nPython wins: " + str(python_wins))

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

    return play_rps


play = rps()

play()