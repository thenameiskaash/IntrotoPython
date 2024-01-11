import random

class MSDie:
    def __init__(self, number_sides):
        self.number_sides = number_sides
        self.current = self.roll()

    def __str__(self): # Magic method to give it a meaninigful string representation.
        return str(self.current)
    
    # Magic method for representation in the interactive shell, the debugger, and other cases where string conversion does not happen.
    def __repr__(self): 
        return f"MSDie({self.number_sides} : {self.current})"

    def roll(self):
        self.current = random.randrange(1,self.number_sides+1)
        return self.current
    
my_die = MSDie(6)
for i in range(5):
    print(my_die, my_die.current)
    my_die.roll()

d_list = [MSDie(6), MSDie(20)]
print(d_list)