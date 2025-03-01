import callings

class NPC:
    def __init__(self, name, gender, race, title, npcClass, job, 
    hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, 
    lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, 
    inventory, magics, arts, skills, x, y):
        self.name = name
        self.gender = gender
        self.race = race
        self.title = title
        self.npcClass = npcClass
        self.job = job
        self.hp = hp
        self.hpmax = hpmax
        self.ap = ap
        self.apmax = apmax
        self.mp = mp
        self.mpmax = mpmax
        self.sp = sp
        self.spmax = spmax
        self.lvl = lvl
        self.exp = exp
        self.expmax = expmax
        self.rep = rep
        self.lums = lums
        self.primary = primary 
        self.secondary = secondary
        self.head = head
        self.ears = ears
        self.eyes = eyes
        self.neck = neck
        self.shoulders = shoulders 
        self.back = back
        self.chest = chest
        self.arms = arms
        self.wrist = wrist
        self.hands = hands
        self.fingers = fingers
        self.waist = waist
        self.legs = legs
        self.feet = feet
        self.inventory = inventory
        self.magics = magics
        self.arts = arts
        self.skills = skills
        self.x = x
        self.y = y

male = 'M'
female = 'F'
other = 'O'
none = 'N'

supreme_star = "Supreme Star"
primeval_star = "Primeval Star"
prime_star = "Prime Star"
high_star = "High Star"
low_star = "Low Star"
half_star = "Half Star"

