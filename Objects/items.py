# Items

class Item:
    def __init__(self, name, technicalName, grade, condition, description, itemTag):
        self.name = name
        self.technicalName = technicalName
        self.grade = grade
        self.itemTag = itemTag
        self.condition = condition
        self.description = description

    # Grades
    u_grade = "U"
    sp_grade = "S+"
    s_grade = "S"
    a_grade = "A"
    b_grade = "B"
    c_grade = "C"
    d_grade = "D"
    f_grade = "F"

    # Condition    
    pristine = 1.0
    undamaged = 0.9
    durable = 0.8
    tested = 0.7
    blemished = 0.6
    worn = 0.5
    damaged = 0.4
    weakened = 0.3
    fragile = 0.2
    compromised = 0.1
    unusable = 0

    # Effects
    pHP = 10
    ppHP = 20
    pAP = 10
    ppAP = 20
    pMP = 10
    ppMP = 20
    pSP = 10
    ppSP = 20

    pSTR = 10
    pDEF = 10
    pSPD = 10
    pAGI = 10
    pPRO = 10
    pMAG = 10
    pCHR = 10
    pINT = 10
    pFRT = 10
    pLUC = 10

    # Item tags
    weapon_tag = "0000"
    sword_tag = "0001"
    knife_tag = "0002"
    potion_tag = "0003"
    health_tag = "0004"
    magic_tag = "0005"
    wearable_tag = "0006"
    head_tag = "0007"
    ear_tag = "0008"
    eye_tag = "0009"
    neck_tag = "0010"
    shoulder_tag = "0011" 
    back_tag = "0012"
    chest_tag = "0013"
    arm_tag = "0014"
    wrist_tag = "0015"
    hand_tag = "0016"
    finger_tag = "0017"
    waist_tag = "0018"
    leg_tag = "0019"
    foot_tag = "0020"

# Consumables
class Consumable(Item):
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
                 None, "Potion that heals you 10% of your health", [Item.potion_tag, Item.health_tag])
basic_mp_potion = Potion("Mana Potion", "Basic Mana Potion", Potion.d_grade, Potion.undamaged, Potion.pMP, None, None, None, None, None, None, None, 
                 None, "Potion that heals you 10% of your mana", [Item.potion_tag, Item.magic_tag])

# Wearables
class Wearable(Item):
    def __init__(self, name, technicalName, grade, condition, effect1, effect2, effect3, enhance1, enhance2, enhance3, enchant1, enchant2, enchant3, 
                 description, itemTag):
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

class Headwear(Wearable):
    def __init__(self, name, technicalName, grade, condition, effect1, effect2, effect3, enhance1, enhance2, enhance3, enchant1, enchant2, enchant3, 
                 description, itemTag):
        super().__init__(name, technicalName, grade, condition, effect1, effect2, effect3, enhance1, enhance2, enhance3, enchant1, enchant2, enchant3, 
                 description, itemTag)
        
class Earwear(Wearable):
    def __init__(self, name, technicalName, grade, condition, effect1, effect2, effect3, enhance1, enhance2, enhance3, enchant1, enchant2, enchant3, 
                 description, itemTag):
        super().__init__(name, technicalName, grade, condition, effect1, effect2, effect3, enhance1, enhance2, enhance3, enchant1, enchant2, enchant3, 
                 description, itemTag)
        
class Eyewear(Wearable):
    def __init__(self, name, technicalName, grade, condition, effect1, effect2, effect3, enhance1, enhance2, enhance3, enchant1, enchant2, enchant3, 
                 description, itemTag):
        super().__init__(name, technicalName, grade, condition, effect1, effect2, effect3, enhance1, enhance2, enhance3, enchant1, enchant2, enchant3, 
                 description, itemTag)
        
class Neckwear(Wearable):
    def __init__(self, name, technicalName, grade, condition, effect1, effect2, effect3, enhance1, enhance2, enhance3, enchant1, enchant2, enchant3, 
                 description, itemTag):
        super().__init__(name, technicalName, grade, condition, effect1, effect2, effect3, enhance1, enhance2, enhance3, enchant1, enchant2, enchant3, 
                 description, itemTag)
        
