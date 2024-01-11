import random

def guess(x):
    secretNumber = random.randint(1,x)
    print(f"Let's play a game, guess a number from 1 to {secretNumber}")
    for guesses in range(1,x):
        guess = int(input())
        if guess > secretNumber:
            print("The guess is too high, try again")
        elif guess < secretNumber:
            print("The guess is too low, try again")
        else:
            print(f"You got it , it was {secretNumber} in {guesses} guesses!")
            break

guess(10)