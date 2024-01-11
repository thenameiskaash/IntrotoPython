class Person:
    def __init__(self,name:str,age:int):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major
    
    def __str__(self):
        return f"{self.name}, they are {self.age} years old and in {self.major}"
    
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
        
    def __str__(self):
        return f"Prof. {self.name}, they are {self.age} and teaches {self.subject}"
    

a = Student("Joe", 22, "Computers")
print(a)

b = Teacher("Jana", 53, "Classical Mechanics")
print(b)