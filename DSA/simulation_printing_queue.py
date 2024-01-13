import random
from queue import *

class Printer:
    def __init__(self, pagepermin):
        self.pagepermin = pagepermin
        self.currenttask = None
        self.timeremain = 0

    def tick(self):
        if self.currenttask != None:
            self.timeremain = self.timeremain - 1
            if self.timeremain <= 0:
                self.currenttask = None

    def busy(self):
        if self.currenttask != None:
            return True
        else:
            return False
    
    def NextTask(self, newtask):
        self.currenttask = newtask
        self.timeremain = newtask.getPages() * 60/self.pagepermin
    
class Task:
    def __init__(self,time):
        self.timestamp = time
        self.pages = random.randrange(1,21)

    def getStamp(self):
        return self.timestamp
    
    def getPages(self):
        return self.pages
    
    def waitTime(self, currentTime):
        return currentTime - self.timestamp
    
def sim(num_sec, PagesPerMin):

    printer = Printer(PagesPerMin)
    q = Queue()
    wait_time = []

    for current in range(num_sec):
        if newTask():
            task = Task(current)
            q.enqueue(task)
        
        if (not q.isEmpty()) and (not printer.busy()):
            nexttask = q.dequeue()
            wait_time.append(nexttask.waitTime(current))
            printer.NextTask(nexttask)
        
        printer.tick()

    avg_wait = sum(wait_time)/len(wait_time)
    print(f"Average wait time is {avg_wait:.2f} second, {q.size()} task remaining")

def newTask():
    num = random.randrange(0,181) 
    if num == 180:
        return True
    else:
        return False

for i in range(10):
    sim(3600, 5)