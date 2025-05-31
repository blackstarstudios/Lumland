# UI Menus
import ui.design.style as style
import text.event_text as eventxt
import utils.text_util as tutil

def main_menu():
    tutil.clear()
    style.bordl()
    eventxt.typewrite("WELCOME TO LUMLAND")
    style.space()
    style.space()
    print("1. NEW GAME")
    print("2. LOAD GAME")
    print("3. RULES")
    print("4. QUIT GAME")
    style.bordl()

def hud():
    pass

def options_menu():
    pass
    # resume
    # settings
    # save and exit
    # exit game

def settings_menu():
    pass

def credits_menu():
    pass