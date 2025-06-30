#                                                                          LUMLAND                                                                            
# _____________________________________________________________________ BY BLACKSTAR. ________________________________________________________________________

import data.internal.states as state
import user.player as user
# from user.player import Player
import ui.design.style as style, ui.menu as menu
import utils.text_util as tutil, utils.system_util as sutil

# ==================================================================== MAIN GAME LOOP ========================================================================

def lumland():
    while state.run:
        menu.main_menu()
        o = tutil.opt()

        match o:
            case 0:
                sutil.quitGame()
            case 1:
                player: type = user.characterCreation()
                state.play = True
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass

        while state.play:
            tutil.clear()
            style.bordl()
            print(f"LOCATION: ({player.x}, {player.y})")
            style.undrl()
            style.space()
            print(f"NAME: {player.name}, {player.title[0]}")
            print(f"HP: {player.hp} / {player.hpmax}")
            print(f"MP: {player.mp} / {player.mpmax}")
            print(f"AP: {player.ap} / {player.apmax}")
            print(f"SP: {player.sp} / {player.spmax}")
            print(f"PRIMARY: {player.primary[0]}")
            print(f"LUMS: {player.lums}")
            style.sectl()
            style.space()
            print("1. NORTH")
            print("2. WEST")
            print("3. EAST")
            print("4. SOUTH")
            print("5. IVENTORY")
            print("6. OPEN STATUS")
            style.sectl()
            print("0. PAUSE GAME")
            style.bordl()

            o = tutil.opt()

            match o:
                case 0:
                    pass
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    pass
                case 6:
                    pass
                case 7:
                    pass
            
# Game Function
if __name__ == "__main__": 
    lumland()