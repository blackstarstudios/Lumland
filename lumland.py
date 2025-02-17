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
key = False
fight = False
buy = False
standing = True
speak = False
boss = False
talk = False
inventory = False
status = False
craft = False
brew = False
enhance = False
enchant = False

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

HP = 50
HPMAX = 50
ATK = 3
pot = 1
elix = 0
gold = 0
x = 0
y = 0

class Player:
    def __init__(self, name, race, title, job, HP, AP, MP, SP, lums):
        self.name = name
        self.race = race
        self.title = title
        self.job = job
        self.HP = HP
        self.AP = AP
        self.MP = MP
        self.SP = SP
        self.lums = lums

def heal(amount):
    global HP
    if HP + amount < HPMAX:
        HP += amount
    else:
        HP = HPMAX
    print(name + "'s HP refilled to " + str(HP) + "!")

# ====================================================================== FUNCTIONS ===========================================================================

def battle():
    global name, fight, play, run, HP, pot, elix, gold, boss

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
        print(name + "'s HP: " + str(HP) + "/" + str(HPMAX))
        print("POTIONS: " + str(pot))
        print("ELIXIR: " + str(elix))
        sectl()
        print("1 - ATTACK")
        if pot > 0:
            print("2 - USE POTION (30HP)")
        if elix > 0:
            print("3 - USE ELIXIR (50HP)")
        bordl()

        choice = input("# ")

        if choice == "1":
            hp -= ATK
            print(name + " dealt " + str(ATK) + " damage to the " + enemy + ".")
            if hp > 0:
                HP -= atk
                print(enemy + " dealt " + str(atk) + " damage to " + name + ".")
            input("> ")

        elif choice == "2":
            if pot > 0:
                pot -= 1
                heal(30)
                HP -= atk
                print(enemy + " dealt " + str(atk) + " damage to " + name + ".")
            else:
                print("No potions!")
            input("> ")

        elif choice == "3":
            if elix > 0:
                elix -= 1
                heal(50)
                HP -= atk
                print(enemy + " dealt " + str(atk) + " damage to " + name + ".")
            else:
                print("No elixirs!")
            input("> ")

        if HP <= 0:
            print(enemy + " defeated " + name + "...")
            sectl()
            fight = False
            play = False
            run = False
            print("GAME OVER")
            input("> ")

        if hp <= 0:
            print(name + " defeated the " + enemy + "!")
            sectl()
            fight = False
            gold += g
            print("You've found " + str(g) + " gold!")
            if random.randint(0, 100) < 30:
                pot += 1
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
    global buy, gold, pot, elix, ATK

    while buy:
        clear()
        bordl()
        print("Welcome to the shop!")
        sectl()
        print("GOLD: " + str(gold))
        print("POTIONS: " + str(pot))
        print("ELIXIRS: " + str(elix))
        print("ATK: " + str(ATK))
        sectl()
        print("1 - BUY POTION (30HP) - 5 GOLD")
        print("2 - BUY ELIXIR (MAXHP) - 8 GOLD")
        print("3 - UPGRADE WEAPON (+2ATK) - 10 GOLD")
        print("4 - LEAVE")
        bordl()

        choice = input("# ")

        if choice == "1":
            if gold >= 5:
                pot += 1
                gold -= 5
                print("You've bought a potion!")
            else:
                print("Not enough gold!")
            input("> ")
        elif choice == "2":
            if gold >= 8:
                elix += 1
                gold -= 8
                print("You've bought an elixir!")
            else:
                print("Not enough gold!")
            input("> ")
        elif choice == "3":
            if gold >= 10:
                ATK += 2
                gold -= 10
                print("You've upgraded your weapon!")
            else:
                print("Not enough gold!")
            input("> ")
        elif choice == "4":
            buy = False

def mayor():
    global speak, key

    while speak:
        clear()
        bordl()
        print("Hello there, " + name + "!")
        if ATK < 10:
            print("You're not strong enough to face the dragon yet! Keep practicing and come back later!")
            key = False
        else:
            print("You might want to take on the dragon now! Take this key but be careful with the beast!")
            key = True

        sectl()
        print("1 - LEAVE")
        bordl()

        choice = input("# ")

        if choice == "1":
            speak = False

