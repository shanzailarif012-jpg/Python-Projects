# Project 2 THE PERFECT GUESS  

import random
a = random.randint(1,100)

guesses = 1
n = -1

while (a != n):
    n = int(input("Enter Guess Number: "))
    if a > n:
        print("Higher Number please")
        guesses +=1
    elif a < n:
        print("Lower number please")
        guesses +=1

print(f"You have guessed the number {n} correctly in {guesses} attempts")

