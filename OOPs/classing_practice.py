class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def introduction(self):
        return f"Hey, my name is {self.name} and I am level {self.level}"
    
    def levelup(self):
        self.level+=1
        return self.level

player1 = Player("Jeff", 20)
player2 = Player("Louie", 50)
player3 = Player("Danny", 60)
print(player1.introduction())
print(player1.levelup())