class Shoulderwear(Wearable):
    def __init__(self, name, technicalName, grade, condition, effect1, effect2, effect3, enhance1, enhance2, enhance3, enchant1, enchant2, enchant3, 
                 description, itemTag):
        super().__init__(name, technicalName, grade, condition, effect1, effect2, effect3, enhance1, enhance2, enhance3, enchant1, enchant2, enchant3, 
                 description, itemTag)
        
class Backwear(Wearable):
    def __init__(self, name, technicalName, grade, condition, effect1, effect2, effect3, enhance1, enhance2, enhance3, enchant1, enchant2, enchant3, 
                 description, itemTag):
        super().__init__(name, technicalName, grade, condition, effect1, effect2, effect3, enhance1, enhance2, enhance3, enchant1, enchant2, enchant3, 
                 description, itemTag)
        
class Chestwear(Wearable):
    def __init__(self, name, technicalName, grade, condition, effect1, effect2, effect3, enhance1, enhance2, enhance3, enchant1, enchant2, enchant3, 
                 description, itemTag):
        super().__init__(name, technicalName, grade, condition, effect1, effect2, effect3, enhance1, enhance2, enhance3, enchant1, enchant2, enchant3, 
                 description, itemTag)

class Armwear(Wearable):
    def __init__(self, name, technicalName, grade, condition, effect1, effect2, effect3, enhance1, enhance2, enhance3, enchant1, enchant2, enchant3, 
                 description, itemTag):
        super().__init__(name, technicalName, grade, condition, effect1, effect2, effect3, enhance1, enhance2, enhance3, enchant1, enchant2, enchant3, 
                 description, itemTag)

class Wristwear(Wearable):
    def __init__(self, name, technicalName, grade, condition, effect1, effect2, effect3, enhance1, enhance2, enhance3, enchant1, enchant2, enchant3, 
                 description, itemTag):
        super().__init__(name, technicalName, grade, condition, effect1, effect2, effect3, enhance1, enhance2, enhance3, enchant1, enchant2, enchant3, 
                 description, itemTag)

class Handwear(Wearable):
    def __init__(self, name, technicalName, grade, condition, effect1, effect2, effect3, enhance1, enhance2, enhance3, enchant1, enchant2, enchant3, 
                 description, itemTag):
        super().__init__(name, technicalName, grade, condition, effect1, effect2, effect3, enhance1, enhance2, enhance3, enchant1, enchant2, enchant3, 
                 description, itemTag)
        
class Fingerwear(Wearable):
    def __init__(self, name, technicalName, grade, condition, effect1, effect2, effect3, enhance1, enhance2, enhance3, enchant1, enchant2, enchant3, 
                 description, itemTag):
        super().__init__(name, technicalName, grade, condition, effect1, effect2, effect3, enhance1, enhance2, enhance3, enchant1, enchant2, enchant3, 
                 description, itemTag)
        
class Waistwear(Wearable):
    def __init__(self, name, technicalName, grade, condition, effect1, effect2, effect3, enhance1, enhance2, enhance3, enchant1, enchant2, enchant3, 
                 description, itemTag):
        super().__init__(name, technicalName, grade, condition, effect1, effect2, effect3, enhance1, enhance2, enhance3, enchant1, enchant2, enchant3, 
                 description, itemTag)
        
class Legwear(Wearable):
    def __init__(self, name, technicalName, grade, condition, effect1, effect2, effect3, enhance1, enhance2, enhance3, enchant1, enchant2, enchant3, 
                 description, itemTag):
        super().__init__(name, technicalName, grade, condition, effect1, effect2, effect3, enhance1, enhance2, enhance3, enchant1, enchant2, enchant3, 
                 description, itemTag)
        
