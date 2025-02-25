import items

class Weapon(Item):
    def __init__(self, name, technicalName, grade, itemType, condition, effect1, effect2, effect3, enhance1, enhance2, enhance3, enchant1, enchant2, enchant3, description, baseATK, baseDEF):
        super().__init__(name, technicalName, grade, itemType, condition, effect1, effect2, effect3, enhance1, enhance2, enhance3, enchant1, enchant2, enchant3, description)
        self.baseATK = baseATK
        self.baseDEF = baseDEF