import json
from copy import copy
import re
import os
import pdb

os.chdir(r'C:\Users\andre\Documents\TEMPLATE HEROCLIX MAKER\Teste henrique')

with open('tdw.json', 'r') as file:
    deck = json.load(file)

with open('raw_template.json', 'r') as file:
    template = file.read()

character = deck[0]

collection_name = input("Qual a coleção?")

hcudimensions_to_ttsdimensions = {
    '1x1': '1.0,\\"scaleY\\":1.0,\\"scaleZ\\":1.0',
    '2x1': '2.0,\\"scaleY\\":2.0,\\"scaleZ\\":1.0',
    '2x2': '2.0,\\"scaleY\\":2.0,\\"scaleZ\\":2.0',
    '4x2': '4.0,\\"scaleY\\":4.0,\\"scaleZ\\":2.0',
    '6x3': '6.0,\\"scaleY\\":6.0,\\"scaleZ\\":3.0',
}

hcuspeedsymbol_to_ttsspeedsymbol = {
    'boot': 'boot',
    'transport_boot': 'boot',
    'dolphin': 'dolphin',
    'transport_dolphin': 'transport-dolphin',
    'wing': 'wing',
    'transport_wing': 'transport-wing',
}

hcutarget_to_ttstarget = {
    #convert speed powers to Tabletop Simulator equivalent.
    '1': 'range1',
    '2': 'range2',
    '3': 'range4',
    '4': 'range3',
}

hcuteams_to_ttsteams = {
    #convert team abilities to Tabletop Simulator equivalent.
    'noaffiliation': 'noaffiliation',
    '2000_ad': '2000ad',
    'arachnos': 'arachnos',
    'ascendent': 'ascendent',
    'assassins': 'assassins',
    'avengers': 'avengers',
    'avengers_initiative': 'avengersinitiative',
    'batman_ally': 'batmanally',
    'batman_enemy': 'batmanenemy',
    'borg': 'borg(awayteam)',
    'borg_tactics': 'borg',
    'bprd': 'bprd',
    'brotherhood_of_mutants': 'brotherhoodofmutants',
    'calculator': 'calculator',
    'cardassian': 'cardassian',
    'coalition_of_ordered_governments': 'coalitionoforderedgovernments',
    'council_of_the_mists': 'councilofthemists',
    'covenant_empire': 'covenantempire',
    'crime_syndicate': 'crimesyndicate',
    'crossgen': 'crossgen',
    'crusade': 'crusade',
    'danger_girl': 'dangergirl',
    'defenders': 'defenders',
    'dominion': 'dominion',
    'dominion_pact': 'dominionpact',
    'fantastic_four': 'fantasticfour',
    'federation': 'federation',
    'federation_away_team': 'federationawayteam',
    'federation_support_team': 'federationsupportteam',
    'founders': 'founders',
    'freedom_phalanx': 'freedomphalanx',
    'green_lantern_corps': 'greenlanterncorps',
    'guardians': 'guardians',
    'guardians_of_the_globe': 'guardiansoftheglobe',
    'hydra': 'hydra',
    'hypertime': 'hypertime',
    'injustice_league': 'injusticeleague',
    'justice_league': 'justiceleague',
    'justice_society': 'justicesociety',
    'kabuki': 'kabuki',
    'kaiju': 'kaiju',
    'kingdom_come': 'kingdomcome',
    'klingon_empire': 'klingonempire(awayteam)',
    'klingon_empire_tactics': 'klingonempire',
    'legion_of_super_heroes': 'legionofsuperheroes',
    'locust_horde': 'locusthorde',
    'mage_spawn': 'magespawn',
    'masters_of_evil': 'mastersofevil',
    'mercenary': 'mercenary',
    'minions_of_doom': 'minionsofdoom',
    'mirror_universe': 'mirroruniverse',
    'morlocks': 'morlocks',
    'mystics': 'mystics',
    'outsiders': 'outsiders',
    'pan_pacific_defense_corps': 'panpacificdefensecorps',
    'phoenix_concord': 'phoenixconcord',
    'police': 'police',
    'power_cosmic': 'powercosmic',
    'q_continuum': 'qcontinuum',
    'quintessence': 'quintessence',
    'romulan_star_empire': 'romulanstarempire(awayteam)',
    'romulan_star_empire_tactics': 'romulanstarempire',
    'serpent_society': 'serpentsociety',
    'shield': 'unitshield',
    'sinister_syndicate': 'sinistersyndicate',
    'spider_man': 'spider-man',
    'street_fighter': 'streetfighter',
    'suicide_squad': 'suicidesquad',
    'superman_ally': 'supermanally',
    'superman_enemy': 'supermanenemy',
    'team_player': 'teamplayer',
    'ultimate_x_men': 'ultimatex-men',
    'the_alliance': 'thealliance',
    'titans': 'titans',
    'top_cow': 'topcow',
    'underworld': 'underworld',
    'watchmen': 'watchmen',
    'x_men': 'x-men',
    'cosmic_energy': 'cosmicenergy',
    'ultimates': 'ultimates',
    'wonder_woman_ally': 'wonderwoman',
    'skrulls': 'skrulls',
    'united_federation': 'unitedfederationofplanets',
}

