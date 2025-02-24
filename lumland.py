#                                                                          LUMLAND                                                                            
# _____________________________________________________________________ BY BLACKSTAR. ________________________________________________________________________

# ====================================================================== LIBRARIES ===========================================================================

# Official Libraries
import os, _pickle as pickle, math, random, time
import Design.colors as colors

# Custom Libraries

# Abilites
import Abilities.Magic as magic
import Abilities.BattleArts as battleArts
import Abilities.Skills as skills

# Items
import Items.Materials as materials
import Items.Consumables as consumables
import Items.Equipment as equipment
import Items.Wearables as wearables
import Items.Weapons as weapons

# NPCs
import NPCs.Monsters as monsters
import NPCs.Characters as characters

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
def clear():
    os.system('cls' if os.name == 'nt' else 'clear') # cls - Windows; clear - Unix

# Write borderline
def bordl():
    print("!=========================!")
    #print(" ")

# Write borderline
#def brdb():
#    print(" ")
#    print("!=====================================!")

# Write underline
def undrl():
    print("________________")

# Write spaceline
def space():
    print(" ")

# Write sectionline
def sectl():
    print("+-----------------+")

# Healthbar display
bars = 20
remaining_stat_symbol = "█"
lost_stat_symbol = "_"

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

#  RACE NAME  |   HP   AP   MP   SP   STR   DEF   SPD   AGI   PRO   MAG   CHR   INT   FRT   LUC
#----------------------------------------------------------------------------------------------
# Giants      |  000  000  000  000   000   000   000   000   000   000   000   000   000   000
# Beastmen    |  000  000  000  000   000   000   000   000   000   000   000   000   000   000
# Orcs        |  000  000  000  000   000   000   000   000   000   000   000   000   000   000
# Ogres       |  000  000  000  000   000   000   000   000   000   000   000   000   000   000
# Humans       |  100  050  050  100   100   100   050   050   100   050   050   100   050   050
# Elves       |  000  000  000  000   000   000   000   000   000   000   000   000   000   000
# Dwarves     |  000  000  000  000   000   000   000   000   000   000   000   000   000   000
# Goblins     |  000  000  000  000   000   000   000   000   000   000   000   000   000   000
# Faries      |  000  000  000  000   000   000   000   000   000   000   000   000   000   000

def characterCreation():
    clear()
    #name = input("What's your name, hero? > ")
    name = "Greg"
    #race = input("What is your race? > ")
    race = "Human"
    title = ["Sword King", "Dragon Slayer"]
    job = ["Adventurer", "Knight"]
    HP = 100
    HPMAX = HP
    AP = 50
    APMAX = AP
    MP = 50
    MPMAX = MP
    SP = 100
    SPMAX = SP
    LVL = 1
    EXP = 0
    EXPMAX = 100
    REP = 0
    STR = 10
    DEF = 10
    SPD = 10
    AGI = 10
    PRO = 10
    MAG = 10
    CHR = 10
    INT = 10
    FRT = 10
    LUC = 10
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
    lums = 100
    x = 0
    y = 0
    standing = True
    key = False
    return Player(name, race, title, job, HP, HPMAX, AP, APMAX, MP, MPMAX, SP, SPMAX, LVL, EXP, EXPMAX, REP, STR, DEF, SPD, AGI, PRO, MAG, CHR, INT, FRT, LUC, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, pot, elix, lums, x, y, standing, key)

class Player:
    def __init__(self, name, race, title, job, 
                 HP, HPMAX, AP, APMAX, MP, MPMAX, SP, SPMAX, LVL, EXP, EXPMAX, REP, 
                 STR, DEF, SPD, AGI, PRO, MAG, CHR, INT, FRT, LUC, 
                 primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, 
                 inventory, pot, elix, lums, x, y, standing, key):
        self.name = name
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
        self.chest = ches
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
            print("  LUMLAND")
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