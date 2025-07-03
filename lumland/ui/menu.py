# Menus
import ui.design.style as style
import utils.text_util as tutil

# Start menu UI
def main_menu():
    tutil.clear()
    style.bordl()
    print("WELCOME TO LUMLAND")
    style.sectl()
    style.space
    print("1. NEW GAME")
    print("2. LOAD GAME")
    print("3. OPTIONS")
    print("4. CREDITS")
    print("0. QUIT GAME")
    style.bordl()

# Pause menu UI
def options_menu(resumeCheck: bool):
    tutil.clear()
    style.bordl()
    print("OPTIONS")
    style.undrl()
    if resumeCheck:
        print("1. RESUME GAME")
        print("2. SAVE GAME")
        print("3. LOAD GAME")
        print("4. SETTINGS")
        print("0. EXIT GAME")
    else:
        print("1. SAVE GAME")
        print("2. LOAD GAME")
        print("3. SETTINGS")
        print("0. BACK TO MENU")
    style.bordl()

# Settings menu UI
def settings_menu(tab: str):
    tutil.clear()
    if tab == "G":
        print("General")
    elif tab == "A":
        print("Audio")
    elif tab == "D":
        print("Display")
    elif tab == "C":
        print("Controls")
    elif tab == "a":
        print("Accessibility")
    else:
        style.bordl()
        print("SETTINGS")
        style.undrl()
        print("1. GENERAL")
        print("2. AUDIO")
        print("3. DISPLAY")
        print("4. CONTROLS")
        print("5. ACCESSIBILITY")
        print("0. BACK TO OPTIONS")
        style.bordl()