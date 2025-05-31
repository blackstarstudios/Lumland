#                                                                          LUMLAND                                                                            
# _____________________________________________________________________ BY BLACKSTAR. ________________________________________________________________________

import data.internal.data as data
import ui.menu as menu

# ==================================================================== MAIN GAME LOOP ========================================================================

def lumland():
    while data.run_state:
        while data.menu_state:
            menu.main_menu()
        while data.play_state:
            data.menu_state = False
            menu.hud()
        while data.option_state:
            data.play_state = False
            menu.options_menu()
        while data.credit_state:
            data.menu_state = False
            menu.credits_menu()

# Game Function
if __name__ == "__main__": 
    lumland()