import random

amount_guess = 10
number_of_letters = 3

def main():
    print(f"Welcome to the guess the letters game. You have {amount_guess} chances to guess the combination of {number_of_letters} letters")

    while True:
        secretComp = getsecretComp()
        print("I have a combination of letters of the alphabet, try guessing")

        number_guess = 1
        while number_guess <= amount_guess:
            user_guess = ''
            print(f"Guess #{number_guess}")
            user_guess = input("-> ")
            if len(user_guess) == number_of_letters:
                clues = getClues(user_guess, secretComp)
            else:
                print("They should only contain 3 letters")

            if clues == "You got it!":
                print(f"You got it, it was {secretComp}")
                exit()
            else:
                print(clues)

            number_guess+=1
        
            if number_guess > amount_guess:
                print(f"Use used up all your guesses, the answer was {secretComp}")
                print("Thanks for playing!")
                exit()


def getsecretComp():
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    random.shuffle(alphabet)

    secretComp = ''
    for i in range(number_of_letters):
        secretComp += str(alphabet[i])
    return secretComp

def getClues(user_guess, secretComp):
    clues = []
    if user_guess == secretComp:
        clues.append("You got it!")
    for i in range(len(user_guess)):
        if user_guess[i] == secretComp[i]:
            clues.append(" >Right letter and right position< ")
        elif user_guess[i] in secretComp:
            clues.append(" >Right letter but wrong position< ")
    
    if len(clues) == 0:
        return "None of the letter are used"
    else:
        clues.sort()
        return ' '.join(clues)
    
if __name__ == '__main__':
    main()