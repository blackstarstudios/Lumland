#                                                                          LUMLAND                                                                            
# _____________________________________________________________________ BY BLACKSTAR. ________________________________________________________________________

# ====================================================================== LIBRARIES ===========================================================================

# Official Libraries
import os, random

# Custom Libraries


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

'''
# Healthbar stats
max_health = 100
current_health = 100
max_mana = 50
current_mana = 50

# Healthbar display
bars = 20
remaining_health_symbol = "█"
lost_health_symbol = "_"

# Colors
color_green = "\033[92m"
color_yellow = "\33[33m"
color_red = "\033[91m"
color_blue = "\33[34m"
color_default = "\033[0m"
health_color = color_green

# bar update
remaining_health_bars = round(current_health / max_health * bars)
lost_health_bars = bars - remaining_health_bars
remaining_mana_bars = round(current_mana / max_mana * bars)
lost_mana_bars = bars - remaining_mana_bars

# printing stats
print(f"HEALTH: {current_health} / {max_health}")
print(f"|{health_color}{remaining_health_bars * remaining_health_symbol}"
        f"{lost_health_bars * lost_health_symbol}{color_default}|")
print(f"MANA: {current_mana} / {max_mana}")
print(f"|{color_blue}{remaining_mana_bars * remaining_health_symbol}"
        f"{lost_mana_bars * lost_health_symbol}{color_default}|")

# stat update
current_health -= 1
current_mana -= 1

current_health = max(current_health, 0)
current_mana = max(current_mana, 0)

# health color update
if current_health > 0.66 * max_health:
    health_color = color_green
elif current_health > 0.33 * max_health:
    health_color = color_yellow
else:
    health_color = color_red
'''

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

def characterCreation():
    clear()
    name = input("What's your name, hero? > ")
    #race = input("What is your race? > ")
    race = "Human"
    title = "Voyager"
    job = "Adventurer"
    HP = 100
    HPMAX = HP
    AP = 50
    APMAX = AP
    MP = 50
    MPMAX = MP
    SP = 100
    SPMAX = SP
    ATK = 3
    pot = 1
    elix = 0
    lums = 0
    x = 0
    y = 0
    standing = True
    key = False
    return Player(name, race, title, job, HP, HPMAX, AP, APMAX, MP, MPMAX, SP, SPMAX, ATK, pot, elix, lums, x, y, standing, key)

class Player:
    def __init__(self, name, race, title, job, HP, HPMAX, AP, APMAX, MP, MPMAX, SP, SPMAX, ATK, pot, elix, lums, x, y, standing, key):
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
        self.ATK = ATK
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
        if self.x < x_len:
            print("2 - EAST")
        if self.y < y_len:
            print("3 - SOUTH")
        if self.x > 0:
            print("4 - WEST")

    def heal(self, amount):
        if self.HP + amount < self.HPMAX:
            self.HP += amount
        else:
            self.HP = self.HPMAX
        print(self.name + "'s HP refilled to " + str(self.HP) + "!")

    def rejuvinate(self, amount):
        if self.AP + amount < self.APMAX:
            self.AP += amount
        else:
            self.AP = self.APMAX
        print(self.name + "'s AP refilled to " + str(self.AP) + "!")

    def restore(self, amount):
        if self.MP + amount < self.MPMAX:
            self.MP += amount
        else:
            self.MP = self.MPMAX
        print(self.name + "'s MP restored to " + str(self.MP) + "!")

    def recover(self, amount):
        if self.SP + amount < self.SPMAX:
            self.SP += amount
        else:
            self.SP = self.SPMAX
        print(self.name + "'s SP recovered to " + str(self.SP) + "!")
    
    def characterStatus(self, type):
        
        if type == "main":
            print("NAME: " + player.name)
            print("HP: " + str(player.HP) + "/" + str(player.HPMAX))
            print("AP: " + str(player.AP) + "/" + str(player.APMAX))
            print("MP: " + str(player.MP) + "/" + str(player.MPMAX))
            print("SP: " + str(player.SP) + "/" + str(player.SPMAX))
            print("ATK: " + str(player.ATK))
            print("POTIONS: " + str(player.pot))
            print("ELIXIRS: " + str(player.elix))
            print("LUMS: " + str(player.lums))
            print("COORD:", player.x, player.y)

        elif type == "battle":
            print("NAME: " + player.name)
            print("HP: " + str(player.HP) + "/" + str(player.HPMAX))
            print("AP: " + str(player.AP) + "/" + str(player.APMAX))
            print("MP: " + str(player.MP) + "/" + str(player.MPMAX))
            print("SP: " + str(player.SP) + "/" + str(player.SPMAX))
            print("ATK: " + str(player.ATK))
            print("POTIONS: " + str(player.pot))
            print("ELIXIRS: " + str(player.elix))

        elif type == "shop":
            print("HP: " + str(player.HP) + "/" + str(player.HPMAX))
            print("AP: " + str(player.AP) + "/" + str(player.APMAX))
            print("MP: " + str(player.MP) + "/" + str(player.MPMAX))
            print("SP: " + str(player.SP) + "/" + str(player.SPMAX))
            print("ATK: " + str(player.ATK))
            print("POTIONS: " + str(player.pot))
            print("ELIXIRS: " + str(player.elix))
            print("LUMS: " + str(player.lums))

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
    atk = mobs[enemy]["at"]
    g = mobs[enemy]["go"]

    while fight:
        clear()
        bordl()
        print("Defeat the " + enemy + "!")
        sectl()
        print(enemy + "'s HP: " + str(hp) + "/" + str(hpmax))
        print(player.name + "'s HP: " + str(player.HP) + "/" + str(player.HPMAX))
        player.characterStatus()
        sectl()
        print("1 - ATTACK")
        if player.pot > 0:
            print("2 - USE POTION (30HP)")
        if player.elix > 0:
            print("3 - USE ELIXIR (50HP)")
        bordl()

        choice = input("# ")

        if choice == "1":
            hp -= player.ATK
            print(player.name + " dealt " + str(player.ATK) + " damage to the " + enemy + ".")
            if hp > 0:
                player.HP -= atk
                print(enemy + " dealt " + str(atk) + " damage to " + player.name + ".")
            input("> ")

        elif choice == "2":
            if player.pot > 0:
                player.pot -= 1
                player.heal(30)
                player.HP -= atk
                print(enemy + " dealt " + str(atk) + " damage to " + player.name + ".")
            else:
                print("No potions!")
            input("> ")

        elif choice == "3":
            if player.elix > 0:
                player.elix -= 1
                player.heal(50)
                player.HP -= atk
                print(enemy + " dealt " + str(atk) + " damage to " + player.name + ".")
            else:
                print("No elixirs!")
            input("> ")

        if player.HP <= 0:
            print(enemy + " defeated " + player.name + "...")
            sectl()
            fight = False
            play = False
            run = False
            print("GAME OVER")
            input("> ")

        if hp <= 0:
            print(player.name + " defeated the " + enemy + "!")
            sectl()
            fight = False
            player.lums += g
            print("You've found " + str(g) + " self.lums!")
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
        print("ATK: " + str(player.ATK))
        sectl()
        print("1 - BUY POTION (30HP) - 5 lums")
        print("2 - BUY ELIXIR (MAXHP) - 8 lums")
        print("3 - UPGRADE WEAPON (+2ATK) - 10 lums")
        print("4 - LEAVE")
        bordl()

        choice = input("# ")

        if choice == "1":
            if player.lums >= 5:
                pot += 1
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
                player.ATK += 2
                player.lums -= 10
                print("You've upgraded your weapon!")
            else:
                print("Not enough lums!")
            input("> ")
        elif choice == "4":
            buy = False

