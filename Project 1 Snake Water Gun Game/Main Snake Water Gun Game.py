                           #Snake Water Gune Game 

# Game Description
'''
A simple Python-based Snake, Water, Gun game where the player competes against the computer.
 The game uses random choice logic to determine the computer's move and announces
 the winner based on the game rules.'''

'''
1 For Snake 
-1 For Water 
0 For Gun
'''
                    # Lets Start Snake Water Gun Game

import random 

computer = random.choice ([-1 , 0 , 1])
youstr = input("Enter Your choice: ")
youdict = {"s":1 , "w":-1 , "g":0 }
reversedict = {1:"Snake" , -1:'Water', 0:"Gun"}

you = youdict[youstr] 

# By Now We have (2 Variable) You and Computer 

print(f"You Choose {reversedict[you]} \nComputer Choose {reversedict[computer]}")

# Conditions You and Computer 

if ( computer == you):
    print("Oops Its Draw")
else:

    if (computer == -1 and you == 1):
     print("You Win!")

    elif (computer == -1 and you == 0):
       print("You Loose!")

    elif (computer == 1 and you == 0):
       print("You Win!")

    elif (computer == 1 and you == -1):
       print("You Loose!")

    elif (computer == 0 and you == -1):
       print("You Win!")

    elif (computer == 0 and you == 1):
       print("You Loose!")

    else:
       print("SomeThing Went Wrong!")

'''
Project Description:
This is a simple Snake, Water, Gun game built using Python. In this project,
the player competes against the computer, where the computer makes a random
choice using the random module. The game takes the player's input, compares
both choices using conditional statements (if-elif-else), and announces the
winner based on the game rules. This project demonstrates the use of variables,
dictionaries, user input, random choice, and decision-making logic in Python.
'''



