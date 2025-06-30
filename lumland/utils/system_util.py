# System Utilities
import data.internal.states as state

# Exit to the main menu
def exitGame(): state.play = False

# Quit the game
def quitGame(): state.run = False