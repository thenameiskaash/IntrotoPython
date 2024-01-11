'''Property function is  apython built-in function that returns a property object
It allows us to get, set and delete attribute values'''

### Syntax
#   property = (fget = None, fset = None, fdel = None, doc = None)

# Getter - Any code that retrieves the value of "num", will be automatically calling getnum. x.num
# Setter - Same holds true for any code tat sets num - will be calling setnum 
# Deleter - Any code that deletes num will automatically call delnum

class Prop():    
    def __init__(self, num):        
        self.n = num  # this makes the calls to setter, getter and deleter    
    
    def getnum(self):  # gets value        
        '''I am the doc for prop'''       
        return self.n    
    
    def setnum(self, value):  # sets a value        
        print('set num: ', value)        
        self.n = value  # this sets the attribute    
        
    def delnum(self):  # deletes a value        
        print("deleting num")        
        del self.n    
    
    num = property(getnum, setnum, delnum)  # this is our property object called "num"
    
x = Prop(8)  # create an instance for Prop, pass value of 8
print("The getter, returns the value", x.num)  # prints value of self.n

x.num = 124  # this invokes the setter
print(x.__dict__.values())  # before delete prints dict_values([124])

del x.num  # this deletes using delnum
print(x.__dict__.values())  # after del prints dict_values([]) # now empty
print(Prop.num.__doc__)  # get the docstring from property function (4th arguments) or from getnum