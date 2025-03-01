#                                                                          LUMLAND                                                                            
# _____________________________________________________________________ BY BLACKSTAR. ________________________________________________________________________

# ====================================================================== LIBRARIES ===========================================================================

# Official Libraries
import sys, math, random, time
import os, _pickle as pickle
import Design.colors as colors

# Custom Libraries
# Abilites
import Abilities.magic as magic
import Abilities.battlearts as battlearts
import Abilities.skills as skills

# Items
import Items.materials as materials
import Items.consumables as consumables
import Items.equipment as equipment
#import Items.wearables as wearables
#import Items.weapons as weapons

# NPCs
import NPCs.monsters as monsters
import NPCs.characters as characters
import NPCs.callings as callings

# Locations

# ======================================================================== STATES ============================================================================

# Major Game States
run = True
menu = True
play = False
pause = False
options = False
rules = False

# Minor Game States
fight = False
buy = False
speak = False
inventory = False
status = False
craft = False
brew = False
enhance = False
enchant = False
boss = False

# ======================================================================== DESIGN ============================================================================

# Clear terminal
def clear(): os.system('cls' if os.name == 'nt' else 'clear') # cls - Windows; clear - Unix

# Write borderline
def bordl(): print("!=========================!")

# Write borderline
#def brdb():
#    print(" ")
#    print("!=====================================!")

# Write underline
def undrl(): print("________________")

# Write spaceline
def space(): print(" ")

# Write sectionline
def sectl(): print("+-----------------+")

# Healthbar display
bars = 20
remaining_stat_symbol = "█"
lost_stat_symbol = "_"

