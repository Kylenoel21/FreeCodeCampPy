                                #Scopes
#Global scopes is avaialble to everything in the file
# name = "Dave"         #255
# count = 1             #255

#Print name is a local scope
# def greeting(name):
#     color = "blue"
#     print(color)
#     print(name)
#                         #To print color in local scope is perfectly fine since its defined
                        #However if print color is in global scope then it will be a problem, since its only defined locally
# greeting("John")

                        #Another is a parent function, color is a nested function
                        #Nested functions is for when ur only gunna use the function, inside
                        #Another function and wont need it outside in the global scope
                        #You do this bcuz when working with others, you want the global scope
                        #to be as unpolluted as possible, and try to keeo things less confusing

                        #You cant change global values, inside of local scopes. Bcuz thats a different variable
                        #When you enter global keyword, the modify value its ok

                                #255
# def another():
#     color = "blue"
#     global count
#     count += 1
#     print(count)
#     def greeting(name):
#         nonlocal color
#         color = "red"
#         print(color)
#         print(name)
#
#     greeting("Dave")
#
# another()
                                #255







                            #RPS 4
                    #Rock, Paper Scissors
import sys
import random
from enum import Enum

game_count = 0

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

    def decide_winner(player, computer):
        if player == 1 and computer ==3:             #You can only have 1 Else and if
            return"You win!🙌"                    #but can have infinite elifs
        elif player ==2 and computer ==1:
            return"You win!🙌"
        elif player ==3 and computer ==2:
            return"You win!🙌"
        elif player == computer:
            return"Tie game!👌"
        else:
            return"Python wins!😁"

    game_result = decide_winner(player, computer)

    print(game_result)

    global game_count
    game_count += 1

    print("\nGame count: " + str(game_count))

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