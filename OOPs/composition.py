class Respository:
    def __init__(self):
        self.packages = {} # <-Dictionary
    def add_packages(self, package): #<- Method
        self.packages[package.name] = package
    def remove_packeges(self, package):
        self.packages[package.name] = package
    def total_size(self):
        result = 0 
        for package in self.packages.values():
            result += package.size
        return result