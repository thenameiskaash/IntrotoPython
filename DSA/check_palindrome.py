# A simple problem : To check if the given word a palindrome

from deque import *

def palindrome(input_string):
    d = Deque()

    for n in input_string:
        d.addRear(n)
    
    checking = True # Boolean value to see if it's still a palindrome or not

    while d.size() > 1 and checking:
        front = d.removeFront()
        back = d.removeRear()
        if front != back: 
            checking = False
        
    return checking

print(palindrome("hello"))
print(palindrome("rotor"))