#This is a guess the number game
import random

hiddenNumber = random.randint(1,25)
print("I am thinking of a number between 1 and 25")

#Ask player to guess 5 times.


for guessTaken in range(1, 7):
    print("Take a guess.")
    guess = int(input())

    if guess < hiddenNumber :
        print("Your guess is too low.")
    elif guess > hiddenNumber :
        print("Your guess is too high.")
    else:
        break       #correct guess.


if guess == hiddenNumber:
    print("good job! you guesses the number in " + str(guessTaken) + "guesses")
else:
    print("worng guess.The number is " + hiddenNumber)

