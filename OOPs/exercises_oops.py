# 1. Implement the simple methods getNum and getDen that will return the numerator and denominator of a fraction.
# 2. Modify the constructor for the Fraction class so that GCD is used to reduce fractions immediately.
from math import gcd
class fraction:
    def __init__(self,top,bot):
        if not isinstance(top, int):
            raise ValueError(f"{top} is not a integer")
        if not isinstance(bot, int):
            ValueError(f"{bot} is not integer")
        else:
            self.top = top
            self.bot = bot
        
    
    def __str__(self):
        return f"{self.top} / {self.bot}"
    
    def getNum(self):
        return f"The numerator is {self.top}"
    
    def getDen(self):
        return f"The denominator is {self.bot}"
    
    def __add__(self, other_fraction):
        self.upper = self.top * other_fraction.bot + self.bot * other_fraction.top
        self.lower = self.bot * other_fraction.bot
        self.together = gcd(self.upper, self.lower)
        return fraction(self.upper//self.together, self.lower//self.together)
    
    def __sub__(self, other_fraction):
        self.upper = self.top * other_fraction.bot - self.bot * other_fraction.top
        self.lower = self.bot * other_fraction.bot
        self.together = gcd(self.upper, self.lower)
        return fraction(self.upper//self.together, self.lower//self.together)
    
    def __mul__(self, other_fraction):
        self.upper = self.top * other_fraction.top
        self.lower = self.bot * other_fraction.bot
        self.together = gcd(self.upper, self.lower)
        return fraction(self.upper//self.together, self.lower//self.together)
    
    def __truediv__(self, other_fraction):
        self.upper = self.top * other_fraction.bot
        self.lower = self.bot * other_fraction.top
        self.together = gcd(self.upper, self.lower)
        return fraction(self.upper//self.together, self.lower//self.together)
    

    



    
test1 = fraction(2,12)
test2 = fraction(1,3)

print(test1.getNum())
print(test1.getDen())
print(test1 + test2)