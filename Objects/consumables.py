# Consumables
import items

class Consumable(items.Item):
    def __init__(self, name, technicalName, grade, condition, effect1, effect2, effect3, enhance1, enhance2, enhance3, enchant1, enchant2, 
                 enchant3, description, itemTag):
        super().__init__(name, technicalName, grade, condition, description, itemTag)
        self.effect1 = effect1
        self.effect2 = effect2
        self.effect3 = effect3
        self.enhance1 = enhance1
        self.enhance2 = enhance2
        self.enhance3 = enhance3
        self.enchant1 = enchant1
        self.enchant2 = enchant2
        self.enchant3 = enchant3

class Food(Consumable):
    def __init__(self, name, technicalName, grade, condition, effect1, effect2, effect3, enhance1, enhance2, enhance3, enchant1, enchant2, 
                 enchant3, description, itemTag):
        super().__init__(name, technicalName, grade, condition, effect1, effect2, effect3, enhance1, enhance2, enhance3, enchant1, enchant2, 
                 enchant3, description, itemTag)

class Potion(Consumable):
    def __init__(self, name, technicalName, grade, condition, effect1, effect2, effect3, enhance1, enhance2, enhance3, enchant1, enchant2, 
                 enchant3, description, itemTag):
        super().__init__(name, technicalName, grade, condition, effect1, effect2, effect3, enhance1, enhance2, enhance3, enchant1, enchant2, 
                 enchant3, description, itemTag)
        
basic_hp_potion = Potion("Health Potion", "Basic Health Potion", Potion.d_grade, Potion.undamaged, Potion.pHP, None, None, None, None, None, None, None, 
                 None, "Potion that heals you 10% of your health", [items.Item.potion_tag, items.Item.health_tag])
basic_mp_potion = Potion("Mana Potion", "Basic Mana Potion", Potion.d_grade, Potion.undamaged, Potion.pMP, None, None, None, None, None, None, None, 
                 None, "Potion that heals you 10% of your mana", [items.Item.potion_tag, items.Item.magic_tag])