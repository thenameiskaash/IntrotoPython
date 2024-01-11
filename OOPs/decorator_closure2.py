# Python Closures and Decorators
''' A Closure is a function object that has access to variables in its lexical scope, 
even when the function is called outside that scope.'''

'''Characteristics of Closures

# 1. **Nested Functions:** The closure must have a nested function that refers to a variable defined in the enclosing (outer) function.
# 2. **Variable Capture:** The inner function captures and remembers the values of the variables in the enclosing function's scope.'''

# Example of Closure
def outer_function(x):    
    def inner_function(y):        
        return x + y    
    return inner_function

closure_instance = outer_function(10)
result = closure_instance(5)
print(result)  # Output: 15

# Decorators
''' A decorator is a design pattern in Python that allows the modification or extension of a function or class 
without altering its source code.'''

# Using Closures for Decorators
# - Closures are often used to implement decorators in Python.

### Example of Decorator
def my_decorator(func):   
    def wrapper():       
        print("Something is happening before the function is called.")        
        func()        
        print("Something is happening after the function is called.")    
    return wrapper

@my_decorator
def say_hello():    
    print("Hello!")

say_hello()

## Conclusion
# - Closures allow functions to retain access to variables from their containing scope.
# - Decorators use closures to modify or extend the behavior of functions or classes.


'''The decorator syntax `@my_decorator` is a convenient and concise way to apply a decorator to a function.
However, you can achieve the same result using the following syntax without using the `@` symbol:'''
def say_hello():    
    print("Hello!")
    
say_hello = my_decorator(say_hello)

'''In this alternative representation, `my_decorator` is explicitly applied to the `say_hello` function by calling
`my_decorator(say_hello)`. This results in the same behavior as using the decorator syntax.'''
# # The original code using the decorator syntax:
@my_decorator
def say_hello():    
    print("Hello!")
    
# is equivalent to:
def say_hello():    
    print("Hello!")
    
say_hello = my_decorator(say_hello)
# Both representations achieve the same outcome of decorating the `say_hello` function with the `my_decorator`.


