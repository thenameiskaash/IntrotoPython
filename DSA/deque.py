class Deque:
    def __init__(self):
        self.items = []
    
    def isEmpty(self): # Check if empty
        return self.items == []
    
    def addRear(self, item): # Add values to the back
        self.items.insert(0, item)
    
    def removeRear(self): # Remove values from the back
        return self.items.pop()

    def addFront(self, item): # Add values to the front
        self.items.append(item)

    def removeFront(self): # Remove values from the front
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)
    
d = Deque()
print("Is the Deque empty : ", d.isEmpty())
d.addRear(8)
d.addRear('mouse')
d.addFront(16)
d.addFront('cat')
print("What is the current size of Deque : ", d.size())
print("Is the Deque still empty : ", d.isEmpty())
d.addFront(True)
print("This was the value in front : ", d.removeFront())
print("This was the value in the rear : ", d.removeRear())
