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

first_demon_monarch = Title("Voyager")
cursed_god = Title("Voyager")
calamity_cold = Title("Voyager")
fallen_archangel = Title("Voyager")
last_carnic_beast = Title("Voyager")
bellowvin = Title("Voyager")
ending_tree = Title("Voyager")
dishonored_majin = Title("Voyager")
demigod_of_wrath = Title("Voyager")
unpure_flame = Title("Voyager")
bloodletter = Title("Voyager")
undeniable_queen = Title("Voyager")
wandering_mist = Title("Voyager")
moving_mountain = Title("Voyager")
restless_king = Title("Voyager")
froric_pillar = Title("Voyager")

dueling_king = Title("Voyager")
first_sword = Title("Voyager")
low_king = Title("Voyager")
branch_of_guidance = Title("Voyager")
branch_of_judgment = Title("Voyager")
king_mountain = Title("Voyager")
golem_slayer = Title("Voyager")
marquis = Title("Voyager")
puppet_king = Title("Voyager")
serrated_fin = Title("Voyager")
grand_sun = Title("Voyager")
rising_star = Title("Voyager")
endside = Title("Voyager")
crimson_king = Title("Voyager")
northern_beast = Title("Voyager")
whiteheart = Title("Voyager")
horus_chronus = Title("Voyager")
glacious = Title("Voyager")
honorable_lord = Title("Voyager")
honorable_general = Title("Voyager")
clean_blade = Title("Voyager")
apexalon = Title("Voyager")
man_of_prey = Title("Voyager")
striped_fang = Title("Voyager")
devil_king = Title("Voyager")
black_middle = Title("Voyager")
greech_wing = Title("Voyager")
whistling_spear = Title("Voyager")
golden_saintius = Title("Voyager")
knight_in_white = Title("Voyager")
yethseyer = Title("Voyager")
armored_dragon = Title("Voyager")
mr_proprietor = Title("Voyager")
death_stomp = Title("Voyager")
light_mind = Title("Voyager")
eight_headed_demon = Title("Voyager")
king_of_hundred_treasures = Title("Voyager")
door_of_colmere = Title("Voyager")
red_sea = Title("Voyager")
captain_killer = Title("Voyager")
white_death = Title("Voyager")
light_of_retribution = Title("Voyager")
smiling_swordsman = Title("Voyager")
heavy_heart = Title("Voyager")
sanguinica = Title("Voyager")
ringmaster = Title("Voyager")
little_god = Title("Voyager")


great_march = Title("Voyager")
low_tide = Title("Voyager")
raging_breath = Title("Voyager")
dragon_ancestor = Title("Voyager")
purecrown = Title("Voyager")
nightwalker = Title("Voyager")
hidden_expanse = Title("Voyager")
first_watcher = Title("Voyager")
over_march = Title("Voyager")
tidal_abyss = Title("Voyager")
raging_zephyr = Title("Voyager")
noble_lineage = Title("Voyager")
shining_crown = Title("Voyager")
twilight_walk = Title("Voyager")
pharid_eye = Title("Voyager")
name = Title("Voyager")
name = Title("Voyager")
name = Title("Voyager")
name = Title("Voyager")
name = Title("Voyager")
name = Title("Voyager")
name = Title("Voyager")
name = Title("Voyager")
name = Title("Voyager")
name = Title("Voyager")
name = Title("Voyager")
name = Title("Voyager")
name = Title("Voyager")
name = Title("Voyager")

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