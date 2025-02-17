#                                                                          LUMLAND                                                                            
# _____________________________________________________________________ BY BLACKSTAR. ________________________________________________________________________

# ====================================================================== LIBRARIES ===========================================================================

# Official Libraries
import os

# Custom Libraries


# ======================================================================== STATES ============================================================================

# Major Game States
run = True
menu = True
play = False
pause = False
options = False

# Minor Game States
fight = False
buy = False
talk = False
inventory = False
status = False
craft = False
brew = False
enhance = False
enchant = False

# ======================================================================== DESIGN ============================================================================

# Clear terminal
def clr():
    os.system('cls' if os.name == 'nt' else 'clear') # cls - Windows; clear - Unix

# Write borderline
def brdl():
    print("!=========================!")
    #print(" ")

# Write borderline
#def brdb():
#    print(" ")
#    print("!=====================================!")

# Write underline
def undl():
    print("________________")

# Write spaceline
def spcl():
    print(" ")

# Write sectionline
def secl():
    print("+-----------------+")

# ======================================================================== ITEMS =============================================================================



# ========================================================================= NPCS =============================================================================



# ======================================================================= LOCATIONS ==========================================================================



# ======================================================================== PLAYER ============================================================================

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

# ====================================================================== FUNCTIONS ===========================================================================

def battle():
    pass

def shop():
    pass

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
    pass

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
            clr()
            brdl()
            print("   LUMLAND")
            spcl()
            print("1. NEW GAME")
            print("2. LOAD GAME")
            print("3. OPTIONS")
            print("4. RULES")
            print("5. QUIT")
            brdl()

            o = opt()

            if o == 1:
                pass
            elif o == 2:
                pass
            elif o == 3:
                pass
            elif o == 4:
                rules()
            elif o == 5:
                quit()

# Game Function
lumland()