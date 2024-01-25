hcudimensions_to_ttsdimensions = {
    #convert hcunits dimensions to Tabletop Simulator equivalent.
    '1x1': '1.0,\\"scaleY\\":1.0,\\"scaleZ\\":1.0',
    '2x1': '2.0,\\"scaleY\\":2.0,\\"scaleZ\\":1.0',
    '2x2': '2.0,\\"scaleY\\":2.0,\\"scaleZ\\":2.0',
    '4x2': '4.0,\\"scaleY\\":4.0,\\"scaleZ\\":2.0',
    '6x3': '6.0,\\"scaleY\\":6.0,\\"scaleZ\\":3.0',
}

hcuspeedsymbol_to_ttsspeedsymbol = {
    #convert speed symbols from hcunits to Tabletop Simulator equivalent.
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
