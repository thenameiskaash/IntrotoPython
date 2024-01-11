class LogicGate:
    def __init__(self,name):
        self.name = name
        self.output = None
    
    def GetName(self):
        return self.name
    
    def GetOutput(self):
        self.output = self.GetResult()
        return self.output
    
class BinaryGate(LogicGate):
    def __init__(self, name):
        super(BinaryGate, self).__init__(name)
    
        self.pina = None
        self.pinb = None
    
    def PinA(self):
        if self.pina == None:
            return int(input(f"Enter for the value for {self.name} : "))
        else:
            return self.pina.getfrom().GetOutput()
    
    def PinB(self):
        if self.pinb == None:
            return int(input(f"Enter for the value for {self.name} : "))
        else:
            return self.pinb.getfrom().GetOutput()
    
    def NextPin(self, source):
        if self.pina == None:
            self.pina = source
        elif self.pinb == None:
            self.pinb = source
        else:
            raise "An Error has occured"
        
class AndGate(BinaryGate):
    def __init__(self,name):
        super(AndGate, self).__init__(name)
    
    def GetResult(self):
        a = self.PinA()
        b = self.PinB()

        if a == 1 and b == 1:
            return 1
        else:
            return 0
    
class OrGate(BinaryGate):
    def __init__(self,name):
        super(OrGate,self).__init__(name)

    def GetResult(self):
        a = self.PinA()
        b = self.PinB()

        if a == 1 or b == 1:
            return 1
        else:
            return 0

class Connector:
    def __init__(self, fgate, tgate):
        self.fgate = fgate
        self.tgate = tgate

        tgate.NextPin(self)

    def getfrom(self):
        return self.fgate
    
    def getto(self):
        return self.tgate

    

        
andna = AndGate("AndGate")
oro = OrGate("OrGate")

connecting = Connector(andna, oro)

print(oro.GetOutput())