power_to_color = {
    #convert speed powers to Tabletop Simulator equivalent.
    'flurry': 'red',
    'leap_climb': 'orange',
    'phasing_teleport': 'yellow',
    'earthbound_neutralized': 'lime',
    'charge': 'green',
    'mind_control': 'blue',
    'plasticity': 'dblue',
    'force_blast': 'purple',
    'sidestep': 'pink',
    'hypersonic_speed': 'brown',
    'stealth': 'black',
    'running_shot': 'gray',
    'blades_claws_fangs': 'red',
    'energy_explosion': 'orange',
    'pulse_wave': 'yellow',
    'quake': 'lime',
    'super_strength': 'green',
    'incapacitate': 'blue',
    'penetrating_psychic_blast': 'dblue',
    'smoke_cloud': 'purple',
    'precision_strike': 'pink',
    'poison': 'brown',
    'steal_energy': 'black',
    'telekinesis': 'gray',
    'super_senses': 'red',
    'toughness': 'orange',
    'defend': 'yellow',
    'combat_reflexes': 'lime',
    'energy_shield_deflection': 'green',
    'barrier': 'blue',
    'mastermind': 'dblue',
    'willpower': 'purple',
    'invincible': 'pink',
    'impervious': 'brown',
    'regeneration': 'black',
    'invulnerability': 'gray',
    'ranged_combat_expert': 'red',
    'battle_fury': 'orange',
    'support': 'yellow',
    'exploit_weakness': 'lime',
    'enhancement': 'green',
    'probability_control': 'blue',
    'shape_change': 'dblue',
    'close_combat_expert': 'purple',
    'empower': 'pink',
    'perplex': 'brown',
    'outwit': 'black',
    'leadership': 'gray',
    "special" : "special"
}

#Define the contrast of the text color and background color
TEXTCOLORTOBLACK = ["white", "special", "red", "orange", "yellow", "lime", "green", "blue", "pink"]
TEXTCOLORTOWHITE = ["dblue", "purple", "brown", "black", "gray"]
TEXTCOLORTOCLEAR = "ko"

#Creates a dictionary based on current character
def build_field_sequence(character, max_value, VALUE, field_name, field_color):
    seq_dictionary = dict()

    #Fills all fields with default answers
    for idx in range(max_value):
        seq_dictionary[f"{VALUE}{idx + 1}"] = {
            "value" : "clear",
            "background_color" : TEXTCOLORTOCLEAR,
            "text_contrast_color" : "clear",
        }

    for dial in character['dial']:

        # Realiza o preenchimento em cima de clear com os valores em dial
        # pdb.set_trace()
        try:
            if field_color in dial:
                background_color = power_to_color[dial[field_color]]
            else:
                background_color = "white"
        except:
            raise Exception(f"cor {dial[field_color]} não encontrada")

        if background_color in TEXTCOLORTOBLACK:
          text_contrast_color = "black"
        elif background_color in TEXTCOLORTOWHITE: 
          text_contrast_color = "white"
        else:
            text_contrast_color = "clear"
        # text_contrast_color

        seq_dictionary[f"{VALUE}{dial['click_number']}"] = {
            "value" : dial[field_name],
            "background_color" : background_color,
            "text_contrast_color" : text_contrast_color,
        }
    return seq_dictionary

card_image = input(f"URL da carta de {character['unit_id']} {character['name']}: ") or "URLCARD"
figure_image = input(f"URL da miniatura de {character['unit_id']} {character['name']}: ") or "URLFIGURE"

characterinfo = {
    "GUIDTEMP" : f"c{character['unit_id']}",
    "FIGURENAME" : f"{character['unit_id']} {character['name']}",
    "SETNAME" : collection_name,
    "DIMENSIONS" : character['dimensions'],
    "RANGEOFCLIX" : character['unit_range'],
    "HOWMANYTARGETS" : character['targets'],
    "TEAMABILITY1" : character['team_abilities'][0] if "team_abilities" in character else "noaffiliation",
    "TEAMABILITY2" : character['team_abilities'][1] if "team_abilities" in character else "noaffiliation",
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
text = re.sub(r'\bSPEEDSYMBOL\b', characterinfo["SPEEDSYMBOL"], text)
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