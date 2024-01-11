'''In Python, overloading and overriding are two fundamental concepts used in object-oriented programming,
specifically when dealing with methods.

Method Overloading:
Method overloading refers to the ability to define multiple methods in the same class with the same name
but different parameters. 
Python doesn't support method overloading in the traditional sense, as it doesn't consider the method name 
and parameter types to differentiate between methods. 
Instead, you can achieve method overloading by using default arguments or variable-length argument lists.'''

# Here's an example demonstrating method overloading in Python:

# Base Class: Human
class Human:    
    def __init__(self, name, age):        
        self.name = name        
        self.age = age

# Concrete Class: Student
class Student(Human):    
    def __init__(self, name, age, student_id):        
        super().__init__(name, age)        
        self.student_id = student_id    
    
    def introduce(self, additional_info=""):        
        return f"Hi, I'm a student named {self.name} with student ID {self.student_id}. {additional_info}"

# Creating Objects
student1 = Student("Alice", 25, "12345")

# Method Overloading in Action
print(student1.introduce())  # Output: "Hi, I'm a student named Alice with student ID 12345."
print(student1.introduce("I love programming."))  # Output: "Hi, I'm a student named Alice with student ID 12345. I love programming."

'''In the above example, the introduce method in the Student class is overloaded to accept an additional_info 
parameter, providing flexibility when calling the method with or without additional information.

Method Overriding:
Method overriding occurs when a subclass provides a specific implementation for a method that is already 
defined in its superclass. 
It allows a subclass to provide its own implementation of a method while keeping the method name the same.'''

# Here's an example demonstrating method overriding in Python:

# Base Class: Human
class Human:    
    def __init__(self, name, age):        
        self.name = name        
        self.age = age    
    
    def introduce(self):        
        return f"Hello, my name is {self.name}, and I'm {self.age} years old."

# Concrete Class: Teacher (Method Overriding)
class Teacher(Human):    
    def __init__(self, name, age, subject):        
        super().__init__(name, age)        
        self.subject = subject    
    
    def introduce(self):        
        return f"Hello, my name is {self.name}, and I'm a teacher. I teach {self.subject}."

# Creating Objects
teacher1 = Teacher("Mr. Smith", 45, "Math")

# Method Overriding in Action
print(teacher1.introduce())

'''In the above example, the Teacher class overrides the introduce method defined in the Human class
# with its own implementation. When you call teacher1.introduce(), the overridden method in the Teacher class is
# executed instead of the method from the Human class.'''

'''Method overriding allows a subclass to provide a specialized behavior for a method inherited from its superclass
promoting the flexibility and extensibility of the class hierarchy.'''