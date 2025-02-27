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
god_of_creation = Job("God of Creation")
god_of_destruction = Job("God of Destruction")
god_of_light = Job("God of Light")
god_of_time = Job("God of Time")
god_of_life = Job("God of Life")
god_of_darkness = Job("God of Darkness")
god_of_chaos = Job("God of Chaos")
god_of_death = Job("God of Death")
god_of_all = Job("God of All")
guardian_of_bahhana = Job("Guardian of None")
guardian_of_the_sky = Job("Guardian of sum")
guardian_of_the_land = Job("Guardian of sum")
guardian_of_the_sea = Job("Guardian of sum")
guardian_of_jathal = Job("Guardian of sum")
guardian_of_shogrinn = Job("Guardian of sum")
god_of_sum = Job("God of sum")
god_of_law = Job("God of Law")
god_of_war = Job("God of War")
god_of_knowledge = Job("God of Knowledge")
god_of_magic = Job("God of Magic")
god_of_love = Job("God of Love")
god_of_crafts = Job("God of Crafts")
god_of_dreams = Job("God of Dreams")
god_of_trade = Job("God of Trade")
god_of_luck = Job("God of Luck")
god_of_hunting = Job("God of Hunting")
god_of_medicine = Job("God of Medicine")
god_of_pride = Job("God of sum")
god_of_wrath = Job("God of sum")
god_of_forbidden_knowledge = Job("God of sum")
god_of_witchcraft = Job("God of sum")
god_of_lust = Job("God of sum")
god_of_sloth = Job("God of sum")
god_of_nightmares = Job("God of sum")
god_of_greed = Job("God of sum")
god_of_misfortune = Job("God of sum")
god_of_gluttony = Job("God of sum")
god_of_envy = Job("God of sum")
god_of_sum = Job("God of sum")
god_of_sum = Job("God of sum")
god_of_sum = Job("God of sum")
god_of_sum = Job("God of sum")
god_of_sum = Job("God of sum")
god_of_sum = Job("God of sum")
god_of_sum = Job("God of sum")
god_of_sum = Job("God of sum")
god_of_sum = Job("God of sum")
god_of_sum = Job("God of sum")

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