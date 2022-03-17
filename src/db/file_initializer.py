import string


PARTS = ['HEAD', 'NECK', 'TAIL', 'TORSO', 'WING', 'LEG', 'BACK', 'ABDOMEN', 'HORN', 
    'FORELEG', 'CUTWING', 'THORNS', 'MANE', 'HIP', 'BODY', 'HALF', 'REAR', 'FIN', 'CLUMP', 
    'CLAW', 'WINGARM', 'CHEST', 'ARMBLADE', 'TAILBLADE', 'MUDBULB', 'SNOUT', 'TONGUE', 'BOULDER']

MONSTER_NAMES = ['Rathian', 'Rathalos', 'Khezu', 'Basarios', 'Diablos', 'Rajang', 'Kushala', 
    'Chameleos', 'Teostra', 'Tigrex', 'Nargacuga', 'Barioth', 'Barroth', 'Ludroth', 'Baggi', 
    'Zinogre', 'Wroggi', 'Arzuros', 'Lagombi', 'Volvidon', 'Mizutsune', 'Valstrax', 'Magnamalo', 
    'Bishaten', 'Aknosom', 'Tetranadon', 'Somnacanth', 'Rakna-Kadaki', 'Almudron', 'Ibushi', 
    'Goss', 'Izuchi', 'Narwa', 'Anjanath', 'Pukei-Pukei', 'Kuli-Ya-Ku', 'Jyuratodus', 'Tobi-Kadachi', 'Bazelgeuse']

MONSTER_TYPES = ['WYVERN', 'DRAGON', 'BEAST', 'LEVIATHAN', 'TEMNOCERANS']

def prepare_file(file_name):
    file = open(file_name, 'r')
    lines = file.readlines()
    new_file = open('new_f.txt', 'w')

    for line in lines:
        if any(string.upper() in line.upper() for string in MONSTER_NAMES):
            new_file.write('n ' + line)
        elif any(string.upper() in line.upper() for string in MONSTER_TYPES):
            new_file.write('t ' + line)
        elif any(string.upper() in line.upper() for string in PARTS):
            new_file.write('p ' + line)
        elif line == '\n':
            new_file.write('\n')
        else:
            new_file.write('a ' + line)
            

if __name__ == "__main__":
    prepare_file('prova.txt')