import os
import re

os.chdir(r'C:\Users\andre\Documents\TEMPLATE HEROCLIX MAKER\Teste henrique')

with open('projectheroclix2021template.json', 'r') as file:
    text = file.read()

letter_to_word = {
    'b!': 'black',
    'c!': 'clear',
    'w!': 'white',
    'r1': 'range1',
    'r2': 'range2',
    'r3': 'range3',
    'r4': 'range4',
}

BASEDIMENSIONS = [0 for x in range(3)]
DIMENSIONS = ["width", "height", "length"]
VALIDBOLTS = ["r1", "r2", "r3", "r4", "range1", "range2", "range3", "range4"]
TEAMABILITY = [0 for x in range(2)]
VALIDTEAMABILITIES = ["noaffiliation", "2000ad", "arachnos", "ascendent", "assassins", "avengers", "avengersinitiative", "batmanally", "batmanenemy", "borg(awayteam)", "borg", "bprd", "brotherhoodofmutants", "calculator", "cardassian", "coalitionoforderedgovernments", "councilofthemists", "covenantempire", "crimesyndicate", "crossgen", "crusade", "dangergirl", "defenders", "dominion", "dominionpact", "fantasticfour", "federation", "federationawayteam", "federationsupportteam", "founders", "freedomphalanx", "greenlanterncorps", "guardians", "guardiansoftheglobe", "hydra", "hypertime", "injusticeleague", "justiceleague", "justicesociety", "kabuki", "kaiju", "kingdomcome", "klingonempire(awayteam)", "klingonempire", "legionofsuperheroes", "locusthorde", "magespawn", "masterofevil", "mastersofevil", "mercenary", "minionsofdoom", "mirroruniverse", "morlocks", "mystics", "outsiders", "panpacificdefensecorps", "phoenixconcord", "police", "powercosmic", "qcontinuum", "quintessence", "romulanstarempire(awayteam)", "romulanstarempire", "serpentsociety", "unitshield", "sinistersyndicate", "spider-man", "streetfighter", "suicidesquad", "supermanally", "supermanenemy", "teamplayer", "ultimatex-men", "thealliance", "titans", "topcow", "underworld", "watchmen", "x-men", "cosmicenergy", "ultimates", "wonderwoman", "skrulls", "unitedfederationofplanets"]
COMBATSLOT = ["speed", "attack", "defense", "damage"]
COMBATSYMBOL = [0 for x in range(4)]
VALIDCOMBATSYMBOLS = [["boot", "transport-boot", "wing", "transport-wing", "dolphin", "transport-dolphin"], ["fist", "autonomous", "duo", "sharpshooter", "team"], ["indomitable", "shield", "vehicle"], ["starburst", "tiny", "giant", "colossal"]]
CLICKVALUES = [[0 for x in range(12)] for x in range(4)]
CLICKPOWERS = [[0 for x in range(12)] for x in range(4)]
CLICKTXTCOLORS = [[0 for x in range(12)] for x in range(4)]
TEXTCOLORTOBLACK = ["white", "special", "red", "orange", "yellow", "lime", "green", "blue", "pink"]
TEXTCOLORTOWHITE = ["dblue", "purple", "brown", "black", "gray"]
VALIDCOLORS = ["ko", "clear", "white", "special","red", "orange", "yellow", "lime", "green", "blue", "dblue", "purple", "pink", "brown", "black", "gray"]

GUIDTEMP = input("What is the ID of the character? Example btu001. ")
print(GUIDTEMP)

NICKNAMETEMP = input("What is the nickname of the Clix? Example Robin. ")
print(NICKNAMETEMP)

SETNAME = input("What set does this Clix Come from? Example Batman Team-Up. ")
print(SETNAME)

idx = 0
while idx < 3:
    BASEDIMENSIONS[idx] = input(f"What is the figure's {DIMENSIONS[idx]}? Usually 1-6. ") or "1"
    print(BASEDIMENSIONS[idx])
    idx += 1

