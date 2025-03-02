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
the_beginning = Title("The Beginning")
daystar = Title("Daystar")
newstar = Title("Newstar")
the_end = Title("The End")
nightstar = Title("Nightstar")
endstar = Title("Endstar")
the_god_of_all = Title("God of All")
allstar = Title("Allstar")
supreme_ones_seal = Title("Supreme One's Seal")
archangel = Title("Archangel")
lightstar = Title("Lightstar")
father_time = Title("Father Time")
timestar = Title("Timestar")
allmother = Title("Allmother")
lifestar = Title("Lifestar")
the_god_of_none = Title("God of None")
antistar = Title("Antistar")
mark_of_the_end = Title("Mark of the End")
dark_prince = Title("Dark Prince")
darkstar = Title("Darkstar")
chaos_incarnate = Title("Chaos Incarnate")
chaostar = Title("Chaostar")
the_reaper = Title("The Reaper")
deathstar = Title("Deathstar")
holy_steed = Title("Holy Steed")
the_one_who_claims_the_sky = Title("The One Who Claims the Sky")
king_of_earth = Title("King of Earth")
wonder_of_the_depths = Title("Wonder of the Depths")
living_prison = Title("Living Prision")
gatekeeper_to_hell = Title("Gatekeeper to Hell")
final_judge = Title("Final Judge")
lawstar = Title("Lawstar")
god_of_war = Title("God of War")
ironstar = Title("Ironstar")
gemini = Title("Gemini")
wisestar = Title("Wisestar")
grand_magiciana = Title("Grand Magicana")
magistar = Title("Magistar")
mother_hearth = Title("Mother Hearth")
lovestar = Title("Lovestar")
holysmith = Title("Holysmith")
firestar = Title("Firestar")
tranqoui = Title("Tranqoui")
cloudstar = Title("Cloudstar")
grand_merchant = Title("Grand Merchant")
tradestar = Title("Tradestar")
saint_fortune = Title("Saint Fortune")
luckstar = Title("Luckstar")
goddess_of_the_hunt = Title("Goddess of the Hunt")
huntstar = Title("Huntstar")
the_blessed_healer = Title("The Blessed Healer")
medstar = Title("Medstar")
sin_of_pride = Title("Sin of Pride")
egostar = Title("Egostar")
sin_of_wrath = Title("Sin of Wrath")
wrathstar = Title("Wrathstar")
sin_of_the_forbidden = Title("Sin of the Forbidden")
courruptstar = Title("Corruptstar")
witch_of_the_damned = Title("Witch of the Damned")
witchstar = Title("Witchstar")
sin_of_lust = Title("Sin of Lust")
luststar = Title("Luststar")
sin_of_sloth = Title("Sin of Sloth")
slothstar = Title("Slothstar")
night_conjurer = Title("Night Conjurer")
marestar = Title("Marestar")
father_greed = Title("Father Greed")
greedstar = Title("Greedstar")
the_unlucky_one = Title("Unlucky One")
badstar = Title("Badstar")
voracion = Title("Voracion")
vourstar = Title("Vourstar")
the_envious = Title("The Envious")
envystar = Title("Envystar")

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
god_of_creation = Job("God of Creation")
goddess_of_destruction = Job("Goddess of Destruction")
god_of_all = Job("God of All")
goddess_of_light = Job("Goddess of Light")
god_of_time = Job("God of Time")
goddess_of_life = Job("Goddess of Life")
god_of_none = Job("God of None")
god_of_darkness = Job("God of Darkness")
god_of_chaos = Job("God of Chaos")
goddess_of_death = Job("Goddess of Death")
guardian_of_bahhana = Job("Guardian of Bahhana")
guardian_of_the_sky = Job("Guardian of the Sky")
guardian_of_the_land = Job("Guardian of Land")
guardian_of_the_sea = Job("Guardian of Sea")
guardian_of_jathal = Job("Guardian of Jathal")
guardian_of_shogrinn = Job("Guardian of Shogrinn")
god_of_law = Job("God of Law")
god_of_war = Job("God of War")
god_of_knowledge = Job("God of Knowledge")
god_of_magic = Job("God of Magic")
goddess_of_love = Job("Goddess of Love")
god_of_crafts = Job("God of Crafts")
god_of_dreams = Job("God of Dreams")
god_of_trade = Job("God of Trade")
god_of_luck = Job("God of Luck")
goddess_of_hunting = Job("Goddess of Hunting")
goddess_of_medicine = Job("Goddess of Medicine")
god_of_pride = Job("God of Pride")
god_of_wrath = Job("God of Wrath")
god_of_forbidden_knowledge = Job("God of Forbidden Knowledge")
goddess_of_witchcraft = Job("Goddess of Witchcraft")
god_of_lust = Job("God of Lust")
god_of_sloth = Job("God of Sloth")
goddess_of_nightmares = Job("Goddess of Nightmares")
god_of_greed = Job("God of Greed")
god_of_misfortune = Job("God of Misfortune")
god_of_gluttony = Job("God of Gluttony")
god_of_envy = Job("God of Envy")
unemployed = Job("Unemployed")
king = Job("King")
emperor = Job("Emperor")
knight = Job("Knight")
guildmaster = Job("Guildmaster")
sailor = Job("Sailor")
vigilante = Job("Vigilante")
mage = Job("Mage")
paladin = Job("Paladin")
chief = Job("Chieftian")
adventurer = Job("Adventurer")
elder = Job("Elder")
grand_elder = Job("Grand Elder")
keeper = Job("Keeper")
warrior = Job("Warrior")
ruler = Job("Ruler")
monarch = Job("Monarch")
maurader = Job("Maurader")
lordmage = Job("Lordmage")
guardmage = Job("Guardmage")
lord = Job("Lord")
general = Job("General")
samurai = Job("Samurai")
overlord = Job("Overlord")
queen = Job("Queen")
empress = Job("Empress")
guard = Job("Guard")
soverign = Job("Soverign")
guardineer = Job("Guardineer")
captain = Job("Captain")
gambler = Job("Gambler")
bandit = Job("Bandit")
mercenary = Job("Mercenary")
engineer = Job("Engineer")
aristocrat = Job("Aristocrat")
blacksmith = Job("Blacksmith")
hunter = Job("Hunter")
slayer = Job("Slayer")
outdoorsman = Job("Outdoorsman")
merchant = Job("Merchant")
priest = Job("Priest")
scholar = Job("Scholar")
student = Job("Student")
chef = Job("Chef")
artist = Job("Artist")
witch = Job("Witch")
runineer = Job("Runineer")
association_head = Job("Association Head")
master = Job("Master")
commander = Job("Commander")

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
adventuring = Ambition("Adventuring", 1, None, None)
hired_hand = Ambition("Hired Hand", 1, None, None)

# DEF-based (2)
honorable = Ambition("Honorable", 2, None, None)

# SPD-based (3)
slaying = Ambition("Slaying", 3, None, None)
hunting = Ambition("Hunting", 3, None, None)

# AGI-based (4)
unlawful = Ambition("Unlawful", 4, None, None)

# PRO-based (5)
crafting = Ambition("Crafting", 5, None, None)
dueling = Ambition("Dueling", 5, None, None)

# MAG-based (6)
magical = Ambition("Magical", 6, None, None) # int

# CHR-based (7)
political = Ambition("Political", 7, None, None)
faithful = Ambition("Faithful", 7, None, None)

# INT-based (8)
academic = Ambition("Academic", 8, None, None)
innovative = Ambition("Innovative", 8, None, None) # pro

# FRT-based (9)
Sailing = Ambition("sailing", 9, None, None)
survival = Ambition("Survival", 9, None, None)

# LUC-based (10)
economic = Ambition("Economic", 10, None, None)