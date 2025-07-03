# System Utilities
import data.internal.states as state

# Exit to the main menu
def exitGame(): 
    if state.options:
        state.options = False
    state.play = False

# Quit the game
def quitGame(): state.run = False