def mayor():
    global player, speak, key

    while speak:
        clear()
        bordl()
        print("Hello there, " + player.name + "!")
        if player.ATK < 10:
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

def status():
    pass

def inventory():
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

# Save game file
def save():
    global player
    
    clear()
    list = [
        player.name,
        player.race, 
        player.title, 
        player.job,
        str(player.HP),
        str(player.HPMAX), 
        str(player.AP), 
        str(player.APMAX), 
        str(player.MP), 
        str(player.MPMAX), 
        str(player.SP), 
        str(player.SPMAX),
        str(player.ATK),
        str(player.pot),
        str(player.elix),
        str(player.lums),
        str(player.x),
        str(player.y),
        str(player.standing),
        str(player.key)
    ]

    file = open("load.txt", "w")

    for item in list:
        file.write(item + "\n")
    file.close()

# Load game file
def load():
    global player, menu, play
    
    clear()
    try:
        f = open("load.txt", "r")
        load_list = f.readlines()
        if len(load_list) == 20:
            player.name = load_list[0][:-1]
            player.race = load_list[1][:-1]
            player.title = load_list[2][:-1]
            player.job = load_list[3][:-1]
            player.HP = int(load_list[4][:-1])
            player.HPMAX = int(load_list[5][:-1])
            player.AP = int(load_list[6][:-1])
            player.APMAX = int(load_list[7][:-1])
            player.MP = int(load_list[8][:-1])
            player.MPMAX = int(load_list[9][:-1])
            player.SP = int(load_list[10][:-1])
            player.SPMAX = int(load_list[11][:-1])
            player.ATK = int(load_list[12][:-1])
            player.pot = int(load_list[13][:-1])
            player.elix = int(load_list[14][:-1])
            player.lums = int(load_list[15][:-1])
            player.x = int(load_list[16][:-1])
            player.y = int(load_list[17][:-1])
            player.standing = bool(load_list[18][:-1])
            player.key = bool(load_list[19][:-1])
            clear()
            print("Welcome back, " + player.name + "!")
            input("> ")
            menu = False
            play = True
        else:
            print("Corrupt save file!")
            input("> ")
    except OSError:
        print("No loadable save file!")
        input("> ")

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
def cont():
    input("> ")

# In-game choice
def opt():
    print(" ")
    o = int(input(" > "))
    return o

# ==================================================================== MAIN GAME LOOP ========================================================================

def lumland():
    global player, run, menu, play, pause, options

    while run:
        while menu:
            clear()
            bordl()
            print("LUMLAND")
            space()
            print("1. NEW GAME")
            print("2. LOAD GAME")
            print("3. RULES")
            print("4. QUIT GAME")
            bordl()

            o = opt()

            if o == 1:
                player = characterCreation()
                menu = False
                play = True
            elif o == 2:
                load()
            elif o == 3:
                rules()
            elif o == 4:
                quit()

        while play:
            save()  # autosave
            clear()

            if not player.standing:
                if biom[map[player.y][player.x]]["e"]:
                    if random.randint(0, 100) < 30:
                        fight = True
                        battle()

            if play:
                bordl()
                print("LOCATION: " + biom[map[player.y][player.x]]["t"])
                undrl()
                player.characterStatus()
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
                    save()
                elif dest == "1":
                    if player.y > 0:
                        player.y -= 1
                        player.standing = False
                elif dest == "2":
                    if player.x < x_len:
                        player.x += 1
                        player.standing = False
                elif dest == "3":
                    if player.y < y_len:
                        player.y += 1
                        player.standing = False
                elif dest == "4":
                    if player.x > 0:
                        player.x -= 1
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