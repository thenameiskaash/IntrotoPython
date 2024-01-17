# Implementing an Unordered List: Linked Lists

# Basic building blocks for the linked list implementation is the 'Node'.
# Node must contain the list item itself, we call this 'Data Field' of the node.

class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

temp = Node(93)
print(temp.getData())

# The reference 'None' to denote the "end" of the linked structure.

class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None
    
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

# 'size' 'search' 'remove' are based on linked list traversal
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count +=1 
            current = current.getNext()
        return count
    
    def search(self, item):
        current = self.head
        search = False
        while current != None and not search:
            if current.getData() == item:
                search = True
            else:
                current = current.getNext()
        return search
    
    def remove(self, item):
        current = self.head
        search = False
        previous = None
        while current != None and not search:
            if current.getData() == item:
                search = True
            else:
                previous = current # "inch-worming" as 'previous' must catch up to 'current' before 'current' moves ahead.
                current = current.getNext()
        if previous == None:
            self.head == current.getNext()
        else:
            previous.setNext(current.getNext())

    def append(self, item):
        temp = Node(item)
        current = self.head
        while current.next != None:
            current = current.next
            if current == None:
                current = temp
        current.next = temp

    # def insert(self, item, previous):
    #     temp = Node(item)
    #     temp.next = previous.next
    #     previous.next = temp

    def display(self):
        display = []
        current = self.head
        while current:
            display.append(current.data)
            current = current.next
        return display



mylist = UnorderedList()
mylist.add(31) # First item added, last node on the linked list
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54) # Last item added, first node on the linked list

print("Size of the list :", mylist.size())

print("Does the number exist in the list :", mylist.search(17))

mylist.append(99)

print(mylist.size())

print(mylist.display())