RANGEOFCLIX = input("What is the Clix Range value? Usually 0-16. ") or "0"
print(RANGEOFCLIX)

idx = 0
while idx < 1:
    HOWMANYTARGETS = input(("How many Targets does this Clix have? Example for 1 bolt: r1 or range1, for 2 bolts: r2/range2, "
                            "for 3 bolts: r4/range4, for 4 bolts: r3/range3?")) or "r1"

    if HOWMANYTARGETS in VALIDBOLTS:
        print(f"Number of bolts is {HOWMANYTARGETS}")
        idx += 1
    else:
        print("Incorrect syntax, please repeat: ")

idx = 0
while idx < 2:
    TEAMABILITY[idx] = input(f"What is the figure Team Ability {idx+1}? syntax - {VALIDTEAMABILITIES}") or "noaffiliation"
    
    if TEAMABILITY[idx] in VALIDTEAMABILITIES:
        print(f"Team ability {idx+1} is {TEAMABILITY[idx]}")
        idx += 1
    else:
        print("Incorrect syntax, please repeat: ")

idx = 0
while idx < 4:
    COMBATSYMBOL[idx] = input(f"What is the Clix {COMBATSLOT[idx]} symbol? syntax - {VALIDCOMBATSYMBOLS[idx]}") or VALIDCOMBATSYMBOLS[idx][0]

    if COMBATSYMBOL[idx] in VALIDCOMBATSYMBOLS[idx]:
        print(f"{COMBATSLOT[idx]} symbol is {COMBATSYMBOL[idx]}")
        idx += 1
    else:
        print("Incorrect syntax, please repeat: ") or VALIDCOMBATSYMBOLS[idx][0]

for i in range(0, 4):
    for j in range(0, 12):
        CLICKVALUES[i][j]= input(f"What is the Clix {COMBATSLOT[i]} value on click {j+1}? syntax - 0-99 or clear? ") or "clear"
        print(CLICKVALUES[i][j])

for i in range(0, 4):
    idx = 0
    while idx < 12:
        CLICKPOWERS[i][idx]= str(input(f"What is the Clix {COMBATSLOT[i]} power on click {idx+1} syntax - ko, clear, white, special"
                             ", red, orange, yellow, lime, green, blue, dblue, purple, pink, brown, black, gray? ") or "ko")
    
        if CLICKPOWERS[i][idx] in VALIDCOLORS:       

            if CLICKPOWERS[i][idx] in TEXTCOLORTOBLACK:
                CLICKTXTCOLORS[i][idx] = "black"
            elif CLICKPOWERS[i][idx] in TEXTCOLORTOWHITE:
                CLICKTXTCOLORS[i][idx] = "white"
            else:
                CLICKTXTCOLORS[i][idx] = "clear"

            print(f"Power color: {CLICKPOWERS[i][idx]}")
            print(f"Text color: {CLICKTXTCOLORS[i][idx]}") 

            idx += 1

        else:
            print("Incorrect syntax please repeat: ")

CARDIMAGEURL = input("What is the card image URL? paste full URL here->")
print(CARDIMAGEURL)

FIGUREIMAGEURL = input("What is the figure image URL? paste full URL here->")
print(FIGUREIMAGEURL)


text = re.sub('GUIDTEMP', "c" + GUIDTEMP, text)
text = re.sub('FIGURENAME', GUIDTEMP + " " + NICKNAMETEMP, text)
text = re.sub('SETNAME', SETNAME, text)

idx = 0
text = re.sub(r'\bWIDTHTEMP\b', BASEDIMENSIONS[idx], text)
idx += 1
text = re.sub(r'\bHEIGHTTEMP\b', BASEDIMENSIONS[idx], text)
idx += 1
text = re.sub(r'\bLENGTHTMP\b', BASEDIMENSIONS[idx], text)

