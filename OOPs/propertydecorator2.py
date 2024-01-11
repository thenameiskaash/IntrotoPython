class Student:    
    def __init__(self, name, age):        
        self._name = name  # Note: conventionally, a single leading underscore indicates a "protected" attribute        
        self._age = age    
    
    @property    
    def name(self):        
        """Getter method for the 'name' property."""        
        return self._name    
    
    @name.setter    
    def name(self, new_name):        
        """Setter method for the 'name' property."""        
        if not isinstance(new_name, str):            
            raise TypeError("Name must be a string.")        
        self._name = new_name    
        
    @property    
    def age(self):        
        """Getter method for the 'age' property."""        
        return self._age    
    
    @age.setter    
    def age(self, new_age):       
        """Setter method for the 'age' property."""        
        if not isinstance(new_age, int):            
            raise TypeError("Age must be an integer.")        
        if new_age < 0:            
            raise ValueError("Age must be a non-negative integer.")        
        self._age = new_age
        
# Creating a Student object
student = Student("Alice", 20)

# Accessing properties
print("Name:", student.name)
print("Age:", student.age)

# Modifying properties using setters
student.name = "Bob"
student.age = 25

# Accessing modified properties
print("Modified Name:", student.name)
print("Modified Age:", student.age)