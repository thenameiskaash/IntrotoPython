# Ordered Linked List : Elements are arranged in specific order, ascending or decending.
# When a new elements is inserted, the list is rearranged to maintain the order.

# [17, 26, 31, 54, 77, 93]

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

    def setNext(self, newdata):
        self.next = newdata

class OrderedList:
    def __init__(self):
        self.head = None

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() == item:
                    stop = True
                else:
                    current = current.getNext()
        return found
    
    def add(self, item):
        temp = Node(item)
        current = self.head
        stop = False
        previous = None
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def isEmpty(self):
        return self.head == None
    
    def size(self):
        current = self.head
        count = 0 
        while current != None:
            count+=1
            current = current.getNext()
        return count
    
    def display(self):
        display = []
        current = self.head
        while current:
            display.append(current.data)
            current = current.next
        return display

mylist = OrderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))

print(mylist.display())