text = re.sub(r'\bRANGEOFCLIX\b', RANGEOFCLIX, text)
text = re.sub(r'\bHOWMANYTARGETS\b', HOWMANYTARGETS, text)

idx = 0
text = re.sub(r'\bTEAMABILITY1\b', TEAMABILITY[idx], text)
idx += 1
text = re.sub(r'\bTEAMABILITY2\b', TEAMABILITY[idx], text)

idx = 0
text = re.sub(r'\bSPEEDSYMBOL\b', COMBATSYMBOL[idx], text)
idx += 1
text = re.sub(r'\bATTACKSYMBOL\b', COMBATSYMBOL[idx], text)
idx += 1
text = re.sub(r'\bDEFENSESYMBOL\b', COMBATSYMBOL[idx], text)
idx += 1
text = re.sub(r'\bDAMAGESYMBOL\b', COMBATSYMBOL[idx], text)

idx = 0
idx2 = 0
text = re.sub(r'\bSPDCLK1\b', CLICKVALUES[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bSPDCLK2\b', CLICKVALUES[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bSPDCLK3\b', CLICKVALUES[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bSPDCLK4\b', CLICKVALUES[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bSPDCLK5\b', CLICKVALUES[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bSPDCLK6\b', CLICKVALUES[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bSPDCLK7\b', CLICKVALUES[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bSPDCLK8\b', CLICKVALUES[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bSPDCLK9\b', CLICKVALUES[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bSPDCLK10\b', CLICKVALUES[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bSPDCLK11\b', CLICKVALUES[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bSPDCLK12\b', CLICKVALUES[idx][idx2], text)
idx += 1
idx2 = 0
text = re.sub(r'\bATTACKCLK1\b', CLICKVALUES[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bATTACKCLK2\b', CLICKVALUES[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bATTACKCLK3\b', CLICKVALUES[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bATTACKCLK4\b', CLICKVALUES[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bATTACKCLK5\b', CLICKVALUES[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bATTACKCLK6\b', CLICKVALUES[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bATTACKCLK7\b', CLICKVALUES[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bATTACKCLK8\b', CLICKVALUES[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bATTACKCLK9\b', CLICKVALUES[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bATTACKCLK10\b', CLICKVALUES[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bATTACKCLK11\b', CLICKVALUES[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bATTACKCLK12\b', CLICKVALUES[idx][idx2], text)
idx += 1
idx2 = 0
text = re.sub(r'\bDEFCLK1\b', CLICKVALUES[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDEFCLK2\b', CLICKVALUES[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDEFCLK3\b', CLICKVALUES[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDEFCLK4\b', CLICKVALUES[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDEFCLK5\b', CLICKVALUES[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDEFCLK6\b', CLICKVALUES[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDEFCLK7\b', CLICKVALUES[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDEFCLK8\b', CLICKVALUES[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDEFCLK9\b', CLICKVALUES[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDEFCLK10\b', CLICKVALUES[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDEFCLK11\b', CLICKVALUES[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDEFCLK12\b', CLICKVALUES[idx][idx2], text)
idx += 1
idx2 = 0
text = re.sub(r'\bDAMCLK1\b', CLICKVALUES[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDAMCLK2\b', CLICKVALUES[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDAMCLK3\b', CLICKVALUES[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDAMCLK4\b', CLICKVALUES[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDAMCLK5\b', CLICKVALUES[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDAMCLK6\b', CLICKVALUES[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDAMCLK7\b', CLICKVALUES[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDAMCLK8\b', CLICKVALUES[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDAMCLK9\b', CLICKVALUES[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDAMCLK10\b', CLICKVALUES[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDAMCLK11\b', CLICKVALUES[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDAMCLK12\b', CLICKVALUES[idx][idx2], text)

idx = 0
idx2 = 0
text = re.sub(r'\bSPEEDCOLOR1\b', CLICKPOWERS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bSPEEDCOLOR2\b', CLICKPOWERS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bSPEEDCOLOR3\b', CLICKPOWERS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bSPEEDCOLOR4\b', CLICKPOWERS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bSPEEDCOLOR5\b', CLICKPOWERS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bSPEEDCOLOR6\b', CLICKPOWERS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bSPEEDCOLOR7\b', CLICKPOWERS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bSPEEDCOLOR8\b', CLICKPOWERS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bSPEEDCOLOR9\b', CLICKPOWERS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bSPEEDCOLOR10\b', CLICKPOWERS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bSPEEDCOLOR11\b', CLICKPOWERS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bSPEEDCOLOR12\b', CLICKPOWERS[idx][idx2], text)
idx += 1
idx2 = 0
text = re.sub(r'\bATTACKCOLOR1\b', CLICKPOWERS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bATTACKCOLOR2\b', CLICKPOWERS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bATTACKCOLOR3\b', CLICKPOWERS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bATTACKCOLOR4\b', CLICKPOWERS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bATTACKCOLOR5\b', CLICKPOWERS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bATTACKCOLOR6\b', CLICKPOWERS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bATTACKCOLOR7\b', CLICKPOWERS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bATTACKCOLOR8\b', CLICKPOWERS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bATTACKCOLOR9\b', CLICKPOWERS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bATTACKCOLOR10\b', CLICKPOWERS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bATTACKCOLOR11\b', CLICKPOWERS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bATTACKCOLOR12\b', CLICKPOWERS[idx][idx2], text)
idx += 1
idx2 = 0
text = re.sub(r'\bDEFCOLOR1\b', CLICKPOWERS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDEFCOLOR2\b', CLICKPOWERS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDEFCOLOR3\b', CLICKPOWERS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDEFCOLOR4\b', CLICKPOWERS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDEFCOLOR5\b', CLICKPOWERS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDEFCOLOR6\b', CLICKPOWERS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDEFCOLOR7\b', CLICKPOWERS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDEFCOLOR8\b', CLICKPOWERS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDEFCOLOR9\b', CLICKPOWERS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDEFCOLOR10\b', CLICKPOWERS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDEFCOLOR11\b', CLICKPOWERS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDEFCOLOR12\b', CLICKPOWERS[idx][idx2], text)
idx += 1
idx2 = 0
text = re.sub(r'\bDAMCOLOR1\b', CLICKPOWERS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDAMCOLOR2\b', CLICKPOWERS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDAMCOLOR3\b', CLICKPOWERS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDAMCOLOR4\b', CLICKPOWERS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDAMCOLOR5\b', CLICKPOWERS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDAMCOLOR6\b', CLICKPOWERS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDAMCOLOR7\b', CLICKPOWERS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDAMCOLOR8\b', CLICKPOWERS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDAMCOLOR9\b', CLICKPOWERS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDAMCOLOR10\b', CLICKPOWERS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDAMCOLOR11\b', CLICKPOWERS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDAMCOLOR12\b', CLICKPOWERS[idx][idx2], text)

idx = 0
idx2 = 0
text = re.sub(r'\bSPEEDTEXTCOLOR1\b', CLICKTXTCOLORS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bSPEEDTEXTCOLOR2\b', CLICKTXTCOLORS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bSPEEDTEXTCOLOR3\b', CLICKTXTCOLORS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bSPEEDTEXTCOLOR4\b', CLICKTXTCOLORS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bSPEEDTEXTCOLOR5\b', CLICKTXTCOLORS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bSPEEDTEXTCOLOR6\b', CLICKTXTCOLORS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bSPEEDTEXTCOLOR7\b', CLICKTXTCOLORS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bSPEEDTEXTCOLOR8\b', CLICKTXTCOLORS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bSPEEDTEXTCOLOR9\b', CLICKTXTCOLORS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bSPEEDTEXTCOLOR10\b', CLICKTXTCOLORS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bSPEEDTEXTCOLOR11\b', CLICKTXTCOLORS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bSPEEDTEXTCOLOR12\b', CLICKTXTCOLORS[idx][idx2], text)
idx += 1
idx2 = 0
text = re.sub(r'\bATTACKTEXTCOLOR1\b', CLICKTXTCOLORS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bATTACKTEXTCOLOR2\b', CLICKTXTCOLORS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bATTACKTEXTCOLOR3\b', CLICKTXTCOLORS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bATTACKTEXTCOLOR4\b', CLICKTXTCOLORS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bATTACKTEXTCOLOR5\b', CLICKTXTCOLORS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bATTACKTEXTCOLOR6\b', CLICKTXTCOLORS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bATTACKTEXTCOLOR7\b', CLICKTXTCOLORS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bATTACKTEXTCOLOR8\b', CLICKTXTCOLORS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bATTACKTEXTCOLOR9\b', CLICKTXTCOLORS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bATTACKTEXTCOLOR10\b', CLICKTXTCOLORS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bATTACKTEXTCOLOR11\b', CLICKTXTCOLORS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bATTACKTEXTCOLOR12\b', CLICKTXTCOLORS[idx][idx2], text)
idx += 1
idx2 = 0
text = re.sub(r'\bDEFTEXTCOLOR1\b', CLICKTXTCOLORS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDEFTEXTCOLOR2\b', CLICKTXTCOLORS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDEFTEXTCOLOR3\b', CLICKTXTCOLORS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDEFTEXTCOLOR4\b', CLICKTXTCOLORS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDEFTEXTCOLOR5\b', CLICKTXTCOLORS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDEFTEXTCOLOR6\b', CLICKTXTCOLORS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDEFTEXTCOLOR7\b', CLICKTXTCOLORS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDEFTEXTCOLOR8\b', CLICKTXTCOLORS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDEFTEXTCOLOR9\b', CLICKTXTCOLORS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDEFTEXTCOLOR10\b', CLICKTXTCOLORS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDEFTEXTCOLOR11\b', CLICKTXTCOLORS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDEFTEXTCOLOR12\b', CLICKTXTCOLORS[idx][idx2], text)
idx += 1
idx2 = 0
text = re.sub(r'\bDAMTEXTCOLOR1\b', CLICKTXTCOLORS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDAMTEXTCOLOR2\b', CLICKTXTCOLORS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDAMTEXTCOLOR3\b', CLICKTXTCOLORS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDAMTEXTCOLOR4\b', CLICKTXTCOLORS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDAMTEXTCOLOR5\b', CLICKTXTCOLORS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDAMTEXTCOLOR6\b', CLICKTXTCOLORS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDAMTEXTCOLOR7\b', CLICKTXTCOLORS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDAMTEXTCOLOR8\b', CLICKTXTCOLORS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDAMTEXTCOLOR9\b', CLICKTXTCOLORS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDAMTEXTCOLOR10\b', CLICKTXTCOLORS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDAMTEXTCOLOR11\b', CLICKTXTCOLORS[idx][idx2], text)
idx2 += 1
text = re.sub(r'\bDAMTEXTCOLOR12\b', CLICKTXTCOLORS[idx][idx2], text)

text = re.sub(r'\bCARDIMAGEURL\b', CARDIMAGEURL, text)
text = re.sub(r'\bFIGUREIMAGEURL\b', FIGUREIMAGEURL, text)

word_to_replacement = {
    'b!': 'black',
    'c!': 'clear',
    'w!': 'white',
    'r1': 'range1',
    'r2': 'range2',
    'r3': 'range3',
    'r4': 'range4',
}

content = text

for word, replacement in word_to_replacement.items():
    content = content.replace(word, replacement)

with open(GUIDTEMP + " " + NICKNAMETEMP + '.json', 'w') as f:
    f.write(content)