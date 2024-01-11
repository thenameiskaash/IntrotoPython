import math

anumber = int(input("Please enter an integer : "))
try:
    print(math.sqrt(anumber))
except:
    print("You cannot use a negative number")
    print("Try a absolute value")
    print(math.sqrt(abs(anumber)))


