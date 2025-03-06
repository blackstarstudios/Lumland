# Monsters

class Monsters:
    def __init__(self, name, hp, atk, exp, loot):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.exp = exp
        self.loot = loot

slime = Monsters("Slime", 30, 2, 10, 12)
goblin = Monsters("Goblin", 15, 3, 5, 8)
orc = Monsters("Orc", 35, 5, 20, 18)
dragon = Monsters("Dragon", 100, 8, 50, 100)