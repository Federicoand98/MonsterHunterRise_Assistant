import json
import numpy as np

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

    file = open('f.txt', 'r')
    lines = file.readlines()

    count = 0
    for line in lines:
        if 'M' in line:
            

    """
    m = input('In: ')
    m_array = m.split()
    np_m = np.asarray(m_array)
    matrix = np_m.reshape(7, 11)
    print(matrix)

    flag = input('Nuovo mostro? [s/n]')

    while flag == 's':
        name = input('Nome Mostro: ')
        tipo = input('Tipo Mostro: ')

        p = input('Parts: ')
        p_splitted = p.split()
        p_np_m = np.array(p_splitted)
        matrix = p_np_m.reshape(7, 11)

        for i in range(7):
            row = matrix[i, :]
            part = Part(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
            parts_array.append(part)

        for i in range(10):
            a = input('Ailment: ')
            a_splitted = a.split()

            if len(a_splitted) == 5:
                ailment = Ailment(a_splitted[0], a_splitted[1], a_splitted[2], a_splitted[3], a_splitted[4])
                ailments_array.append(ailment)

        monster = Monster(name, tipo, parts_array, ailments_array)
        lista_mostri.monsters.append(monster)
        flag = input('Nuovo mostro? [s/n]')
    

        with open("f2.json", "w") as file:
            file.write(json.dumps(lista_mostri.__dict__, default=custom_encode))
    """