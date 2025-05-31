# Text Utilities
import os

# ==================================================================== General Utilities =====================================================================

# clear terminal
def clear(): os.system('cls' if os.name == 'nt' else 'clear')

# Number comma formatter (100000 -> 100,000)
def numform(num): return f"{num:,}"

# ==================================================================== Custom Utilities =====================================================================

# Pause game text
def cont(): input("> ")

# In-game choice
def opt(): return int(input("\n > "))