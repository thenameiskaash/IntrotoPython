# A classmethod is a method that takes the class as its first argument, rather than the instance.
# It can access and modify the class state, making it useful for tasks related to the class rather
# than a specific instance.

class Student:    
    total_students = 0    
    def __init__(self, name, age):        
        self.name = name        
        self.age = age        
        Student.total_students += 1    
        
    @classmethod    
    def get_total_students(cls):        
        return cls.total_students
    
# Creating instances of the Student class
student1 = Student("Alice", 20)
student2 = Student("Bob", 16)

# Using the class method
total_students = Student.get_total_students()
print(f"Total students: {total_students}")