osiri = NPC("Osiri", male, supreme_star, callings.the_beginning, 'U', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
khuthulun = NPC("Khuthulun", female, supreme_star, callings.the_end, 'U', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
jofiel = NPC("Jofiel", female, prime_star, callings.archangel, 'U', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
hermle = NPC("Hermle", male, prime_star, callings.father_time, 'U', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
lynniel = NPC("Lynniel", female, prime_star, title, 'U', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
marmou = NPC("Marmou", male, prime_star, title, 'U', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
rahdreal = NPC("Rahdreal", male, prime_star, title, 'U', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
grimini = NPC("Grimini", female, prime_star, title, 'U', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
aprial = NPC("Aprial", male, primeval_star, [ callings.the_god_of_all, callings.allstar], 'U', [callings.supreme_ones_seal, callings.god_of_all], hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
antiking = NPC("Antiking", male, primeval_star, [ callings.the_god_of_none, callings.antistar], 'U', [callings.mark_of_the_end, callings.god_of_none], hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
montero = NPC("", 'gen', high_star, title, 'U', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
uran = NPC("", 'gen', high_star, title, 'U', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
sage = NPC("", 'gen', high_star, title, 'U', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
wolford = NPC("", 'gen', high_star, title, 'U', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
asanna = NPC("", female, high_star, title, 'U', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
crozzen = NPC("", 'gen', high_star, title, 'U', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
yukire = NPC("", 'gen', high_star, title, 'U', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
agil = NPC("", 'gen', high_star, title, 'U', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
veneti = NPC("", 'gen', high_star, title, 'U', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
rachess = NPC("", female, high_star, title, 'U', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
bingeal = NPC("", female, high_star, title, 'U', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
krenari = NPC("", 'gen', high_star, title, 'U', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
gahl = NPC("", 'gen', high_star, title, 'U', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
zakzano = NPC("", 'gen', high_star, title, 'U', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
verbel = NPC("", 'gen', high_star, title, 'U', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
himhia = NPC("", 'gen', high_star, title, 'U', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
perizay = NPC("", 'gen', high_star, title, 'U', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
inachtra = NPC("", 'gen', high_star, title, 'U', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
lahkus = NPC("", 'gen', high_star, title, 'U', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
teher = NPC("", 'gen', high_star, title, 'U', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
eirnin = NPC("", 'gen', high_star, title, 'U', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
neieba = NPC("", 'gen', high_star, title, 'U', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
malvent = NPC("", 'gen', low_star, title, 'U', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
beast_Star = NPC("", 'gen', low_star, title, 'U', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
gelalios = NPC("", 'gen', "race", title, 'U', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
kesisumera = NPC("", 'gen', "race", title, 'U', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
mahmu = NPC("", 'gen', "race", title, 'U', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
blaskam = NPC("", 'gen', "race", title, 'U', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
zhillegoh = NPC("", 'gen', "race", title, 'U', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
hezgaur = NPC("", 'gen', "race", title, 'U', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
aran = NPC("", 'gen', half_star, title, 'U', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
blood_god = NPC("", 'gen', half_star, title, 'U', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
greyrose = NPC("Greyrose", male, race, whiteheart, npcClass, job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
malgrieve = NPC("Malgrieve", male, race, endside, npcClass, job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
yahren = NPC("Yahren", male, race, low_king, npcClass, job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
elias = NPC("Elias", male, race, dueling_king, npcClass, job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
gualtier = NPC("", 'gen', "race", title, 'class', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
ezua = NPC("", 'gen', "race", title, 'class', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
aolis = NPC("", 'gen', "race", title, 'class', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
daggril = NPC("", 'gen', "race", title, 'class', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
wearld = NPC("", 'gen', "race", title, 'class', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
william_knightmond = NPC("", male, "race", title, 'class', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
aeces = NPC("", 'gen', "race", title, 'class', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
nutear = NPC("", male, "race", title, 'class', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
pausiris = NPC("", 'gen', "race", title, 'class', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
kinnard = NPC("", male, "race", title, 'class', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
borkus = NPC("", male, "race", title, 'class', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
rheflyn = NPC("", 'gen', "race", title, 'class', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
obeah = NPC("", 'gen', "race", title, 'class', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
uyemura = NPC("", male, "race", title, 'class', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
yuguro = NPC("", male, "race", title, 'class', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
jihro = NPC("", male, "race", title, 'class', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
moffari = NPC("", male, "race", title, 'class', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
eryam = NPC("", 'gen', "race", title, 'class', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
jurni_nyl_fuprir = NPC("", female, "race", title, 'class', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
igbias = NPC("", male, "race", title, 'class', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
cabal = NPC("", male, "race", title, 'class', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
geshrew = NPC("", 'gen', "race", title, 'class', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
pseosippe = NPC("", 'gen', "race", title, 'class', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
bryra = NPC("", female, "race", title, 'class', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
phanuel = NPC("", male, "race", title, 'class', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
hekekri = NPC("", female, "race", title, 'class', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
orthix = NPC("", male, "race", title, 'class', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
ettore = NPC("", 'gen', "race", title, 'class', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
hias = NPC("", male, "race", title, 'class', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
leieth = NPC("", female, "race", title, 'class', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
cyraenan = NPC("", 'gen', "race", title, 'class', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
tosul = NPC("", 'gen', "race", title, 'class', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
llann = NPC("", 'gen', "race", title, 'class', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
captain_southerland = NPC("", male, "race", title, 'class', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
captain_dierge = NPC("", male, "race", title, 'class', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
bayson_cross = NPC("", male, "race", title, 'class', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
yemel = NPC("", female, "race", title, 'class', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
morri = NPC("", male, "race", title, 'class', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
dreven_grey = NPC("", male, "race", title, 'class', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
little_Star = NPC("", male, "race", title, 'class', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
count_abel_waryn = NPC("", male, "race", title, 'class', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
name_voaustier = NPC("", 'gen', "race", title, 'class', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
barri = NPC("", male, "race", title, 'class', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
miel = NPC("", female, "race", title, 'class', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
daisy_pearl = NPC("", female, "race", title, 'class', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)
rosevana_pearl = NPC("", female, "race", title, 'class', job, hp, hpmax, ap, apmax, mp, mpmax, sp, spmax, lvl, exp, expmax, rep, lums, primary, secondary, head, ears, eyes, neck, shoulders, back, chest, arms, wrist, hands, fingers, waist, legs, feet, inventory, magics, arts, skills, x, y)