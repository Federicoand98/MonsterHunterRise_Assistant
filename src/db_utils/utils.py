import json
import os
import string
from db_data import *

PARTS = ['HEAD', 'NECK', 'TAIL', 'TORSO', 'WING', 'LEG', 'BACK', 'ABDOMEN', 'HORN',
    'FORELEG', 'CUTWING', 'THORNS', 'MANE', 'HIP', 'BODY', 'HALF', 'REAR', 'FIN', 'CLUMP',
         'CLAW', 'WINGARM', 'CHEST', 'ARMBLADE', 'TAILBLADE', 'MUDBULB', 'SNOUT', 'TONGUE', 'BOULDER']

MONSTER_NAMES = ['Rathian', 'Rathalos', 'Khezu', 'Basarios', 'Diablos', 'Rajang', 'Kushala',
    'Chameleos', 'Teostra', 'Tigrex', 'Nargacuga', 'Barioth', 'Barroth', 'Ludroth', 'Baggi',
    'Zinogre', 'Wroggi', 'Arzuros', 'Lagombi', 'Volvidon', 'Mizutsune', 'Valstrax', 'Magnamalo',
    'Bishaten', 'Aknosom', 'Tetranadon', 'Somnacanth', 'Rakna-Kadaki', 'Almudron', 'Ibushi',
                 'Goss', 'Izuchi', 'Narwa', 'Anjanath', 'Pukei-Pukei', 'Kuli-Ya-Ku', 'Jyuratodus', 'Tobi-Kadachi', 'Bazelgeuse']

MONSTER_TYPES = ['WYVERN', 'DRAGON', 'BEAST', 'LEVIATHAN', 'TEMNOCERANS']

AILMENT = ['POISON', 'PARALYSIS', 'SLEEP', 'STUN', 'BLAST', 'EXHAUST',
    'FIREBLIGHT', 'WATERBLIGHT', 'THUNDERBLIGHT', 'ICEBLIGHT']


def create_monsters_from_file(path):
    print('Read_and_parse_File | started | path={path}')

    name = ''
    type = ''
    count = 0
    a_type = ''
    a_buildup = ''
    a_decay = ''
    a_damage = ''
    a_duration = ''
    parts = []
    ailments = []
    monsters = []

    with open(path, 'r') as f:
        lines = f.readlines()

    for l in lines:
        if l != '\n':
            _l = l.split()
            flag = _l[0]
            _l.pop(0)
            line = ' '.join(_l)
        if flag == 'n':
            name = line
        elif flag == 't':
            type = line
        elif flag == 'p':
            splitted = line.split(' ')
            if len(splitted) == 11:
                part = Part(splitted[0], splitted[1], splitted[2], splitted[3], splitted[4], splitted[5], splitted[6], splitted[7], splitted[8], splitted[9], splitted[10])
                parts.append(part)
            elif len(splitted) == 12:
                n = splitted[0] + ' ' + splitted[1]
                part = Part(n, splitted[2], splitted[3], splitted[4], splitted[5], splitted[6], splitted[7], splitted[8], splitted[9], splitted[10], splitted[11])
                parts.append(part)
            elif len(splitted) == 13:
                n = splitted[0] + ' ' + splitted[1] + ' ' + splitted[2]
                part = Part(n, splitted[3], splitted[4], splitted[5], splitted[6], splitted[7], splitted[8], splitted[9], splitted[10], splitted[11], splitted[12])
                parts.append(part)
            else:
                print('Error in part ' + line)
        elif flag == 'a':
            if any(string.upper() in line.upper() for string in AILMENT):
                count = 0
                if a_type != '' and a_buildup != '' and a_decay != '' and a_damage != '' and a_duration != '':
                    ailment = Ailment(a_type, a_buildup, a_decay, a_damage, a_duration)
                    ailments.append(ailment)
                a_type = line.strip()
                a_buildup = ''
                a_decay = ''
                a_damage = ''
                a_duration = ''
            else:
                count = count + 1
                if '→' in line:
                    line.replace('→', '->')
                match count:
                    case 1:
                        a_buildup = line.strip()
                    case 2:
                        a_decay = line.strip()
                    case 3:
                        a_damage = line.strip()
                    case 4:
                        a_duration = line.strip()
        elif flag == 'new':
            monster = Monster(name, type, parts, ailments)
            print(monster.name)
            monsters.append(monster)
            name = ''
            type = ''
            parts = []
            ailments = []

    m = Monsters()
    m.monsters.append(monsters)
    return m


def create_json_db(monsters, path):
    with open(path, 'w') as file:
        file.write(json.dumps(monsters.__dict__, default=custom_encode))


def split_file(file_name, separator, out_folder):
    file = open(file_name, 'r')
    lines = file.readlines()

    count = 0
    for line in lines:
        name = out_folder + str(count) + '.txt'
        f = open(name, 'a')

        if line != separator:
            f.write(line)
        else:
            f.close()
            count = count + 1


def prepare_file(file_name, out_file_name):
    file = open(file_name, 'r')
    lines = file.readlines()
    new_file = open(out_file_name, 'w')

    for line in lines:
        if any(string.upper() in line.upper() for string in MONSTER_NAMES):
            new_file.write('n ' + line)
        elif any(string.upper() in line.upper() for string in MONSTER_TYPES):
            new_file.write('t ' + line)
        elif any(string.upper() in line.upper() for string in PARTS):
            new_file.write('p ' + line)
        elif line == '\n':
            new_file.write('new\n')
        else:
            new_file.write('a ' + line)

