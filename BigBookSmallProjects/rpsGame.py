import random
import sys

print("ROCK, PAPER, SCISSORS")

while True: #Player loop
    print("Enter (r)ock, (p)aper, (s)cissors or (q)uit")
    playmove = input()
    if playmove == 'q':
        sys.exit()
    if playmove == 'r' or 'p' or 's':
        break
    else:
        print("You have to pick from (r)ock, (p)aper, (s)cissors or (q)uit")

 
computer = random.randint(1,3)
if computer == 1:
    computerMove = 'r'
    print("Computer chose Rock")
if computer == 2:
    computerMove = 'p'
    print("Computer chose Paper")
else:
    computerMove = 's'
    print("Computer chose Scissor")

if playmove == computerMove:
    print("It's a draw")
if playmove == 'r' and computerMove == 's' or playmove == 's' and computerMove == 'p' or playmove == 'p' and computerMove == 'r':
    print("player wins")
if playmove == 's' and computerMove == 'r' or playmove == 'p' and computerMove == 's' or playmove == 'r' and computerMove == 'p':
    print("Computer wins")