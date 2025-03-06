# Items

class Item:
    def __init__(self, name, technicalName, grade, condition, description, itemTag):
        self.name = name
        self.technicalName = technicalName
        self.grade = grade
        self.itemTag = itemTag
        self.condition = condition
        self.description = description

    # Grades
    u_grade = "U"
    sp_grade = "S+"
    s_grade = "S"
    a_grade = "A"
    b_grade = "B"
    c_grade = "C"
    d_grade = "D"
    f_grade = "F"

    # Condition    
    pristine = 1.0
    undamaged = 0.9
    durable = 0.8
    tested = 0.7
    blemished = 0.6
    worn = 0.5
    damaged = 0.4
    weakened = 0.3
    fragile = 0.2
    compromised = 0.1
    unusable = 0

    # Effects
    pHP = 10
    ppHP = 20
    pAP = 10
    ppAP = 20
    pMP = 10
    ppMP = 20
    pSP = 10
    ppSP = 20

    pSTR = 10
    pDEF = 10
    pSPD = 10
    pAGI = 10
    pPRO = 10
    pMAG = 10
    pCHR = 10
    pINT = 10
    pFRT = 10
    pLUC = 10

    # Item tags
    weapon_tag = "0000"
    sword_tag = "0001"
    knife_tag = "0002"
    potion_tag = "0003"
    health_tag = "0004"
    magic_tag = "0005"
    wearable_tag = "0006"
    head_tag = "0007"
    ear_tag = "0008"
    eye_tag = "0009"
    neck_tag = "0010"
    shoulder_tag = "0011" 
    back_tag = "0012"
    chest_tag = "0013"
    arm_tag = "0014"
    wrist_tag = "0015"
    hand_tag = "0016"
    finger_tag = "0017"
    waist_tag = "0018"
    leg_tag = "0019"
    foot_tag = "0020"