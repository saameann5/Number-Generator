import random
import math
import tkinter as tk





# TAKING INPUTS

lower = int(input("ENTER LOWER INPUT:"))
upper = int(input("ENTER UPPER LIMIT:"))

#USE FORMULA TO GENERATE NUMBER OF GUESSES

x = random.randint(lower, upper)

print("\n\t You have only",
      round(math.log(upper - lower + 1, 2)),
      "chances to guess the number!\n")



#INITIALIZING GUESSES

count = 0


#Guess depends upon range

while count < math.log(upper - lower + 1, 2):
    count += 1


    guess = int(input("Guess a number!:"))

    if x == guess :
        print("Congratulations you did it in",
              count, "try!")
        break
    elif x > guess :
        print("You've guessed too low!")
    elif x < guess :
        print("You've guessed too high!")


if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)
    print("Better luck next time!")
   





