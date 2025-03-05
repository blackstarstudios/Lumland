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
        Title.loadlist.append(self)

    def __repr__(self):
        return f"{self.name}"

# Initialized Ambitions
# STR-based (1)
adventurer = Ambition("Adventurer", 1, None, None)
mercenary = Ambition("Mercenary", 1, None, None)

# DEF-based (2)
knight = Ambition("Knight", 2, None, None)

# SPD-based (3)
hunter = Ambition("Hunter", 3, None, None)

# AGI-based (4)
bandit = Ambition("Bandit", 4, None, None)

# PRO-based (5)
craftsman = Ambition("Craftsman", 5, None, None)
duelist = Ambition("Duelist", 5, None, None)

# MAG-based (6)
magician = Ambition("Magician", 6, None, None) # int

# CHR-based (7)
aristicrat = Ambition("Aristicrat", 7, None, None)
priest = Ambition("Priest", 7, None, None)

# INT-based (8)
scholar = Ambition("Scholar", 8, None, None)
engineer = Ambition("Engineer", 8, None, None) # pro

# FRT-based (9)
sailor = Ambition("Sailor", 9, None, None)
outdoorsman = Ambition("Outdoorsman", 9, None, None)

# LUC-based (10)
merchant = Ambition("Merchant", 10, None, None)