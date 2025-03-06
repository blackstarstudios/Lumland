# Characters

#  RACE NAME  |   HP   AP   MP   SP  |  STR   DEF   SPD   AGI   PRO   MAG   CHR   INT   FRT   LUC
#-------------|----------------------|-----------------------------------------------------------
# Giants      |  125  100  025  050  |  150   150   025   025   025   025   025   050   125   100 farmers
# Orcs        |  100  100  025  075  |  150   150   125   025   100   025   025   025   050   025 warriors 
# Ogres       |  100  100  050  050  |  150   125   025   050   150   025   100   025   025   025 soldiers
# Crusikin    |  100  100  075  025  |  150   150   025   025   125   025   025   050   100   025
# Lepokin     |  075  050  025  150  |  100   025   150   150   125   025   025   050   025   025
# Bovikin     |  100  050  050  100  |  025   150   025   025   025   150   050   100   125   025
# Insikin     |  100  100  050  050  |  150   100   025   025   125   025   025   050   150   025
# Primikin    |  050  100  050  100  |  050   025   025   150   150   025   100   125   025   025
# Rodikin     |  075  075  025  125  |  050   125   025   150   025   025   025   100   125   050
# Amphikin    |  100  075  050  100  |  150   025   025   025   050   150   025   125   100   025
# Marikin     |  075  100  025  100  |  050   150   150   100   025   025   125   025   025   025
# Humans      |  100  050  050  100  |  150   100   025   025   150   050   125   025   025   025
# Canikin     |  100  075  025  100  |  150   125   125   050   100   025   025   025   050   025
# Felikin     |  075  100  025  100  |  150   025   100   150   025   025   025   125   025   050
# Replikin    |  100  100  075  025  |  150   025   025   100   050   150   025   125   025   025
# Avikin      |  075  100  025  100  |  100   025   150   125   050   025   025   150   025   025 
# Orsikin     |  100  100  025  075  |  150   150   100   025   050   025   025   025   125   025
# Suikin      |  100  075  025  100  |  125   150   150   025   025   025   025   050   025   100
# Taurikin    |  100  100  025  075  |  125   150   150   025   100   025   025   025   050   025 
# Aquakin     |  100  050  050  100  |  125   025   100   150   025   050   025   150   025   025 
# Elves       |  050  050  100  100  |  100   025   050   150   025   150   025   125   025   025 magicians / archers
# Dwarves     |  100  100  050  050  |  100   150   025   025   150   025   025   025   125   050 blacksmiths / tanks / heavy
# Goblins     |  050  100  025  125  |  050   025   025   100   025   025   150   150   025   125 merchants / 
# Faries      |  075  025  100  100  |  050   025   025   150   025   150   100   025   025   125 alchemists

#-------------------------------

class Character:
    def __init__(self, name, gender, race, title, job, aspiration,
                 HP, HPMAX, AP, APMAX, MP, MPMAX, SP, SPMAX, LVL, EXP, EXPMAX, REP, 
                 STR, DEF, SPD, AGI, PRO, MAG, CHR, INT, FRT, LUC, 
                 primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, 
                 inventory, lums, x, y):
        self.name = name
        self.gender = gender
        self.race = race
        self.title = title
        self.job = job
        self.aspiration = aspiration
        self.HP = HP
        self.HPMAX = HPMAX
        self.AP = AP
        self.APMAX = APMAX
        self.MP = MP
        self.MPMAX = MPMAX
        self.SP = SP
        self.SPMAX = SPMAX
        self.LVL = LVL
        self.EXP = EXP
        self.EXPMAX = EXPMAX
        self.REP = REP
        self.STR = STR
        self.DEF = DEF
        self.SPD = SPD
        self.AGI = AGI
        self.PRO = PRO
        self.MAG = MAG
        self.CHR = CHR
        self.INT = INT
        self.FRT = FRT
        self.LUC = LUC
        self.primary = primary 
        self.secondary = secondary
        self.head = head
        self.ears = ears
        self.eyes = eyes
        self.neck = neck
        self.shoulders = shoulders 
        self.back = back
        self.chest = chest
        self.arms = arms
        self.wrist = wrist
        self.hands = hands
        self.fingers = fingers
        self.waist = waist
        self.legs = legs
        self.feet = feet
        self.inventory = inventory
        self.lums = lums
        self.x = x
        self.y = y

    male = 'M'
    female = 'F'
    other = 'O'
    none = 'N'

    supreme_star = "Supreme Star"
    primeval_star = "Primeval Star"
    prime_star = "Prime Star"
    high_star = "High Star"
    low_star = "Low Star"
    half_star = "Half Star"

    azurean = "Azurean"
    ivor = "Ivor" 
    hunyadi = "Hunyadi"
    laudquin = "Laudquin"
    carmissean = "Carmissean"
    tearan = "Tearan"
    parakere = "Parakere"
    marron = "Marron"

    giant = "Giant"
    orc = "Orc"
    ogre = "Ogre"
    elf = "Elf"
    dwarf = "Dwarf"
    goblin = "Goblin"
    fairy = "Fairy"

    canikin = "Canikin"
    felikin = "Felikin"
    replikin = "Replikin"
    aquakin = "Aquakin"
    avikin = "avikin"
    bovikin = "Bovikin"
    orsikin = "Orsikin"
    taurkin = "Taurkin"
    insikin = "Insikin"
    lepokin = "Lepokin"
    primikin = "Primikin"
    crusikin = "Crusikin"
    rodikin = "Rodikin"
    amphikin = "Amphikin"
    marekin = "Marekin"
    suikin = "suikin"