class Footwear(Wearable):
    def __init__(self, name, technicalName, grade, condition, effect1, effect2, effect3, enhance1, enhance2, enhance3, enchant1, enchant2, enchant3, 
                 description, itemTag):
        super().__init__(name, technicalName, grade, condition, effect1, effect2, effect3, enhance1, enhance2, enhance3, enchant1, enchant2, enchant3, 
                 description, itemTag)
        
helmet = Headwear("Helmet", "Basic Iron Helmet", Headwear.d_grade, Headwear, None, None, None, None, None, None, None, None, None, 
                 "description", [Item.wearable_tag,Item.head_tag])
        
earring = Earwear("Helmet", "Basic Iron Helmet", Earwear.d_grade, Earwear.durable, None, None, None, None, None, None, None, None, None, 
                 "description", [Item.wearable_tag,Item.ear_tag])
        
glasses = Eyewear("Helmet", "Basic Iron Helmet", Eyewear.d_grade, Eyewear.durable, None, None, None, None, None, None, None, None, None, 
                 "description", [Item.wearable_tag,Item.eye_tag])
        
chain = Neckwear("Helmet", "Basic Iron Helmet", Neckwear.d_grade, Neckwear.durable, None, None, None, None, None, None, None, None, None, 
                 "description", [Item.wearable_tag,Item.neck_tag])
        
cape = Shoulderwear("Helmet", "Basic Iron Helmet", Shoulderwear.d_grade, Shoulderwear.durable, None, None, None, None, None, None, None, None, None, 
                 "description", [Item.wearable_tag,Item.shoulder_tag])
        
backpack = Backwear("Helmet", "Basic Iron Helmet", Backwear.d_grade, Backwear.durable, None, None, None, None, None, None, None, None, None, 
                 "description", [Item.wearable_tag,Item.back_tag])
        
chestplate = Chestwear("Helmet", "Basic Iron Helmet", Chestwear.d_grade, Chestwear.durable, None, None, None, None, None, None, None, None, None, 
                 "description", [Item.wearable_tag,Item.chest_tag])

sleeve = Armwear("Helmet", "Basic Iron Helmet", Armwear.d_grade, Armwear.durable, None, None, None, None, None, None, None, None, None, 
                 "description", [Item.wearable_tag,Item.arm_tag])

bracelet = Wristwear("Helmet", "Basic Iron Helmet", Wristwear.d_grade, Wristwear.durable, None, None, None, None, None, None, None, None, None, 
                 "description", [Item.wearable_tag,Item.wrist_tag])

gloves = Handwear("Helmet", "Basic Iron Helmet", Handwear.d_grade, Handwear.durable, None, None, None, None, None, None, None, None, None, 
                 "description", [Item.wearable_tag,Item.hand_tag])
        
ring = Fingerwear("Helmet", "Basic Iron Helmet", Fingerwear.d_grade, Fingerwear.durable, None, None, None, None, None, None, None, None, None, 
                 "description", [Item.wearable_tag,Item.finger_tag])
        
belt = Waistwear("Helmet", "Basic Iron Helmet", Waistwear.d_grade, Waistwear.durable, None, None, None, None, None, None, None, None, None, 
                 "description", [Item.wearable_tag,Item.waist_tag])
        
plate_pants = Legwear("Helmet", "Basic Iron Helmet", Legwear.d_grade, Legwear.durable, None, None, None, None, None, None, None, None, None, 
                 "description", [Item.wearable_tag,Item.leg_tag])
        
boots = Footwear("Helmet", "Basic Iron Helmet", Footwear.d_grade, Footwear.durable, None, None, None, None, None, None, None, None, None, 
                 "description", [Item.wearable_tag,Item.foot_tag])

# Weapons
class Weapon(Item):
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
               "A poorly made iron sword", [Item.weapon_tag, Item.sword_tag])
iron_dagger = Weapon("Iron Dagger", "Basic Iron Dagger", Weapon.d_grade, Weapon.durable, 5, 0, None, None, None, None, None, None, None, None, 
               None, "A poorly made iron dagger", [Item.weapon_tag, Item.knife_tag])