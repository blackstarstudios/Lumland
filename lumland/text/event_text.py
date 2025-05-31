# Event Text
import sys, time
import utils.text_util as tutil, ui.design.style as style

# Slow text write
def typewrite(text: str):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

# Fast text write
def storywrite(text: str):
    tutil.clear()
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    style.space()
    tutil.cont()