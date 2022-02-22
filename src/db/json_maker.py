from copy import deepcopy
import json

class Monsters(object):
    def __init__(self):
        self.monsters = []

class Monster(object):
    def __init__(self, name, type, parts_list, ailments_list):
        self.name = name
        self.type = type
        self.parts_list = parts_list
        self.ailments_list = ailments_list

class Part(object):
    def __init__(self, type, state, hit_slash, hit_strike, hit_shell, fire, water, ice, thunder, dragon, stun):
        self.type = type
        self.state = state
        self.hit_slash = hit_slash
        self.hit_strike = hit_strike
        self.hit_shell = hit_shell
        self.fire = fire
        self.water = water
        self.ice = ice
        self.thunder = thunder
        self.dragon = dragon
        self.stun = stun

class Ailment(object):
    def __init__(self, type, buildup, decay, damage, duration):
        self.type = type
        self.buildup = buildup
        self.decay = decay
        self.damage = damage
        self.duration = duration

def custom_encode(obj):
    if isinstance(obj, Monster):
        return obj.__dict__
    if isinstance(obj, Part):
        return obj.__dict__
    if isinstance(obj, Ailment):
        return obj.__dict__
    return obj

if __name__ == "__main__":
    parts_array = []
    ailments_array = []
    voti_arr = []
    lista_mostri = Monsters()

    flag = raw_input('Nuovo mostro? [s/n]')

    while flag == 's':
        name = raw_input('Nome Mostro: ')
        tipo = raw_input('Tipo Mostro: ')

        for i in range(7):
            p = raw_input('Part: ')
            p_splitted = p.split()

            if len(p_splitted) == 11:
                part = Part(p_splitted[0], p_splitted[1], p_splitted[2], p_splitted[3], p_splitted[4], p_splitted[5], p_splitted[6], p_splitted[7], p_splitted[8], p_splitted[9], p_splitted[10])
                parts_array.append(part)

        for i in range(10):
            a = raw_input('Ailment: ')
            a_splitted = a.split()

            if len(a_splitted) == 5:
                ailment = Ailment(a_splitted[0], a_splitted[1], a_splitted[2], a_splitted[3], a_splitted[4])
                ailments_array.append(ailment)

        monster = Monster(name, tipo, parts_array, ailments_array)
        lista_mostri.monsters.append(monster)
        flag = raw_input('Nuovo mostro? [s/n]')

        with open("f1.json", "w") as file:
            file.write(json.dumps(lista_mostri.__dict__, default=custom_encode))
