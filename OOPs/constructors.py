class Apple: 
    # Constructors
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
    def __str__(self): 
        return f"This Apple is {self.color} and taste like {self.flavor}"
jonagold = Apple("red", "sweet")
print(jonagold)


class Persona:
    def __init__(self, name, number):
        self.name = name
        self.number = number
    def __str__(self):
        return f"Hi, my name is {self.name} and I am {self.number} years old"
    
introduction = Persona("Jona", "38")
print(introduction)
print(introduction.name)