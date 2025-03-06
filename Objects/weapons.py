# Weapons
import items

class Weapon(items.Item):
    def __init__(self, name, technicalName, grade, condition, dmg, prot, effect1, effect2, effect3, enhance1, enhance2, enhance3, enchant1, 
                 enchant2, enchant3, description, itemTag):
        super().__init__(name, technicalName, grade, itemTag, condition, description)
        self.dmg = dmg
        self.prot = prot
        self.effect1 = effect1
        self.effect2 = effect2
        self.effect3 = effect3
        self.enhance1 = enhance1
        self.enhance2 = enhance2
        self.enhance3 = enhance3
        self.enchant1 = enchant1
        self.enchant2 = enchant2
        self.enchant3 = enchant3

iron_sword = Weapon("Iron Sword", "Basic Iron Sword", Weapon.c_grade, Weapon.undamaged, 10, 1, None, None, None, None, None, None, None, None, None, 
               "A poorly made iron sword", [items.Item.weapon_tag, items.Item.sword_tag])
iron_dagger = Weapon("Iron Dagger", "Basic Iron Dagger", Weapon.d_grade, Weapon.durable, 5, 0, None, None, None, None, None, None, None, None, 
               None, "A poorly made iron dagger", [items.Item.weapon_tag, items.Item.knife_tag])