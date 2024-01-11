# Inheritance is the ability for one class to be related to another class, just like how people are related to one another.

# Inheritance Hierarchy : 
# Python child classes can inherit characteristic data and behavior from a parent class. 
# These classes are often referred to as subclasses (Child) and superclasses (Parent).

# IS-A Relationship: (Requires inheritance)
# Python Collections -> Sequential collection (Parent) -> list, string, tuple (Each is a child)
#                    -> Non_sequential collection (Parent) -> dictionary (child)

#Logic Gates :
        # Binary Gate : AND, OR
        # Unary Gate : NOT

class LogicGate:
    
    # Parent class constructors
    def __init__(self, n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label
    
    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

class BinaryGate(LogicGate): # AND, OR

    # Child class constructors
    # Need to call parent class constructors and then move on their own data
    def __init__(self,n):
        #LogicGate.__init__(self,n)
        super(BinaryGate,self).__init__(n)

        self.pinA = None
        self.pinB = None
    
    def getPinA(self):
        if self.pinA == None: # To check if the input line is connected to anything
            return int(input(f"Enter Pin A input for gate {self.getLabel()} --> "))
        else: 
            return self.pinA.getFrom().getOutput()
    
    def getPinB(self):
        if self.pinB == None: 
            return int(input(f"Enter Pin B input for gate {self.getLabel()} --> "))
        else:
            return self.pinB.getFrom().getOutput()
    
    def setNextPin(self, source): # Connector must only be connected to one line
        if self.pinA == None:   # pinA is chosen by default
            self.pinA = source
        else:
            if self.pinB == None: # if pinA is already connected then choose pinB
                self.pinB = source
            else:
                #raise RuntimeError("Error : No Empty Pins on this Gate") # Raise an error
                print("Cannot Connect: NO EMPTY PINS on this gate")

class AndGate(BinaryGate):
    def __init__(self,n):
        super(AndGate,self).__init__(n)
    
    def performGateLogic(self):
        
        a = self.getPinA()
        b = self.getPinB()

        if a == 1 and b == 1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):
    def __init__(self, n):
        super(OrGate, self).__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 1 or b == 1:
            return 1
        else:
            return 0

class UnaryGate(LogicGate):
    
    # Constructors
    def __init__(self, n):
        # LogicGate().__init__(self,n)
        super(UnaryGate,self).__init__(n) 

        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(input(f"Enter Pin input for gate {self.getLabel()} --> "))
        else:
            return self.pin.getFrom().getOutput()
    
    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")

class NotGate(UnaryGate):
    def __init__(self, n):
        super(NotGate, self).__init__(n)
    
    def performGateLogic(self): 
        a = self.getPin()

        if a != 1:
            return 1
        else:
            return 0

# Create a two new gate classes, one called NorGate the other called NandGate. 
# NandGates work like AndGates that have a Not attached to the output. 
class NandGate(AndGate):
    def performGateLogic(self):
        if super().performGateLogic() == 1:
            return 0
        else:
            return 1

        
        
# NorGates work lake OrGates that have a Not attached to the output.
class NorGate(OrGate):    
    def performGateLogic(self):
        if super().performGateLogic() == 1:
            return 0
        else:
            return 1

        
# In order to create a circuit, we need to connect gates together, the output of one flowing into the input of another.
# We need to implement a classed called Connector.
# HAS-A Relationship uses the gate hierarchy in that each connector will have two gates. (no inheritance)

# Connector class HAS-A LogicGate
class Connector:
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self) # Important for making connections

    def getFrom(self):
        return self.fromgate
    
    def getTo(self):
        return self.togate



test1 = AndGate("try1") # AndGet object, 'test1'. Internal label, 'try1'
# print(test1.getOutput())

test2 = OrGate("try2")
# print(test2.getOutput())

test3 = NotGate("try3")
# print(test3.getOutput())

t1 = AndGate('T1')
t2 = AndGate('T2')
t3 = OrGate("T3")
t4 = NotGate("T4")

# Outputs of both AND gates are connected to the OR gate
c1 = Connector(t1,t3) # AndGate to OrGate
c2 = Connector(t2,t3) # AndGate to OrGate

# Outputs of OR gate is connected to NOT gate
c3 = Connector(t3,t4) # OrGate to NotGate

# Output from the NOT gate is the output of the entire circuit

#print(t4.getOutput())

testing1 = AndGate("testing1")
testing2 = NandGate("testing2")
print(testing2.getOutput())