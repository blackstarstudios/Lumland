import math

'''
x = 0
i = 1
a = 0

while i < 1000:
    if i == 1:
        x += 100
        print(f"{i}th iteration: {x}")
        a += x
        i += 1
    x += round(x ** 0.667716164)
    a += x
    print(f"{i}th iteration: {x}")
    i += 1

print(f"Total to reach Lvl. 999: {a}")
'''

LVL = 1
EXP = 90
EXPMAX = 100

def lvlUp(amount):
    global EXP, EXPMAX, LVL

    EXP += amount
    i = 0

    if EXP >= EXPMAX:
        while EXP >= EXPMAX:
            i += 1
            EXP -= EXPMAX
            EXPMAX += round(EXPMAX ** 0.667716164)
            LVL += 1
        print(f"You have leveled up {i} times and are now Lvl. {LVL}")

lvlUp(100000)