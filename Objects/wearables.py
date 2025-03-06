# Wearables
import items

class Wearable(items.Item):
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
                 "description", [items.Item.wearable_tag,items.Item.head_tag])
        
earring = Earwear("Helmet", "Basic Iron Helmet", Earwear.d_grade, Earwear.durable, None, None, None, None, None, None, None, None, None, 
                 "description", [items.Item.wearable_tag,items.Item.ear_tag])
        
glasses = Eyewear("Helmet", "Basic Iron Helmet", Eyewear.d_grade, Eyewear.durable, None, None, None, None, None, None, None, None, None, 
                 "description", [items.Item.wearable_tag,items.Item.eye_tag])
        
chain = Neckwear("Helmet", "Basic Iron Helmet", Neckwear.d_grade, Neckwear.durable, None, None, None, None, None, None, None, None, None, 
                 "description", [items.Item.wearable_tag,items.Item.neck_tag])
        
cape = Shoulderwear("Helmet", "Basic Iron Helmet", Shoulderwear.d_grade, Shoulderwear.durable, None, None, None, None, None, None, None, None, None, 
                 "description", [items.Item.wearable_tag,items.Item.shoulder_tag])
        
backpack = Backwear("Helmet", "Basic Iron Helmet", Backwear.d_grade, Backwear.durable, None, None, None, None, None, None, None, None, None, 
                 "description", [items.Item.wearable_tag,items.Item.back_tag])
        
chestplate = Chestwear("Helmet", "Basic Iron Helmet", Chestwear.d_grade, Chestwear.durable, None, None, None, None, None, None, None, None, None, 
                 "description", [items.Item.wearable_tag,items.Item.chest_tag])

sleeve = Armwear("Helmet", "Basic Iron Helmet", Armwear.d_grade, Armwear.durable, None, None, None, None, None, None, None, None, None, 
                 "description", [items.Item.wearable_tag,items.Item.arm_tag])

bracelet = Wristwear("Helmet", "Basic Iron Helmet", Wristwear.d_grade, Wristwear.durable, None, None, None, None, None, None, None, None, None, 
                 "description", [items.Item.wearable_tag,items.Item.wrist_tag])

gloves = Handwear("Helmet", "Basic Iron Helmet", Handwear.d_grade, Handwear.durable, None, None, None, None, None, None, None, None, None, 
                 "description", [items.Item.wearable_tag,items.Item.hand_tag])
        
ring = Fingerwear("Helmet", "Basic Iron Helmet", Fingerwear.d_grade, Fingerwear.durable, None, None, None, None, None, None, None, None, None, 
                 "description", [items.Item.wearable_tag,items.Item.finger_tag])
        
belt = Waistwear("Helmet", "Basic Iron Helmet", Waistwear.d_grade, Waistwear.durable, None, None, None, None, None, None, None, None, None, 
                 "description", [items.Item.wearable_tag,items.Item.waist_tag])
        
plate_pants = Legwear("Helmet", "Basic Iron Helmet", Legwear.d_grade, Legwear.durable, None, None, None, None, None, None, None, None, None, 
                 "description", [items.Item.wearable_tag,items.Item.leg_tag])
        
boots = Footwear("Helmet", "Basic Iron Helmet", Footwear.d_grade, Footwear.durable, None, None, None, None, None, None, None, None, None, 
                 "description", [items.Item.wearable_tag,items.Item.foot_tag])