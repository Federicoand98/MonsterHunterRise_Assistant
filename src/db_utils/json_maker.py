import json
import os
import numpy as np
from utils import create_json_db, create_monsters_from_file, prepare_file
import db_data as data

if __name__ == "__main__":
    path = '/Users/federyeeco/Sviluppo/Git/MonsterHunterRise_Assistant/src/db/input-db.txt'
    out_path = '/Users/federyeeco/Sviluppo/Git/MonsterHunterRise_Assistant/src/db/parsed-db.txt'

    prepare_file(path, out_path)
    monsters = create_monsters_from_file('/Users/federyeeco/Sviluppo/Git/MonsterHunterRise_Assistant/src/db/parsed-db.txt')
    create_json_db(monsters, '/Users/federyeeco/Sviluppo/Git/MonsterHunterRise_Assistant/src/db/monsters.json')