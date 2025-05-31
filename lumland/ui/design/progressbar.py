# Healthbar
import ui.design.color as color, utils.text_util as tutil, user.player as user

# Healthbar display
bars = 20
remaining_bar_symbol = "█"
lost_bar_symbol = "_"

def healthBars(hp: bool, ap: bool, mp: bool, sp: bool, xp: bool):

    # bar update
    remaining_health_bars = round(user.HP / user.HPMAX * bars)
    lost_health_bars = bars - remaining_health_bars
    remaining_aura_bars = round(user.AP / user.APMAX * bars)
    lost_aura_bars = bars - remaining_aura_bars
    remaining_mana_bars = round(user.MP / user.MPMAX * bars)
    lost_mana_bars = bars - remaining_mana_bars
    remaining_stamina_bars = round(user.SP / user.SPMAX * bars)
    lost_stamina_bars = bars - remaining_stamina_bars
    remaining_experience_bars = round(user.EXP / user.EXPMAX * bars)
    lost_experience_bars = bars - remaining_experience_bars
    #total_reputation_bars = round(REP / REPMAX * bars)
    #gained_reputation_bars = bars + total_experience_bars

    color_default = "\033[0m"

    # health color update
    if user.HP > 0.66 * user.HPMAX:
        health_color = color.red
    elif user.HP > 0.33 * user.HPMAX:
        health_color = color.crimson
    else:
        health_color = color.darkred

    if user.AP > 0.66 * user.APMAX:
        aura_color = color.yellow
    elif user.AP > 0.33 * user.APMAX:
        aura_color = color.goldenrod
    else:
        aura_color = color.darkgoldenrod

    if user.MP > 0.66 * user.MPMAX:
        mana_color = color.skyblue
    elif user.MP > 0.33 * user.MPMAX:
        mana_color = color.blue
    else:
        mana_color = color.darkblue

    if user.SP > 0.66 * user.SPMAX:
        stamina_color = color.limegreen
    elif user.SP > 0.33 * user.SPMAX:
        stamina_color = color.green
    else:
        stamina_color = color.darkgreen

    if user.EXP < 0.33 * user.EXPMAX:
        experience_color = color.plum
    elif user.EXP < 0.66 * user.EXPMAX:
        experience_color = color.purple
    else:
        experience_color = color.indigo

    '''
    if user.REP > 0.66 * user.REP:
        stamina_color = color.limegreen
    elif user.REP > 0.33 * user.REP:
        stamina_color = color.green
    else:
        stamina_color = color.darkgreen

    if user.REP < 0.33 * user.REP:
        stamina_color = color.plum
    elif user.REP < 0.66 * user.REP:
        stamina_color = color.purple
    else:
        stamina_color = color.indigo
    '''

    # printing stats
    if hp:
        print(f"HP: {tutil.numform(user.HP)} / {tutil.numform(user.HPMAX)}")
        print(f"|{health_color}{remaining_health_bars * remaining_bar_symbol}"
                f"{lost_health_bars * lost_bar_symbol}{color_default}|")

    if ap:
        print(f"AP: {tutil.numform(user.AP)} / {tutil.numform(user.APMAX)}")
        print(f"|{aura_color}{remaining_aura_bars * remaining_bar_symbol}"
                f"{lost_aura_bars * lost_bar_symbol}{color_default}|")

    if mp:
        print(f"MP: {tutil.numform(user.MP)} / {tutil.numform(user.MPMAX)}")
        print(f"|{mana_color}{remaining_mana_bars * remaining_bar_symbol}"
                f"{lost_mana_bars * lost_bar_symbol}{color_default}|")

    if sp:
        print(f"SP: {tutil.numform(user.SP)} / {tutil.numform(user.SPMAX)}")
        print(f"|{stamina_color}{remaining_stamina_bars * remaining_bar_symbol}"
                f"{lost_stamina_bars * lost_bar_symbol}{color_default}|")
    
    if xp:
        print(f"EXP: {tutil.numform(user.EXP)} / {tutil.numform(user.EXPMAX)}")
        print(f"|{experience_color}{remaining_experience_bars * remaining_bar_symbol}"
                f"{lost_experience_bars * lost_bar_symbol}{color_default}|")
        
    '''
    if f == rp:
        print(f"REP: {user.REP}")
        print(f"|{stamina_color}{remaining_stamina_bars * remaining_bar_symbol}"
                f"{lost_stamina_bars * lost_bar_symbol}{color_default}|")
    '''