def cave():
    global boss, key, fight

    while boss:
        clear()
        bordl()
        print("Here lies the cave of the dragon. What will you do?")
        sectl()
        if key:
            print("1 - USE KEY")
        print("2 - TURN BACK")
        bordl()

        choice = input("# ")

        if choice == "1":
            if key:
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

def rules():
    print("rules")

def options():
    print("options")

# Exit game to main menu
def exit():
    pass

# Save game file
def save():
    list = [
        name,
        str(HP),
        str(ATK),
        str(pot),
        str(elix),
        str(gold),
        str(x),
        str(y),
        str(key)
    ]

    file = open("load.txt", "w")

    for item in list:
        file.write(item + "\n")
    file.close()

# Load game file
def load():
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
    while run:
        while menu:
            print("1, NEW GAME")
            print("2, LOAD GAME")
            print("3, RULES")
            print("4, QUIT GAME")

            if rules:
                print("I'm the creator of this game and these are the rules.")
                rules = False
                choice = ""
                input("> ")
            else:
                choice = input("# ")

            if choice == "1":
                clear()
                name = input("# What's your name, hero? ")
                menu = False
                play = True
            elif choice == "2":
                try:
                    f = open("load.txt", "r")
                    load_list = f.readlines()
                    if len(load_list) == 9:
                        name = load_list[0][:-1]
                        HP = int(load_list[1][:-1])
                        ATK = int(load_list[2][:-1])
                        pot = int(load_list[3][:-1])
                        elix = int(load_list[4][:-1])
                        gold = int(load_list[5][:-1])
                        x = int(load_list[6][:-1])
                        y = int(load_list[7][:-1])
                        key = bool(load_list[8][:-1])
                        clear()
                        print("Welcome back, " + name + "!")
                        input("> ")
                        menu = False
                        play = True
                    else:
                        print("Corrupt save file!")
                        input("> ")
                except OSError:
                    print("No loadable save file!")
                    input("> ")
            elif choice == "3":
                rules = True
            elif choice == "4":
                quit()

        while play:
            save()  # autosave
            clear()

            if not standing:
                if biom[map[y][x]]["e"]:
                    if random.randint(0, 100) < 30:
                        fight = True
                        battle()

            if play:
                bordl()
                print("LOCATION: " + biom[map[y][x]]["t"])
                undrl()
                print("NAME: " + name)
                print("HP: " + str(HP) + "/" + str(HPMAX))
                print("ATK: " + str(ATK))
                print("POTIONS: " + str(pot))
                print("ELIXIRS: " + str(elix))
                print("GOLD: " + str(gold))
                print("COORD:", x, y)
                sectl()
                print("0 - SAVE AND QUIT")
                if y > 0:
                    print("1 - NORTH")
                if x < x_len:
                    print("2 - EAST")
                if y < y_len:
                    print("3 - SOUTH")
                if x > 0:
                    print("4 - WEST")
                if pot > 0:
                    print("5 - USE POTION (30HP)")
                if elix > 0:
                    print("6 - USE ELIXIR (50HP)")
                if map[y][x] == "shop" or map[y][x] == "mayor" or map[y][x] == "cave":
                    print("7 - ENTER")
                bordl()

                dest = input("# ")

                if dest == "0":
                    play = False
                    menu = True
                    save()
                elif dest == "1":
                    if y > 0:
                        y -= 1
                        standing = False
                elif dest == "2":
                    if x < x_len:
                        x += 1
                        standing = False
                elif dest == "3":
                    if y < y_len:
                        y += 1
                        standing = False
                elif dest == "4":
                    if x > 0:
                        x -= 1
                        standing = False
                elif dest == "5":
                    if pot > 0:
                        pot -= 1
                        heal(30)
                    else:
                        print("No potions!")
                    input("> ")
                    standing = True
                elif dest == "6":
                    if elix > 0:
                        elix -= 1
                        heal(50)
                    else:
                        print("No elixirs!")
                    input("> ")
                    standing = True
                elif dest == "7":
                    if map[y][x] == "shop":
                        buy = True
                        shop()
                    if map[y][x] == "mayor":
                        speak = True
                        mayor()
                    if map[y][x] == "cave":
                        boss = True
                        cave()
                else:
                    standing = True

# Game Function
lumland()