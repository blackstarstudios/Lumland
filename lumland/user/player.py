# Players
import utils.text_util as tutil

class Player:

    def __init__(self, name, gender, race, title, rank, job, ambition, 
                 hp, hpmax, mp, mpmax, ap, apmax, sp, spmax, lvl, xp, xpmax, rep, 
                 stg, dfn, spd, agi, pro, mag, chr, itl, frt, luc, lums, x, y, 
                 head, ears, eyes, mouth, neck, shoulders, arms, wrists, hands, fingers, back, chest, waist, legs, feet, 
                 inventory, primary, secondary, atk, prot, power, skill, art, magic, companion, party, 
                 standing):
        self.name: str = name
        self.gender: str = gender
        self.race: str = race
        self.title: list = title
        self.rank: str = rank
        self.job: list = job
        self.ambition: list = ambition
        self.hp: int = hp
        self.hpmax: int = hpmax
        self.mp: int = mp
        self.mpmax: int = mpmax
        self.ap: int = ap
        self.apmax: int = apmax
        self.sp: int = sp
        self.spmax: int = spmax
        self.lvl: int = lvl
        self.xp: int = xp
        self.xpmax: int = xpmax
        self.rep: int = rep
        self.stg: int = stg
        self.dfn: int = dfn
        self.agi: int = agi
        self.spd: int = spd
        self.pro: int = pro
        self.mag: int = mag
        self.chr: int = chr
        self.itl: int = itl
        self.frt: int = frt
        self.luc: int = luc
        self.lums: int = lums
        self.x: int = x
        self.y: int = y
        self.head: list = head
        self.eyes: list = eyes
        self.ears: list = ears
        self.mouth: list = mouth
        self.neck: list = neck
        self.back: list = back
        self.shoulders: list = shoulders
        self.arms: list = arms
        self.wrists: list = wrists
        self.hands: list = hands
        self.fingers: list = fingers
        self.chest: list = chest
        self.waist: list = waist
        self.legs: list = legs
        self.feet: list = feet
        self.inventory: list = inventory #type
        self.primary: list = primary #type
        self.secondary: list = secondary #type
        self.atk: int = atk
        self.prot: int = prot
        self.power: list = power
        self.skill: list = skill
        self.art: list = art
        self.magic: list = magic
        self.companion: list = companion
        self.party: list = party
        self.standing: bool = standing

def characterCreation():
    name = "Joten"
    gender = "Male"
    race = "Marron"
    title = ["Voyager"]
    rank = "C"
    job = ["Knight"]
    ambition = ["Adventerous"]
    hp = 50
    hpmax = hp
    mp = 25
    mpmax = mp
    ap = 25
    apmax = ap
    sp = 50
    spmax = sp
    lvl = 1
    xp = 0
    xpmax = 100
    rep = 0
    stg = 10
    dfn = 10
    agi = 10
    spd = 10
    pro = 10
    mag = 10
    chr = 10
    itl = 10
    frt = 10
    luc = 10
    lums = 0
    x = 0
    y = 0
    head = []
    eyes = []
    ears = []
    mouth = []
    neck = []
    back = []
    shoulders = []
    arms = []
    wrists = []
    hands = []
    fingers = []
    chest = []
    waist = []
    legs = []
    feet = []
    inventory = []
    primary = ["Iron Sword"]
    secondary = []
    atk = 10
    prot = 10
    power = []
    skill = []
    art = []
    magic = []
    companion = []
    party = []
    standing = True

    print("Character Created")
    tutil.cont()

    return Player(name, gender, race, title, rank, job, ambition, 
                       hp, hpmax, mp, mpmax, ap, apmax, sp, spmax, lvl, xp, xpmax, rep, 
                       stg, dfn, spd, agi, pro, mag, chr, itl, frt, luc, lums, x, y, 
                       head, ears, eyes, mouth, neck, shoulders, arms, wrists, hands, fingers, back, chest, waist, legs, feet, 
                       inventory, primary, secondary, atk, prot, power, skill, art, magic, companion, party, standing)

# Player(name, gender, race, title, rank, job, ambition, hp, hpmax, mp, mpmax, ap, apmax, sp, spmax, lvl, xp, xpmax, rep, stg, dfn, spd, agi, pro, mag, chr, itl, frt, luc, lums, x, y, head, ears, eyes, mouth, neck, shoulders, arms, wrists, hands, fingers, back, chest, waist, legs, feet, inventory, primary, secondary, atk, prot, power, skill, art, magic, companion, party, standing)
    