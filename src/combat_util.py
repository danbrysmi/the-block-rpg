# fighter class
# generic template for either a player or enemy in a fight

class Fighter():

    def __init__(self, stats):
        self.hp = stats[0]
        self.maxhp = stats[0]
        self.name = stats[1]
        self.mp = stats[2]
        self.maxmp = stats[2]

    def __str__(self):
        return f"""
{"-"*16}
{self.name}
HP: {self.hp}/{self.maxhp}
MP: {self.mp}/{self.maxmp}
{"-"*16} """


class Hero(Fighter): #player controlled Fighter

    def __init__(self, stats):
        super().__init__(stats)

class Enemy(Fighter):

    def __init__(self, stats):
        super().__init__(stats)
        self.mp = 0
        self.maxmp = 0

    def __str__(self):
        return f"""
{"-"*16}
{self.name}
HP: {self.hp}/{self.maxhp}
{"-"*16} """

s = [2, "Dan", 2]

f = Fighter(s)
h = Hero(s)
e = Enemy(s)
print(f)
print(h)
print(e)
