# Modifying the printing simulation to reflect when the number of students was doubled.

from queue import *
import random 

class Printer:
    def __init__(self, paperperminute):
        self.pagerrate = paperperminute
        self.currenttask = None
        self.timeremaining = 0

    def tick(self): # Decrementing the time remaining for the task
        if self.currenttask != None:
            self.timeremaining = self.timeremaining - 1
            if self.timeremaining <= 0:
                self.currenttask = None
    
    def busy(self): # Checking if printer is currently busy or not
        if self.currenttask != None:
            return True
        else:
            return False
    
    def startNextTask(self, nexttask): # Next task that is assigned to the printer
        self.currenttask = nexttask
        self.timeremaining = nexttask.getPages() * 60/self.pagerrate

class Task:
    def __init__(self,time):
        self.timestamp = time
        self.pages = random.randrange(1,21) # One to 20 pages

    def getStamp(self):
        return self.timestamp
    
    def getPages(self):
        return self.pages
    
    def waitTime(self, currenttime):
        return currenttime - self.timestamp
    
def simulation(numSeconds, PagesPerMin):
    lab_printer = Printer(PagesPerMin)
    print_Queue = Queue()
    waiting_times = []

    for currentSecond in range(numSeconds):

        if newPrintTask():
            given_task = Task(currentSecond)
            print_Queue.enqueue(given_task)

        if (not lab_printer.busy()) and (not print_Queue.isEmpty()):
            nexttask = print_Queue.dequeue()
            waiting_times.append(nexttask.waitTime(currentSecond))
            lab_printer.startNextTask(nexttask)

        lab_printer.tick()
    
    averageWait = sum(waiting_times)/len(waiting_times)
    print(f"Average Wait {averageWait:6.2f} seconds {print_Queue.size():3d} task remaining")

def newPrintTask():
    num =  random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False

for i in range(10):
    simulation(3600, 5)