import json
import re
import os
import requests
from copy import copy
from dictionaries import *
from functions import *

# Ensure the script runs in its own directory
current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)

# Get collection name from user input
collection_code = input("Qual o id da coleção (ex: wk25)? ")
collection_name = input("Qual o nome da coleção (ex: Wizkids 2025)? ")
search_url = f"https://hcunits.net/api/v1/units/?ext=json&set_id={collection_code}"
print(f"Buscando unidades da coleção {collection_code}...")
all_units = []

# Fetch all units from the API with pagination
while search_url:
    
    # Make the API request
    response = requests.get(search_url)

    # Check for request errors
    if response.status_code != 200:
        print(f"Erro ao acessar a API: Status {response.status_code}")
        exit()

    # Parse response data
    data = response.json()

    # Determine if data is a list or contains 'results'
    if isinstance(data, dict) and 'results' in data:
        all_units.extend(data['results'])
        search_url = data.get('next')
    elif isinstance(data, list):
        all_units.extend(data)
        search_url = None
    else:
        print("Formato de resposta inesperado ou nenhum resultado encontrado.")
        exit()

# Filter units to get only characters
character_ids = [u['id'] for u in all_units if u.get('type') == 'character']
print(f"Encontrados {len(character_ids)} / {len(all_units)} personagens do tipo 'character'.")

# Open Tabletop Simulator Character Template
with open('raw_template.json', 'r') as file:
    template = file.read()

# Iterates Each Character
for id in character_ids:

    try:
        # Download unit details
        print(f"Baixando detalhes da unidade: {id}...")
        unit_url = f"https://hcunits.net/api/v1/units/{id}/?ext=json"
        unit_data = requests.get(unit_url).json()

        # Prepare character with unit data
        character = unit_data
        card_image = input(f"URL da carta de {character['id']} {character['name']}: ") or "URLCARD"
        figure_image = input(f"URL da miniatura de {character['id']} {character['name']}: ") or "URLFIGURE"
        team_abilities = character.get('team_abilities', [])

        # Build character info dictionary
        characterinfo = {
            "GUIDTEMP" : f"c{character['id']}",
            "FIGURENAME" : f"{character['id']} {character['name']}",
            "SETNAME" : collection_name,
            "DIMENSIONS" : character['dimensions'],
            "RANGEOFCLIX" : character['unit_range'],
            "HOWMANYTARGETS" : character['targets'],
            "TEAMABILITY1" : team_abilities[0] if len(team_abilities) > 0 else "noaffiliation",
            "TEAMABILITY2" : team_abilities[1] if len(team_abilities) > 1 else "noaffiliation",
            "SPEEDSYMBOL" : character['combat_symbols'][0],
            "ATTACKSYMBOL" : character['combat_symbols'][1],
            "DEFENSESYMBOL" : character['combat_symbols'][2],
            "DAMAGESYMBOL" : character['combat_symbols'][3],
            "CARDIMAGE" : card_image,
            "FIGUREIMAGE" : figure_image   
        }

        # Build Speed Clicks sequence
        MAX_VALUE = 26
        VALUE = "SPDCLK"
        FIELD_NAME = 'speed_value'
        FIELD_COLOR = 'speed_power'
        SPDCLK_SEQUENCE = build_field_sequence(character, MAX_VALUE, VALUE, FIELD_NAME, FIELD_COLOR)

        # Build Attack Clicks sequence
        MAX_VALUE = 26
        VALUE = "ATTACKCLK"
        FIELD_NAME = 'attack_value'
        FIELD_COLOR = 'attack_power'
        ATKCLK_SEQUENCE = build_field_sequence(character, MAX_VALUE, VALUE, FIELD_NAME, FIELD_COLOR)
        
        # Build Defense Clicks sequence
        MAX_VALUE = 26
        VALUE = "DEFCLK"
        FIELD_NAME = 'defense_value'
        FIELD_COLOR = 'defense_power'
        DEFCLK_SEQUENCE = build_field_sequence(character, MAX_VALUE, VALUE, FIELD_NAME, FIELD_COLOR)

        # Build Damage Clicks sequence
        MAX_VALUE = 26
        VALUE = "DAMCLK"
        FIELD_NAME = 'damage_value'
        FIELD_COLOR = 'damage_power'
        DAMCLK_SEQUENCE = build_field_sequence(character, MAX_VALUE, VALUE, FIELD_NAME, FIELD_COLOR)

        # Set text to default template information
        text = template

        # Perform replacements
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

        # Save character file locally
        with open(f"{characterinfo['FIGURENAME']}.json", 'w') as f:
            f.write(text)

    # Handle exceptions
    except Exception as e:
        print(f"Erro ao processar {id}: {e}")
        continue