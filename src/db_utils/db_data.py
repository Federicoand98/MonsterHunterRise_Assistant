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