# Typewrite text
def typewrite(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

def storywrite(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    space()
    cont()

# ======================================================================== ITEMS =============================================================================



# ========================================================================= NPCS =============================================================================

e_list = ["Goblin", "Orc", "Slime"]

mobs = {
    "Goblin": {
        "hp": 15,
        "at": 3,
        "go": 8
    },
    "Orc": {
        "hp": 35,
        "at": 5,
        "go": 18
    },
    "Slime": {
        "hp": 30,
        "at": 2,
        "go": 12
    },
    "Dragon": {
        "hp": 100,
        "at": 8,
        "go": 100
    }
}

# ======================================================================= LOCATIONS ==========================================================================

        #  x = 0       x = 1       x = 2       x = 3       x = 4       x = 5         x = 6
map = [["plains",   "plains",   "plains",   "plains",   "forest", "mountain",       "cave"],    # y = 0
       ["forest",   "forest",   "forest",   "forest",   "forest",    "hills",   "mountain"],    # y = 1
       ["forest",   "fields",   "bridge",   "plains",    "hills",   "forest",      "hills"],    # y = 2
       ["plains",     "shop",     "town",    "mayor",   "plains",    "hills",   "mountain"],    # y = 3
       ["plains",   "fields",   "fields",   "plains",    "hills", "mountain",   "mountain"]]    # y = 4

y_len = len(map)-1
x_len = len(map[0])-1

biom = {
    "plains": {
        "t": "PLAINS",
        "e": True},
    "forest": {
        "t": "WOODS",
        "e": True},
    "fields": {
        "t": "FIELDS",
        "e": False},
    "bridge": {
        "t": "BRIGE",
        "e": True},
    "town": {
        "t": "TOWN CENTRE",
        "e": False},
    "shop": {
        "t": "SHOP",
        "e": False},
    "mayor": {
        "t": "MAYOR",
        "e": False},
    "cave": {
        "t": "CAVE",
        "e": False},
    "mountain": {
        "t": "MOUNTAIN",
        "e": True},
    "hills": {
        "t": "HILLS",
        "e": True,
    }
}

# ======================================================================== PLAYER ============================================================================

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

def characterCreation():
    clear()

    # intro
    storywrite("As you approach the landing dock you lay eyes on the new continent, Lumhuin, a land of swords and magic...")
    storywrite("*The boat finally docks and as you unboard the vessel, a guard stops you*")
    storywrite("Guard: Woah there Voyager, you must go through the Lumhuinian registrnation process for a new ID.")
    space()

    # Choose name
    name = input("Guard: What's your name Voyager? > ")
    print(f"You: My name is {name}.")
    storywrite(f"Guard: Nice to meet you {name}")

    # Choose gender
    storywrite("Guard: Your gender?")
    print("""Genders:
    1. Male
    2. Female""")
    option = int(input(" > "))
    if option == 1:
        gender = 'M'
        print("You: I'm male.")
    elif option == 2:
        gender = 'F'
        print("You: I'm female.")

    # Choose race
    storywrite("Guard: Now, what race are you?")
    print("""Races:
    1. Human -> An ambitious race
    2. Dwarf -> Short in stature, full of heart
    3. Orc -> Battle hardened warriors
    4. Beastman -> Half man, half beast
    5. Goblin -> Short green opprotunists
    6. Ogre -> Respected soldiers of culture
    7. Elf -> Graceful elders of nature
    8. Giant -> Large gentle farmers
    9. Fairy -> Mini beings of wonder 
     > """)
    option = int(input(" > "))
    
    match option:
        case 1:
            HP = 100
            AP = 50
            MP = 50
            SP = 100
            strn = 150
            defn = 100
            spd = 25
            agi = 25
            pro = 150
            mag = 50
            chri = 125
            intel = 25
            frt = 25
            luc = 25
            race = "Human"
        case 2:
            HP = 100
            AP = 100
            MP = 50
            SP = 50
            strn = 100
            defn = 150
            spd = 25
            agi = 25
            pro = 150
            mag = 25
            chri = 25
            intel = 25
            frt = 125
            luc = 50
            race = "Dwarf"
        case 3:
            HP = 100
            AP = 100
            MP = 25
            SP = 75
            strn = 150
            defn = 150
            spd = 125
            agi = 25
            pro = 100
            mag = 25
            chri = 25
            intel = 25
            frt = 50
            luc = 25
            race = "Orc"
        case 4:
            storywrite("Guard: Oh, Beastman are ya? Then what is your kin?")
            print("""Beastmen Races:
            1.  Canikin -> Pack hunters that wear down their target
            2.  Felikin -> Predators that always catch their prey
            3.  Replikin -> Age old lesser dragonkin
            4.  Aquakin -> Sea dwellers that maximize the depths
            5.  Avikin -> High flying eyes in the sky
            6.  Bovikin -> Horned grazers of the plains
            7.  Orsikin -> Cuddlers with a death grip
            8.  Taurkin -> Headstrnong fighters
            9.  Insikin -> Hard hard workers, strnong too
            10. Lepokin -> Quick and agile bouncers
            11. Primikin -> Rulers of the high trees
            12. Crusikin -> True born sailors, armor-plated is a bonus
            13. Rodikin -> Resilient little furballs
            14. Amphikin -> Slimy swamp lovers
            15. Marekin -> Steeds ready for battle 
            16. Suikin -> Piggly wigglies""")
            option = int(input(" > "))
            
            match option:
                case 1:
                    HP = 100
                    AP = 75
                    MP = 25
                    SP = 100
                    strn = 150
                    defn = 125
                    spd = 125
                    agi = 50
                    pro = 100
                    mag = 25
                    chri = 25
                    intel = 25
                    frt = 50
                    luc = 25
                    race = "Canikin"
                case 2:
                    HP = 75
                    AP = 100
                    MP = 25
                    SP = 100
                    strn = 150
                    defn = 25
                    spd = 100
                    agi = 150
                    pro = 25
                    mag = 25
                    chri = 25
                    intel = 125
                    frt = 25
                    luc = 50
                    race = "Felikin"
                case 3:
                    HP = 100
                    AP = 100
                    MP = 75
                    SP = 25
                    strn = 150
                    defn = 25
                    spd = 25
                    agi = 100
                    pro = 50
                    mag = 150
                    chri = 25
                    intel = 125
                    frt = 25
                    luc = 25
                    race = "Replikin"
                case 4:
                    HP = 100
                    AP = 50
                    MP = 50
                    SP = 100
                    strn = 125
                    defn = 25
                    spd = 100
                    agi = 150
                    pro = 25
                    mag = 50
                    chri = 25
                    intel = 150
                    frt = 25
                    luc = 25
                    race = "Aquakin"
                case 5:
                    HP = 75
                    AP = 100
                    MP = 25
                    SP = 100
                    strn = 100
                    defn = 25
                    spd = 150
                    agi = 125
                    pro = 50
                    mag = 25
                    chri = 25
                    intel = 150
                    frt = 25
                    luc = 25
                    race = "Avikin"
                case 6:
                    HP = 100
                    AP = 50
                    MP = 50
                    SP = 100
                    strn = 25
                    defn = 150
                    spd = 25
                    agi = 25
                    pro = 25
                    mag = 150
                    chri = 50
                    intel = 100
                    frt = 125
                    luc = 25
                    race = "Bovikin"
                case 7:
                    HP = 100
                    AP = 100
                    MP = 25
                    SP = 75
                    strn = 150
                    defn = 150
                    spd = 100
                    agi = 25
                    pro = 50
                    mag = 25
                    chri = 25
                    intel = 25
                    frt = 125
                    luc = 25
                    race = "Ursikin"
                case 8:
                    HP = 100
                    AP = 100
                    MP = 25
                    SP = 75
                    strn = 125
                    defn = 150
                    spd = 150
                    agi = 25
                    pro = 100
                    mag = 25
                    chri = 25
                    intel = 25
                    frt = 50
                    luc = 25
                    race = "Taurkin"
                case 9:
                    HP = 100
                    AP = 100
                    MP = 50
                    SP = 50
                    strn = 150
                    defn = 100
                    spd = 25
                    agi = 25
                    pro = 125
                    mag = 25
                    chri = 25
                    intel = 50
                    frt = 150
                    luc = 25
                    race = "Insikin"
                case 10:
                    HP = 75
                    AP = 50
                    MP = 25
                    SP = 150
                    strn = 100
                    defn = 25
                    spd = 150
                    agi = 150
                    pro = 125
                    mag = 25
                    chri = 25
                    intel = 50
                    frt = 25
                    luc = 25
                    race = "Lepokin"
                case 11:
                    HP = 50
                    AP = 100
                    MP = 50
                    SP = 100
                    strn = 50
                    defn = 25
                    spd = 25
                    agi = 150
                    pro = 150
                    mag = 25
                    chri = 100
                    intel = 125
                    frt = 25
                    luc = 50
                    race = "Primikin"
                case 12:
                    HP = 100
                    AP = 100
                    MP = 75
                    SP = 25
                    strn = 150
                    defn = 150
                    spd = 25
                    agi = 25
                    pro = 125
                    mag = 25
                    chri = 25
                    intel = 50
                    frt = 100
                    luc = 25
                    race = "Crusikin"
                case 13:
                    HP = 75
                    AP = 75
                    MP = 25
                    SP = 125
                    strn = 50
                    defn = 125
                    spd = 25
                    agi = 150
                    pro = 25
                    mag = 25
                    chri = 25
                    intel = 100
                    frt = 125
                    luc = 50
                    race = "Rodikin"
                case 14:
                    HP = 100
                    AP = 75
                    MP = 50
                    SP = 100
                    strn = 150
                    defn = 25
                    spd = 25
                    agi = 25
                    pro = 50
                    mag = 150
                    chri = 25
                    intel = 125
                    frt = 100
                    luc = 25
                    race = "Amphikin"
                case 15:
                    HP = 75
                    AP = 100
                    MP = 25
                    SP = 100
                    strn = 50
                    defn = 125
                    spd = 150
                    agi = 100
                    pro = 25
                    mag = 25
                    chri = 125
                    intel = 25
                    frt = 25
                    luc = 25
                    race = "Marekin"
                case 16:
                    HP = 100
                    AP = 75
                    MP = 25
                    SP = 100
                    strn = 125
                    defn = 150
                    spd = 150
                    agi = 25
                    pro = 25
                    mag = 25
                    chri = 25
                    intel = 50
                    frt = 25
                    luc = 100
                    race = "Suikin"
                case _:
                    print("Invalid option")
        case 5:
            HP = 50
            AP = 100
            MP = 25
            SP = 125
            strn = 50
            defn = 25
            spd = 25
            agi = 100
            pro = 25
            mag = 25
            chri = 150
            intel = 150
            frt = 25
            luc = 125
            race = "Goblin"
        case 6:
            HP = 100
            AP = 100
            MP = 50
            SP = 50
            strn = 150
            defn = 125
            spd = 25
            agi = 50
            pro = 150
            mag = 25
            chri = 100
            intel = 25
            frt = 25
            luc = 25
            race = "Ogre"
        case 7:
            HP = 50
            AP = 50
            MP = 100
            SP = 100
            strn = 100
            defn = 25
            spd = 50
            agi = 150
            pro = 25
            mag = 150
            chri = 25
            intel = 125
            frt = 25
            luc = 25
            race = "Elf"
        case 8:
            HP = 125
            AP = 100
            MP = 25
            SP = 50
            strn = 150
            defn = 150
            spd = 25
            agi = 25
            pro = 25
            mag = 25
            chri = 25
            intel = 50
            frt = 125
            luc = 100
            race = "Giant"
        case 9:
            HP = 75
            AP = 25
            MP = 100
            SP = 100
            strn = 50
            defn = 25
            spd = 25
            agi = 150
            pro = 25
            mag = 150
            chri = 100
            intel = 25
            frt = 25
            luc = 125
            race = "Fairy"
        case _:
            print("Invalid option")
    storywrite(f"Guard: Huh ok. We don't see {race}s venture through this way often.")
    
    # Choose aspiration
    storywrite(f"Guard: Alright. Lastly, why are you even here {name}?")
    print("""Aspirations:
    1.  Adventurer -> Ultimate task masters 
    2.  Hunter -> Specialized monster hunters
    3.  Mercenary -> Highly trained soldiers for hire
    4.  Knight -> Honorable defnenders of the crown
    5.  magician -> Curious practicioners of magic
    6.  Duelist -> Skilled athletes of the blade
    7.  Craftsman -> Handy artists that love their craft
    8.  Scholar -> Enlightened intelellectuals
    9.  Engineer-> Ingenious creators
    10. Merchant -> Money hungry entrepenuers
    11. Sailor -> Men of the sea...live by it, die by it
    12. Aristocrat -> Influentual figures of the high courts
    13. Priest -> Devout believers of the faith 
    14. Outdoorsman -> Rugged survivalists, living off their own means
    15. Bandit -> Cunning kleptomaniacs earning thier keep "off the books"
        > """)
    option = int(input(" > "))
    
    match option:
        case 1:
            AP += 10
            strn += 10
            aspiration = [callings.adventurer]
        case 2:
            HP += 10
            spd += 10
            aspiration = [callings.hunter]
        case 3:
            AP += 10
            strn += 10
            aspiration = [callings.mercenary]
        case 4:
            AP += 10
            defn += 10
            aspiration = [callings.knight]
        case 5:
            MP += 10
            mag += 10
            aspiration = [callings.magician]
        case 6:
            SP += 10
            pro += 10
            aspiration = [callings.duelist]
        case 7:
            SP += 10
            pro += 10
            aspiration = [callings.craftsman]
        case 8:
            MP += 10
            intel += 10
            aspiration = [callings.scholar]
        case 9:
            SP += 10
            intel += 10
            aspiration = [callings.engineer]
        case 10:
            SP += 10
            luc += 10
            aspiration = [callings.merchant]
        case 11:
            HP += 10
            frt += 10
            aspiration = [callings.sailor]
        case 12:
            HP += 10
            chri += 10
            aspiration = [callings.aristicrat]
        case 13:
            MP += 10
            chri += 10
            aspiration = [callings.priest]
        case 14:
            HP += 10
            frt += 10
            aspiration = [callings.outdoorsman]
        case 15:
            SP += 10
            agi += 10
            aspiration = [callings.bandit]
        case _:
            print("Invalid option")
    
    title = [callings.voyager]
    job = [callings.unemployed]

    # Loadout
    primary = None 
    secondary = None
    head = None
    ears = None
    eyes = None
    neck = None
    shoulders = None 
    back = None
    chest = None
    arms = None
    wrist = None
    hands = None
    fingers = None
    waist = None
    legs = None
    feet = None
    inventory = None
    pot = 1
    elix = 0
    x = 0
    y = 0
    standing = True
    key = False

    return Player(name, gender, race, title, job, HP, HP, AP, AP, MP, MP, SP, SP, 1, 0, 100, 0, strn, defn, spd, agi, pro, mag, chri, intel, frt, luc, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, pot, elix, 0, x, y, standing, key)

class Player:
    def __init__(self, name, gender, race, title, job, 
                 HP, HPMAX, AP, APMAX, MP, MPMAX, SP, SPMAX, LVL, EXP, EXPMAX, REP, 
                 STR, DEF, SPD, AGI, PRO, MAG, CHR, INT, FRT, LUC, 
                 primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, 
                 inventory, pot, elix, lums, x, y, standing, key):
        self.name = name
        self.gender = gender
        self.race = race
        self.title = title
        self.job = job
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
        self.pot = pot
        self.elix = elix
        self.lums = lums
        self.x = x
        self.y = y
        self.standing = standing
        self.key = key

    def movement(self):
        if self.y > 0:
            print("1 - NORTH")
        if self.x > 0:
            print("2 - WEST")
        if self.x < x_len:
            print("3 - EAST")
        if self.y < y_len:
            print("4 - SOUTH")

    def heal(self, amount):
        if self.HP + amount < self.HPMAX:
            self.HP += amount
        else:
            self.HP = self.HPMAX
        print(f"{self.name}'s HP healed to {self.HP}")

    def rejuvenate(self, amount):
        if self.AP + amount < self.APMAX:
            self.AP += amount
        else:
            self.AP = self.APMAX
        print(f"{self.name}'s AP rejuvenated to {self.AP}")

    def restore(self, amount):
        if self.MP + amount < self.MPMAX:
            self.MP += amount
        else:
            self.MP = self.MPMAX
        print(f"{self.name}'s MP restored to {self.MP}")

    def recover(self, amount):
        if self.SP + amount < self.SPMAX:
            self.SP += amount
        else:
            self.SP = self.SPMAX
        print(f"{self.name}'s SP recovered to {self.SP}")

    def levelUp(self, amount):
        # Total exp needed to reach lvl. 999: 10,000,009,511

        self.EXP += amount
        i = 0

        if self.EXP >= self.EXPMAX:
            while self.EXP >= self.EXPMAX:
                i += 1
                self.EXP -= self.EXPMAX
                self.EXPMAX += round(self.EXPMAX ** 0.667716164)
                self.LVL += 1
            if i == 1:
                print(f"You have leveled up {i} time and are now level {self.LVL}")
            else:
                print(f"You have leveled up {i} times and are now level {self.LVL}")

    def healthBars(self, a, b, c, d, e):

        # bar update
        remaining_health_bars = round(self.HP / self.HPMAX * bars)
        lost_health_bars = bars - remaining_health_bars
        remaining_aura_bars = round(self.AP / self.APMAX * bars)
        lost_aura_bars = bars - remaining_aura_bars
        remaining_mana_bars = round(self.MP / self.MPMAX * bars)
        lost_mana_bars = bars - remaining_mana_bars
        remaining_stamina_bars = round(self.SP / self.SPMAX * bars)
        lost_stamina_bars = bars - remaining_stamina_bars
        remaining_experience_bars = round(self.EXP / self.EXPMAX * bars)
        lost_experience_bars = bars - remaining_experience_bars
        #total_reputation_bars = round(self.REP / self.REPMAX * bars)
        #gained_reputation_bars = bars + total_experience_bars

        color_default = "\033[0m"

        # health color update
        if self.HP > 0.66 * self.HPMAX:
            health_color = colors.red
        elif self.HP > 0.33 * self.HPMAX:
            health_color = colors.crimson
        else:
            health_color = colors.darkred

        if self.AP > 0.66 * self.APMAX:
            aura_color = colors.yellow
        elif self.AP > 0.33 * self.APMAX:
            aura_color = colors.goldenrod
        else:
            aura_color = colors.darkgoldenrod

        if self.MP > 0.66 * self.MPMAX:
            mana_color = colors.skyblue
        elif self.MP > 0.33 * self.MPMAX:
            mana_color = colors.blue
        else:
            mana_color = colors.darkblue

        if self.SP > 0.66 * self.SPMAX:
            stamina_color = colors.limegreen
        elif self.SP > 0.33 * self.SPMAX:
            stamina_color = colors.green
        else:
            stamina_color = colors.darkgreen

        if self.EXP < 0.33 * self.EXPMAX:
            experience_color = colors.plum
        elif self.EXP < 0.66 * self.EXPMAX:
            experience_color = colors.purple
        else:
            experience_color = colors.indigo

        '''
        if self.REP > 0.66 * self.REP:
            stamina_color = colors.limegreen
        elif self.REP > 0.33 * self.REP:
            stamina_color = colors.green
        else:
            stamina_color = colors.darkgreen

        if self.REP < 0.33 * self.REP:
            stamina_color = colors.plum
        elif self.REP < 0.66 * self.REP:
            stamina_color = colors.purple
        else:
            stamina_color = colors.indigo
        '''

        # printing stats
        if a == 1:
            print(f"HP: {self.HP} / {self.HPMAX}")
            print(f"|{health_color}{remaining_health_bars * remaining_stat_symbol}"
                    f"{lost_health_bars * lost_stat_symbol}{color_default}|")

        if b == 1:
            print(f"AP: {self.AP} / {self.APMAX}")
            print(f"|{aura_color}{remaining_aura_bars * remaining_stat_symbol}"
                    f"{lost_aura_bars * lost_stat_symbol}{color_default}|")

        if c == 1:
            print(f"MP: {self.MP} / {self.MPMAX}")
            print(f"|{mana_color}{remaining_mana_bars * remaining_stat_symbol}"
                    f"{lost_mana_bars * lost_stat_symbol}{color_default}|")

        if d == 1:
            print(f"SP: {self.SP} / {self.SPMAX}")
            print(f"|{stamina_color}{remaining_stamina_bars * remaining_stat_symbol}"
                    f"{lost_stamina_bars * lost_stat_symbol}{color_default}|")
        
        if e == 1:
            print(f"EXP: {self.EXP} / {self.EXPMAX}")
            print(f"|{experience_color}{remaining_experience_bars * remaining_stat_symbol}"
                    f"{lost_experience_bars * lost_stat_symbol}{color_default}|")
            
        '''
        if f == 1:
            print(f"REP: {self.REP}")
            print(f"|{stamina_color}{remaining_stamina_bars * remaining_stat_symbol}"
                    f"{lost_stamina_bars * lost_stat_symbol}{color_default}|")
        '''

    def characterStatus(self, type):
        
        if type == "main":
            print(f"NAME: {player.name}")
            self.healthBars(1, 1, 1, 1, 1)
            print(f"STR: {player.STR}")
            print(f"POTIONS: {player.pot}")
            print(f"ELIXIRS: {player.elix}")
            print(f"LUMS: {player.lums}")
            print(f"COORD: {player.x}, {player.y}")

        elif type == "battle":
            print(f"NAME: {player.name}")
            self.healthBars(1, 1, 1, 1, 1)
            print(f"STR: {player.STR}")
            print(f"POTIONS: {player.pot}")
            print(f"ELIXIRS: {player.elix}")

        elif type == "shop":
            self.healthBars(1, 1, 1, 1, 1)
            print(f"STR: {player.STR}")
            print(f"POTIONS: {player.pot}")
            print(f"ELIXIRS: {player.elix}")
            print(f"LUMS: {player.lums}")

    def statusWindow(self):
        pass

    def inventory(self):
        pass

# ====================================================================== FUNCTIONS ===========================================================================

def battle():
    global player, fight, play, run, boss

    if not boss:
        enemy = random.choice(e_list)
    else:
        enemy = "Dragon"
    hp = mobs[enemy]["hp"]
    hpmax = hp
    STR = mobs[enemy]["at"]
    g = mobs[enemy]["go"]

    while fight:
        clear()
        bordl()
        print(F"Defeat the {enemy}!")
        sectl()
        print(f"{enemy}'s HP: {hp} / {hpmax}")
        print(f"{player.name}'s HP: {player.HP} / {player.HPMAX}")
        player.characterStatus("battle")
        sectl()
        print("1 - ATTACK")
        if player.pot > 0:
            print("2 - USE POTION (30HP)")
        if player.elix > 0:
            print("3 - USE ELIXIR (50HP)")
        bordl()

        choice = input("# ")

        if choice == "1":
            hp -= player.STR
            print(f"{player.name} dealt {player.STR} damage to the {enemy}")
            if hp > 0:
                player.HP -= STR
                print(f"{enemy} dealt {STR} damage to {player.name}")
            input("> ")

        elif choice == "2":
            if player.pot > 0:
                player.pot -= 1
                player.heal(30)
                player.HP -= STR
                print(f"{enemy} dealt {STR} damage to {player.name}")
            else:
                print("No potions!")
            input("> ")

        elif choice == "3":
            if player.elix > 0:
                player.elix -= 1
                player.heal(50)
                player.HP -= STR
                print(f"{enemy} dealt {STR} damage to {player.name}")
            else:
                print("No elixirs!")
            input("> ")

        if player.HP <= 0:
            print(f"{enemy} defeated {player.name}...")
            sectl()
            fight = False
            play = False
            run = False
            print("GAME OVER")
            input("> ")

        if hp <= 0:
            print(f"{player.name} defeated the {enemy}!")
            sectl()
            fight = False
            player.lums += g
            print(f"You've found {g} lums!")
            if random.randint(0, 100) < 30:
                player.pot += 1
                print("You've found a potion!")
            if enemy == "Dragon":
                sectl()
                print("Congratulations, you've finished the game!")
                boss = False
                play = False
                run = False
            input("> ")
            clear()

def shop():
    global player, buy

    while buy:
        clear()
        bordl()
        print("Welcome to the shop!")
        sectl()
        player.characterStatus("shop")
        print(f"STR: {player.STR}")
        sectl()
        print("1 - BUY POTION (30HP) - 5 lums")
        print("2 - BUY ELIXIR (MAXHP) - 8 lums")
        print("3 - UPGRADE WEAPON (+2STR) - 10 lums")
        print("4 - UPGRADE REP (+20STR) - 1 lums")
        print("5 - LEAVE")
        bordl()

        choice = input("# ")

        if choice == "1":
            if player.lums >= 5:
                player.pot += 1
                player.lums -= 5
                print("You've bought a potion!")
            else:
                print("Not enough lums!")
            input("> ")
        elif choice == "2":
            if player.lums >= 8:
                player.elix += 1
                player.lums -= 8
                print("You've bought an elixir!")
            else:
                print("Not enough lums!")
            input("> ")
        elif choice == "3":
            if player.lums >= 10:
                player.STR += 2
                player.lums -= 10
                print("You've upgraded your weapon!")
            else:
                print("Not enough lums!")
            input("> ")
        elif choice == "4":
            if player.lums >= 1:
                player.EXP += 20
                player.lums -= 1
                print("You've increased your EXP!")
            else:
                print("Not enough lums!")
            input("> ")
        elif choice == "5":
            buy = False

def mayor():
    global player, speak, key

    while speak:
        clear()
        bordl()
        print(f"Hello there, {player.name}!")
        if player.STR < 10:
            print("You're not strong enough to face the dragon yet! Keep practicing and come back later!")
            player.key = False
        else:
            print("You might want to take on the dragon now! Take this key but be careful with the beast!")
            player.key = True

        sectl()
        print("1 - LEAVE")
        bordl()

        choice = input("# ")

        if choice == "1":
            speak = False

def cave():
    global player, boss, fight

    while boss:
        clear()
        bordl()
        print("Here lies the cave of the dragon. What will you do?")
        sectl()
        if player.key:
            print("1 - USE KEY")
        print("2 - TURN BACK")
        bordl()

        choice = input("# ")

        if choice == "1":
            if player.key:
                fight = True
                battle()
        elif choice == "2":
            boss = False

def talk():
    pass

def craft():
    pass

def enhance():
    pass

def enchant():
    pass

def alchemy():
    pass

# ======================================================================== LOGIC =============================================================================

def savePath(n):
    global playerSave_path

    if n == 1:
        playerSave_path = "Saves\Save1\player.pkl"
        return "Saves\Save1\player.pkl"
    elif n == 2:
        playerSave_path = "Saves\Save2\player.pkl"
        return "Saves\Save2\player.pkl"
    elif n == 3:
        playerSave_path = "Saves\Save3\player.pkl"
        return "Saves\Save3\player.pkl"

def saveLastModified(path): 
    try: 
        return time.ctime(os.path.getmtime(path))
    except OSError:
        return "No save found!"

# Save game file
def save():
    global player, o

    clear()
    print("Which file do you want to save to?")
    print(f"1. Save file 1 -> Last saved on {saveLastModified(savePath(1))}")
    print(f"2. Save file 2 -> Last saved on {saveLastModified(savePath(2))}")
    print(f"3. Save file 3 -> Last saved on {saveLastModified(savePath(3))}")
    
    o = opt()

    clear()
    
    if o == 1:
        save_path = savePath(1)
    elif o == 2:
        save_path = savePath(2)
    elif o == 3:
        save_path = savePath(3)

    # Player data 
    with open(save_path, 'wb') as file:
        pickle.dump(player, file)

    print(f"Player data saved to file {o} sucessfully!")
    cont()

# Autosave game file
def autosave():
    global player
    
    clear()
    # Player data 
    with open(playerSave_path, 'wb') as file:
        pickle.dump(player, file)

# Quicksave game file
def quicksave():
    global player
    
    # Player data save
    clear()
    # Player data 
    with open(playerSave_path, 'wb') as file:
        pickle.dump(player, file)

    print(f"Player data saved to file {o} sucessfully!")
    cont()

# Load game file
def load():
    global player, menu, play

    clear()
    print("Which file do you want to load?")
    print(f"1. Save file 1 -> Last saved on {saveLastModified(savePath(1))}")
    print(f"2. Save file 2 -> Last saved on {saveLastModified(savePath(2))}")
    print(f"3. Save file 3 -> Last saved on {saveLastModified(savePath(3))}")
    
    o = opt()

    if o == 1:
        save_path = savePath(1)
    elif o == 2:
        save_path = savePath(2)
    elif o == 3:
        save_path = savePath(3)

    try:

        # Player data
        with open(save_path, 'rb') as file:
            player = pickle.load(file)

        clear()
        print(f"Welcome back, {player.name}!")
        cont()
        menu = False
        play = True

    except OSError:
        clear()
        print("No loadable save file!")
        cont()
    
def rules():
    clear()
    print("I'm the creator of this game and these are the rules.")
    cont()

def options():
    clear()
    print("options")
    cont()

# Exit game to main menu
def exit():
    pass

# Pause game text
def cont(): input("> ")

# In-game choice
def opt():
    print(" ")
    o = int(input(" > "))
    return o

# ==================================================================== MAIN GAME LOOP ========================================================================

def lumland():
    global player, run, menu, play, pause, options, buy, speak, boss, fight

    while run:
        while menu:
            clear()
            bordl()
            typewrite("WELCOME TO LUMLAND")
            space()
            space()
            print("1. NEW GAME")
            print("2. LOAD GAME")
            print("3. RULES")
            print("4. QUIT GAME")
            bordl()

            o = opt()

            if o == 1:
                player = characterCreation()
                save()
                menu = False
                play = True
            elif o == 2:
                load()
            elif o == 3:
                rules()
            elif o == 4:
                quit()

        while play:
            autosave() # autosave
            clear()

            if not player.standing:
                if biom[map[player.y][player.x]]["e"]:
                    if random.randint(0, 100) < 30:
                        fight = True
                        battle()

            if play:
                bordl()
                print(f"LOCATION: {biom[map[player.y][player.x]]["t"]}")
                undrl()
                player.characterStatus("main")
                sectl()
                print("0 - SAVE AND QUIT")
                player.movement()
                if player.pot > 0:
                    print("5 - USE POTION (30HP)")
                if player.elix > 0:
                    print("6 - USE ELIXIR (50HP)")
                if map[player.y][player.x] == "shop" or map[player.y][player.x] == "mayor" or map[player.y][player.x] == "cave":
                    print("7 - ENTER")
                bordl()

                dest = input("> ")

                if dest == "0":
                    play = False
                    menu = True
                    autosave()
                elif dest == "1":
                    if player.y > 0:
                        player.y -= 1
                        player.standing = False
                elif dest == "2":
                    if player.x > 0:
                        player.x -= 1
                        player.standing = False
                elif dest == "3":
                    if player.x < x_len:
                        player.x += 1
                        player.standing = False
                elif dest == "4":
                    if player.y < y_len:
                        player.y += 1
                        player.standing = False
                elif dest == "5":
                    if player.pot > 0:
                        player.pot -= 1
                        player.heal(30)
                    else:
                        print("No potions!")
                    input("> ")
                    player.standing = True
                elif dest == "6":
                    if player.elix > 0:
                        player.elix -= 1
                        player.heal(50)
                    else:
                        print("No elixirs!")
                    input("> ")
                    player.standing = True
                elif dest == "7":
                    if map[player.y][player.x] == "shop":
                        buy = True
                        shop()
                    if map[player.y][player.x] == "mayor":
                        speak = True
                        mayor()
                    if map[player.y][player.x] == "cave":
                        boss = True
                        cave()
                else:
                    player.standing = True

# Game Function
lumland()