# NPC Callings

# Titles
class Title:
    loadlist = []

    def __init__(self, name):
        self.name = name
        Title.loadlist.append(self)
    
    def __repr__(self):
        return f"{self.name}"

# Initialized Titles
voyager = Title("Voyager")

# ----------------------------------------------------------------------------------------------------------------------------------------------------------

# Jobs
class Job:
    loadlist = []

    def __init__(self, name):
        self.name = name
        Title.loadlist.append(self)

    def __repr__(self):
        return f"{self.name}"

# Initialized Jobs
unemployed = Job("Unemployed")

# ----------------------------------------------------------------------------------------------------------------------------------------------------------

# Ambitions
# 2 stats boost + 2 focus-related skills
class Ambition:
    loadlist = []

    def __init__(self, name, attribute1, attribute2, attribute3):
        self.name = name
        self.attribute1 = attribute1
        self.attribute2 = attribute2
        self.attribute3 = attribute3
        Title.loadlist.append(self)

    def __repr__(self):
        return f"{self.name}"

# Initialized Ambitions
# STR-based (1)
adventuring = Ambition("Adventuring", 1, None, None)
hired_hand = Ambition("Hired Hand", 1, None, None)

# DEF-based (2)
honorable = Ambition("Honorable", 2, None, None)

# SPD-based (3)
slaying = Ambition("Slaying", 3, None, None)

# AGI-based (4)
unlawful = Ambition("Unlawful", 4, None, None)

# PRO-based (5)
craftful = Ambition("Craftful", 5, None, None)
athletic = Ambition("Athletic", 5, None, None)

# MAG-based (6)
mystical = Ambition("Mystical", 6, None, None) # int

# CHR-based (7)
political = Ambition("Political", 7, None, None)
faithful = Ambition("Faithful", 7, None, None)

# INT-based (8)
academic = Ambition("Academic", 8, None, None)
innovative = Ambition("Innovative", 8, None, None) # pro

# FRT-based (9)
sailing = Ambition("Sailing", 9, None, None)
survival = Ambition("Survival", 9, None, None)

# LUC-based (10)
mercantile = Ambition("Mercantile", 10, None, None)