import json
from copy import copy
import re
import os
from dictionaries import *
from functions import *

os.chdir(r'C:\Users\andre\Documents\TEMPLATE HEROCLIX MAKER\Teste henrique')

with open('wkd24.json', 'r') as file:
    deck = json.load(file)

with open('raw_template.json', 'r') as file:
    template = file.read()

collection_name = input("Qual a coleção?")

for character in deck[8:]:

    try:

        card_image = input(f"URL da carta de {character['unit_id']} {character['name']}: ") or "URLCARD"
        figure_image = input(f"URL da miniatura de {character['unit_id']} {character['name']}: ") or "URLFIGURE"

        characterinfo = {
            "GUIDTEMP" : f"c{character['unit_id']}",
            "FIGURENAME" : f"{character['unit_id']} {character['name']}",
            "SETNAME" : collection_name,
            "DIMENSIONS" : character['dimensions'],
            "RANGEOFCLIX" : character['unit_range'],
            "HOWMANYTARGETS" : character['targets'],
            "TEAMABILITY1" : character['team_abilities'][0] if 'team_abilities' in character else "noaffiliation",
            "TEAMABILITY2" : character['team_abilities'][1] if ('team_abilities' in character) and (len(character['team_abilities']) >1) else "noaffiliation",
            "SPEEDSYMBOL" : character['speed_type'],
            "ATTACKSYMBOL" : character['attack_type'],
            "DEFENSESYMBOL" : character['defense_type'],
            "DAMAGESYMBOL" : character['damage_type'],
            "CARDIMAGE" : card_image,
            "FIGUREIMAGE" : figure_image   
        }

        MAX_VALUE = 26
        VALUE = "SPDCLK"
        FIELD_NAME = 'speed_value'
        FIELD_COLOR = 'speed_power'
        SPDCLK_SEQUENCE = build_field_sequence(character, MAX_VALUE, VALUE, FIELD_NAME, FIELD_COLOR)

        MAX_VALUE = 26
        VALUE = "ATTACKCLK"
        FIELD_NAME = 'attack_value'
        FIELD_COLOR = 'attack_power'

        ATKCLK_SEQUENCE = build_field_sequence(character, MAX_VALUE, VALUE, FIELD_NAME, FIELD_COLOR)

        MAX_VALUE = 26
        VALUE = "DEFCLK"
        FIELD_NAME = 'defense_value'
        FIELD_COLOR = 'defense_power'

        DEFCLK_SEQUENCE = build_field_sequence(character, MAX_VALUE, VALUE, FIELD_NAME, FIELD_COLOR)

        MAX_VALUE = 26
        VALUE = "DAMCLK"
        FIELD_NAME = 'damage_value'
        FIELD_COLOR = 'damage_power'

        DAMCLK_SEQUENCE = build_field_sequence(character, MAX_VALUE, VALUE, FIELD_NAME, FIELD_COLOR)

        with open('raw_template.json', 'r') as file:
            text = file.read()

        for key, val in characterinfo.items():
            template = re.sub(f"\\b{str(key)}\\b", str(val), template)

        text = re.sub(r'\bGUIDTEMP\b', characterinfo["GUIDTEMP"], text)
        text = re.sub(r'\bFIGURENAME\b', characterinfo["FIGURENAME"], text)
        text = re.sub(r'\bSETNAME\b', characterinfo["SETNAME"], text)
        text = re.sub(r'\bCARDIMAGEURL\b', characterinfo["CARDIMAGE"], text)
        text = re.sub(r'\bFIGUREIMAGEURL\b', characterinfo["FIGUREIMAGE"], text)
        text = re.sub(r'\bDIMENSIONS\b', hcudimensions_to_ttsdimensions[characterinfo["DIMENSIONS"]], text)
        text = re.sub(r'\bRANGEOFCLIX\b', str(characterinfo["RANGEOFCLIX"]), text)
        text = re.sub(r'\bHOWMANYTARGETS\b', str(hcutarget_to_ttstarget[str(characterinfo["HOWMANYTARGETS"])]), text)
        text = re.sub(r'\bTEAMABILITY1\b', hcuteams_to_ttsteams[characterinfo["TEAMABILITY1"]], text)
        text = re.sub(r'\bTEAMABILITY2\b', hcuteams_to_ttsteams[characterinfo["TEAMABILITY2"]], text)
        text = re.sub(r'\bSPEEDSYMBOL\b', hcuspeedsymbol_to_ttsspeedsymbol[characterinfo["SPEEDSYMBOL"]], text)
        text = re.sub(r'\bATTACKSYMBOL\b', characterinfo["ATTACKSYMBOL"], text)
        text = re.sub(r'\bDEFENSESYMBOL\b', characterinfo["DEFENSESYMBOL"], text)
        text = re.sub(r'\bDAMAGESYMBOL\b', characterinfo["DAMAGESYMBOL"], text)

        for idx, (key, val) in enumerate(SPDCLK_SEQUENCE.items()):
            text = re.sub(r'\bSPDCLK{}\b'.format(idx+1), str(val["value"]), text)
            text = re.sub(r'\bSPEEDCOLOR{}\b'.format(idx+1), val["background_color"], text)
            text = re.sub(r'\bSPEEDTEXTCOLOR{}\b'.format(idx+1), val["text_contrast_color"], text)


        for idx, (key, val) in enumerate(ATKCLK_SEQUENCE.items()):
            text = re.sub(r'\bATTACKCLK{}\b'.format(idx+1), str(val["value"]), text)
            text = re.sub(r'\bATTACKCOLOR{}\b'.format(idx+1), val["background_color"], text)
            text = re.sub(r'\bATTACKTEXTCOLOR{}\b'.format(idx+1), val["text_contrast_color"], text)


        for idx, (key, val) in enumerate(DEFCLK_SEQUENCE.items()):
            text = re.sub(r'\bDEFCLK{}\b'.format(idx+1), str(val["value"]), text)
            text = re.sub(r'\bDEFCOLOR{}\b'.format(idx+1), val["background_color"], text)
            text = re.sub(r'\bDEFTEXTCOLOR{}\b'.format(idx+1), val["text_contrast_color"], text)

        for idx, (key, val) in enumerate(DAMCLK_SEQUENCE.items()):
            text = re.sub(r'\bDAMCLK{}\b'.format(idx+1), str(val["value"]), text)
            text = re.sub(r'\bDAMCOLOR{}\b'.format(idx+1), val["background_color"], text)
            text = re.sub(r'\bDAMTEXTCOLOR{}\b'.format(idx+1), val["text_contrast_color"], text)

        with open(f"{characterinfo['FIGURENAME']}.json", 'w') as f:
            f.write(text)

    except:
        pass