from abc import abstractmethod, ABC

class AbstractClass(ABC): #Abstract Base Class
    @abstractmethod
    def say_it(self):
        pass

class ConcreteClass(AbstractClass):
    def say_it(self):
        print("Do it!")

test = ConcreteClass()
test.say_it()