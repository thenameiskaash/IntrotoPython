def hi(msg):
    print(msg)

f = hi
print(f)
f("I'm a function now")


'''Higher order Functions : A function that can accept other functions as arugments 
then returns functions to the caller'''

def adder(num):
    return num + 2

def myfunc(func):
    return str(func) + str(" is your result")

addme = adder(4)
print(myfunc(addme))


'''Closures : Returning a function from within another function, it is a function object that remembers values 
in enclosing scopes even if they are not present in memeory'''

def names(firstname):
    def get_name(lastname):
        return str(firstname) + ' ' + str(lastname)
    return get_name

n = names("Mickey")
print(n("Mouse"))

def number(first):
    def secondnumber(second):
        return first + second
    return secondnumber

add = number(5)
print(add(6))

def decorator(func1):    
    def wrapper():        
        print("This is from the the wrapper function")        
        return func1()    
    print("This is from the the decorator function")    
    return wrapper #Returns wrapper but does not execute - no "( )"
@decorator
def decoratee():    
    return 'This is from decoratee Function'
print(decoratee()) # This executes the wrapper