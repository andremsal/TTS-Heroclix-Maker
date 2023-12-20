import json
from copy import copy
import re


with open('avm.json', 'r') as file:
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
dial = character['dial'][0]

import pdb

target_dict = {
    #convert speed powers to Tabletop Simulator equivalent.
    '1': 'r1',
    '2': 'r2',
    '3': 'r4',
    '4': 'r3',
}

letter_to_word = {
    #convert speed powers to Tabletop Simulator equivalent.
    'avengers_initiative': 'avengersinitiative',
}

# 1. montar a lógica para definir as cores aqui.
letter_to_word = {
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
}

# 2. exceções
# 3. as cores de contrastes do texto

# TEXTCOLORTOBLACK = ["white", "special", "red", "orange", "yellow", "lime", "green", "blue", "pink"]
# TEXTCOLORTOWHITE = ["dblue", "purple", "brown", "black", "gray"]
# CLICKPOWERS = [[0 for x in range(12)] for x in range(4)]

# if CLICKPOWERS[i][idx] in TEXTCOLORTOBLACK:
#                 CLICKTXTCOLORS[i][idx] = "black"
#             elif CLICKPOWERS[i][idx] in TEXTCOLORTOWHITE:
#                 CLICKTXTCOLORS[i][idx] = "white"
#             else:
#                 CLICKTXTCOLORS[i][idx] = "clear"


# 4. Converter as dimensões para texto (outra função)

def build_field_sequence(character, max_value, VALUE, field_name):
    seq_dictionary = dict()
    for idx in range(max_value):
        seq_dictionary[f"{VALUE}{idx + 1}"] = "clear"

    for dial in character['dial']:
        seq_dictionary[f"{VALUE}{dial['click_number']}"] = dial[field_name]

    return seq_dictionary

MAX_VALUE = 26
VALUE = "SPDCLK"
FIELD_NAME = 'speed_value'

print(build_field_sequence(character, MAX_VALUE, VALUE, FIELD_NAME))

MAX_VALUE = 26
VALUE = "ATTACKCLK"
FIELD_NAME = 'attack_value'

print(build_field_sequence(character, MAX_VALUE, VALUE, FIELD_NAME))
MAX_VALUE = 26
VALUE = "DEFENSECLK"
FIELD_NAME = 'defense_value'

print(build_field_sequence(character, MAX_VALUE, VALUE, FIELD_NAME))
MAX_VALUE = 26
VALUE = "DAMAGEKCLK"
FIELD_NAME = 'damage_value'

print(build_field_sequence(character, MAX_VALUE, VALUE, FIELD_NAME))
