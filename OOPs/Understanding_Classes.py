# Class is a code template for creating objects

class Fraction:
    # the methods go here

    #def method(parameter)
    def __init__(self, top, bottom): # self is a parameter that will always be used as a reference back to the object itself
        self.num = top # 'self.num' in the constructor defines the Fraction object to have an internal data object 'num'
        self.den = bottom

        # self = this instance of a class

    def show(self):
        print(self.num, '/', self.den)
    
    def __str__(self): # Method to convert an object into a string
        return str(self.num) + '/' + str(self.den)
    
    def __add__(self, otherfaction): # Method that overrides the addition method
        newnum = self.num * otherfaction.den + self.den * otherfaction.num
        newden = self.den * otherfaction.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common, newden//common)
        # return Fraction(newnum, newden)
    
    def __sub__(self, otherfaction): # Method that overrides the addition method
        newnum = self.num * otherfaction.den - self.den * otherfaction.num
        newden = self.den * otherfaction.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common, newden//common)

    def __mul__(self, other):
        top_num = self.num * other.num
        bot_num = self.den * other.den
        return Fraction(top_num, bot_num)
    
    def __truediv__(self, other):
        top_num = self.num * other.den
        bot_num = self.den * other.num
        return Fraction(top_num, bot_num)
    
# Shadow quality compares the objects' memory addresses, faster but less accurate.
# Deep equality compares the objects' contents, slower but more accurate.

    def __eq__(self, other): # Method compares two objects and returns True if their values are the same, False otherwise
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum
    
    def __le__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum <= secondnum
    
    def __ge__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum >= secondnum


def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

# To create an instance of the Fraction class, we must invoke the constructor.
# myfraction1 is a instance
myfraction1 = Fraction(1,2)
myfraction2 = Fraction(2,3)
print(f"I ate {myfraction1} of the pizza")
print("Addition : ", myfraction1 + myfraction2)
print("Equaling : ", myfraction1 == myfraction2)
print("Multiplying : ", myfraction1 * myfraction2)
print("Division : ", myfraction1 / myfraction2)
print("Addition : ", myfraction1 - myfraction2)
print("Less than or equal to : ", myfraction1 <= myfraction2)
print("Greater than or equal to : ", myfraction1 >= myfraction2)