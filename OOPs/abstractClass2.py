from abc import ABC, abstractmethod

# Abstract Base Class for Human
class Human(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def introduce(self):
        pass

class Student(Human):
    def __init__(self, name, age, student_id):
        super(Student,self).__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        return f"Hello, I'm a student and my name is {self.name} and I am {self.age} years old."
    
class Course:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.student = []

    def enroll_student(self, student):
        if isinstance(student, Student):
            self.student.append(student)
        else:
            print("Only students can enroll to this course")

    def list_student(self):
        student_names = [student.name for student in self.student]
        return student_names
    
# Creating Objects
student1 = Student("Mark", 24, "42952")
course1 = Course("Intro to Computer Science", "CS50")

# Accessing Attributes and calling methods
print(student1.introduce())

course1.enroll_student(student1)


print(course1.list_student())