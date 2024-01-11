import json
from copy import copy
import re
import os

os.chdir(r'C:\Users\andre\Documents\TEMPLATE HEROCLIX MAKER\Teste henrique')

with open('tdw.json', 'r') as file:
    deck = json.load(file)

with open('raw_template.json', 'r') as file:
    template = file.read()


character = deck[0]


collection_name = input("Qual a coleção?")

replacements = {
    "GUIDTEMP" : character['unit_id'],
    "FIGURENAME" : f"{character['unit_id']} {character['name']}",
    "SETNAME" : collection_name,
}

for key, val in replacements.items():
    template = re.sub(f"\\b{key}\\b", val, template)


# caso necessário realizar o sorting baseado no click_number
# dial = character['dial'][0]

import pdb

hcudimensions_to_ttsdimensions = {
    '1x1': '1.0,\\"scaleY\\":1.0,\\"scaleZ\\":1.0',
    '2x1': '2.0,\\"scaleY\\":2.0,\\"scaleZ\\":1.0',
    '2x2': '2.0,\\"scaleY\\":2.0,\\"scaleZ\\":2.0',
    '4x2': '4.0,\\"scaleY\\":4.0,\\"scaleZ\\":2.0',
    '6x3': '6.0,\\"scaleY\\":6.0,\\"scaleZ\\":3.0',
}

hcutarget_to_ttstarget = {
    #convert speed powers to Tabletop Simulator equivalent.
    '1': 'r1',
    '2': 'r2',
    '3': 'r4',
    '4': 'r3',
}

hcuteams_to_ttsteams = {
    #convert speed powers to Tabletop Simulator equivalent.
    'avengers_initiative': 'avengersinitiative',
}

# 1. montar a lógica para definir as cores aqui.
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

# 2. exceções

# 3. as cores de contrastes do texto

TEXTCOLORTOBLACK = ["white", "special", "red", "orange", "yellow", "lime", "green", "blue", "pink"]
TEXTCOLORTOWHITE = ["dblue", "purple", "brown", "black", "gray"]
TEXTCOLORTOCLEAR = "ko"


# CLICKPOWERS = [[0 for x in range(12)] for x in range(4)]

# if CLICKPOWERS[i][idx] in TEXTCOLORTOBLACK:
#                 CLICKTXTCOLORS[i][idx] = "black"
#             elif CLICKPOWERS[i][idx] in TEXTCOLORTOWHITE:
#                 CLICKTXTCOLORS[i][idx] = "white"
#             else:
#                 CLICKTXTCOLORS[i][idx] = "clear"


# 4. Converter as dimensões para texto (outra função)
import pdb


def build_field_sequence(character, max_value, VALUE, field_name, field_color):
    seq_dictionary = dict()

    # Preenche tudo com clear
    for idx in range(max_value):
        seq_dictionary[f"{VALUE}{idx + 1}"] = {
            "value" : "clear",
            "background_color" : TEXTCOLORTOCLEAR,
            "text_contrast_color" : "clear",
        }
        # seq_dictionary[f"{VALUE}{idx + 1}"] = "clear"


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


MAX_VALUE = 26
VALUE = "SPDCLK"
FIELD_NAME = 'speed_value'
FIELD_COLOR = 'speed_power'

print(build_field_sequence(character, MAX_VALUE, VALUE, FIELD_NAME, FIELD_COLOR))

print("22222222222222222222222222222222222222222222222222222222")

MAX_VALUE = 26
VALUE = "ATKCLK"
FIELD_NAME = 'attack_value'
FIELD_COLOR = 'attack_power'

print(build_field_sequence(character, MAX_VALUE, VALUE, FIELD_NAME, FIELD_COLOR))

print("22222222222222222222222222222222222222222222222222222222")

MAX_VALUE = 26
VALUE = "DEFCLK"
FIELD_NAME = 'defense_value'
FIELD_COLOR = 'defense_power'

print(build_field_sequence(character, MAX_VALUE, VALUE, FIELD_NAME, FIELD_COLOR))


# MAX_VALUE = 26
# VALUE = "ATTACKCLK"
# FIELD_NAME = 'attack_value'

# print(build_field_sequence(character, MAX_VALUE, VALUE, FIELD_NAME))
# MAX_VALUE = 26
# VALUE = "DEFENSECLK"
# FIELD_NAME = 'defense_value'

# print(build_field_sequence(character, MAX_VALUE, VALUE, FIELD_NAME))
# MAX_VALUE = 26
# VALUE = "DAMAGEKCLK"
# FIELD_NAME = 'damage_value'

# print(build_field_sequence(character, MAX_VALUE, VALUE, FIELD_NAME))
