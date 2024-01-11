class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
def HotPotato(namelist, num):
    q = Queue()

    for name in namelist:
        q.enqueue(name)
    
    while q.size() > 1:
        for i in range(num):
            q.enqueue(q.dequeue())
        q.dequeue()

    return q.dequeue()

print("The winner of hot potato is : ", HotPotato(["Bill","David","Susan","Jane","Kent","Brad"], 7))