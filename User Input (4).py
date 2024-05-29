                    #Rock, Paper Scissors
import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1                    #Constant data is always in caps
    PAPER = 2                   #Rock = Enum name
    SCISSORS = 3



# print(RPS(2))
# print(RPS.ROCK)
# print(RPS['ROCK'])
# print(RPS.ROCK.value)
# sys.exit()

# value = input('Please enter a value:\n')

# print(value)



print("")
playerchoice = input("Enter ...\n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n")

player = int(playerchoice)

if player < 1 or player > 3:
    print("You must enter 1,2, or 3.")

computerchoice = random.choice("123")

computer = int(computerchoice)

print("")
print("You chose " + str(RPS(player)).replace('RPS.', ''),
print("Python chose " + str(RPS(computer)).replace('RPS.', '') + "."))
print("")

if player == 1 and computer ==3:             #You can only have 1 Else and if
    print("You win!🙌")                           #but can have infinite elifs
elif player ==2 and computer ==1:
    print("You win!🙌")
elif player ==3 and computer ==2:
    print("You win!🙌")
elif player == computer:
    print("Tie game!👌")
else:
    print("Python wins!😁")