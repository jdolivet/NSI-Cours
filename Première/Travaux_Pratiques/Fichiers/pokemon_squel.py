from collections import namedtuple
from math import sqrt, ceil
from random import shuffle

# Pokemons properties names

POKE_PROP_NAMES = [ 'name', 'attack', 'base_egg_steps',
                    'base_hapiness', 'capture_rate', 'classification', 'defense',
                    'experience_grow', 'height_m', 'hp', 
                    'pokedex_number', 'sp_attack', 'sp_defense', 'speed',
                    'type1', 'type2', 'weight_kg', 'generation',
                    'is_legendary' ]

# helper function
def bool_from_str(s):
    """
    :param s: (String) a string
    :return: (bool) True if arg == 'True' or '1', False otherwise
    :exemples:

    >>> bool_from_str('True')
    True
    >>> bool_from_str('False')
    False
    >>> bool_from_str('Toto')
    False
    >>> bool_from_str('1')
    True
    """
    return True if (s  == 'True' or s == '1')  else False

# Pokemon properties types
POKE_PROP_TYPES = [str, int, int,
                   int, float, str, int,
                   int, float, int, 
                   int, int, int, int,
                   str, str, float, int,
                   bool_from_str]

# list of properties used to compute distance
POKE_PROP_USED_FOR_DISTANCE = [ 'base_egg_steps', 'capture_rate', 'experience_grow', 'generation' ]

TRAIN_PROPORTION = 0.65

POKE_DATA_FNAME_SMALL = 'pokemon_small.csv'

Pokemon = namedtuple('Pokemon', POKE_PROP_NAMES)

def read_pokemon_csv(filename = POKE_DATA_FNAME_SMALL):
    """
    :param filename: (String) filename of csv file
    :return: (list of Pokemon) list of pokemon read

    :Exemples:

    >>> l = read_pokemon_csv()
    >>> len(l)
    20
    >>> all(isinstance(p, Pokemon) for p in l)
    True
    """
    res = []
    with open(filename) as f:
        f.readline()
        l = f.readline()
        while l != '':
            args = l.replace('"', '').strip().split(',')
            try:
                typed_args = []
                for i in range(len(args)):
                    typed_args.append(POKE_PROP_TYPES[i](args[i]))
                res.append(Pokemon(*typed_args))
            except ValueError:
                # missing value : continue to next line
                pass
            l = f.readline()
    return res

def get_min_max_values_for_attr(l_pokemon, attr):
    """
    :param l_pokemon: (list of Pokemon) a list of pokemon
    :param attr: (str) the name of an attribute
    :return: (couple) couple of min and max value for numeric attribute `attr`
    :UC: attr is a numeric attribute
    """
    assert attr in POKE_PROP_NAMES, "name {} is not an attibute name".format(attr)
    assert POKE_PROP_TYPES[POKE_PROP_NAMES.index(attr)] in {int, float}, "name {} is not a numeric attribute".format(attr)
    mini, maxi = float('inf'), -float('inf')
    for poke in l_pokemon:
        d_poke = poke._asdict()
        if d_poke[attr] < mini:
            mini = d_poke[attr]
        if d_poke[attr] > maxi:
            maxi = d_poke[attr]
    return (mini, maxi)

def min_max_values(l_pokemon):
    """
    :param l_pokemon: (list of Pokemon) a list of pokemon
    :return: (dict) a dictionnary that contains minimum and maximum values for each numeric attributes

    :Exemples:
    
    >>> lp = read_pokemon_csv()
    >>> min_max_values(lp)
    {'attack': (10, 155), 'base_egg_steps': (1280, 20480), 'base_hapiness': (35, 70), 'capture_rate': (3.0, 255.0), 'defense': (48, 125), 'experience_grow': (1000000, 1250000), 'height_m': (0.3, 6.5), 'hp': (20, 160), 'pokedex_number': (126, 145), 'sp_attack': (15, 125), 'sp_defense': (20, 130), 'speed': (30, 150), 'weight_kg': (4.0, 460.0), 'generation': (1, 1)}
    """
    res = {}
    for attr in POKE_PROP_NAMES:
        if POKE_PROP_TYPES[POKE_PROP_NAMES.index(attr)] in {int, float}:
            res[attr] = get_min_max_values_for_attr(l_pokemon, attr)
    return res

def split_pokemons(pokemons, proportion = TRAIN_PROPORTION):
    """
    :param pokemons: (list of Pokemon) list of pokemon
    :param proportion: (float) proportion of pokemons used in train data
    :return: (tuple) couple of list of train data and test data

    :Exemples:
    
    >>> l = read_pokemon_csv()
    >>> train, test = split_pokemons(l)
    >>> len(train) + len(test) == len(l)
    True
    >>> abs(len(train)/len(l) - TRAIN_PROPORTION) < 0.1
    True
    """
    shuffle(pokemons)
    N = ceil(len(pokemons) * TRAIN_PROPORTION)
    return pokemons[:N], pokemons[N:]

def pokemon_euclidian_distance(poke1, poke2, min_max_val):
    """
    :param poke1: (Pokemon) a pokemon
    :param poke2: (Pokemon) another pokemon
    :param min_max_val: (dict) give for every numeric attribute min and max values
    :return: (float) the distance between poke1 and poke2

    :Exemples:

    >>> lp = read_pokemon_csv()
    >>> d1 = pokemon_euclidian_distance(lp[0], lp[1], min_max_values(lp))
    >>> d1p = pokemon_euclidian_distance(lp[1], lp[0], min_max_values(lp))
    >>> d2 = pokemon_euclidian_distance(lp[1], lp[2], min_max_values(lp))
    >>> d3 = pokemon_euclidian_distance(lp[0], lp[2], min_max_values(lp))
    >>> d1 == d1p
    True
    >>> d3 <= d1 + d2 
    True
    """
    pass

def pokemon_manhattan_distance(poke1, poke2, min_max_val):
    """
    :param poke1: (Pokemon) a pokemon
    :param poke2: (Pokemon) another pokemon
    :param min_max_val: (dict) give for every numeric attribute min and max values
    :return: (float) the distance between poke1 and poke2

    :Exemples:

    >>> lp = read_pokemon_csv()
    >>> d1 = pokemon_manhattan_distance(lp[0], lp[1], min_max_values(lp))
    >>> d1p = pokemon_manhattan_distance(lp[1], lp[0], min_max_values(lp))
    >>> d2 = pokemon_manhattan_distance(lp[1], lp[2], min_max_values(lp))
    >>> d3 = pokemon_manhattan_distance(lp[0], lp[2], min_max_values(lp))
    >>> d1 == d1p
    True
    >>> d3 <= d1 + d2
    True
    """
    res = 0
    p1 = poke1._asdict()
    p2 = poke2._asdict()
    for p in POKE_PROP_USED_FOR_DISTANCE:
        i = POKE_PROP_NAMES.index(p)
        if POKE_PROP_TYPES[i] in {int, float}:
            mini, maxi = min_max_val[p]
            e = maxi-mini if mini != maxi else 1
            res += abs(p1[p]-p2[p])/e
        elif POKE_PROP_TYPES[i] == str:
            res += 0 if p1[p] == p2[p] else 1
    return res

if __name__ == '__main__':
    import doctest
    doctest.testmod()
