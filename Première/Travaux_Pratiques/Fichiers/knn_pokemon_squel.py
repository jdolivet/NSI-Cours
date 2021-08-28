from pokemon import *

def nearest_neighbors(pokemon, train_data, k,
                      mini_maxi_values,
                      distance = pokemon_manhattan_distance):
    """
    :param pokemon: (Pokemon) the pokemon to be classified
    :param train_data: (list of Pokemon) the train dataset
    :param k: (int) number of neighbors
    :param mini_maxi_values: (dict) dictionnary that contains for every numeric attribute the couple of minimum and maximum values
    :param distance: (function) distance function used
    :return: (list of Pokemon) list of k nearest pokemon

    :Exemple:

    >>> l = read_pokemon_csv()
    >>> train, test = split_pokemons(l)
    >>> m_m_values = min_max_values(train)
    >>> len(nearest_neighbors(test[0], train, 4, m_m_values))
    4
    """
    pass

def knn(pokemon, train_data, k,
        mini_maxi_values,
        distance = pokemon_manhattan_distance,
        prop = 'is_legendary'):
    """
    :param pokemon: (Pokemon) the pokemon to be classified
    :param train_data: (list of Pokemon) the train dataset
    :param k: (int) number of neighbors
    :param mini_maxi_values: (dict) dictionnary that contains for every numeric attribute the couple of minimum and maximum values
    :param distance: (function) distance function used
    :param prop: (str) name of the class to be predicted
    :return: (any) the class mostly present in pokemon neighborhood

    :Exemple:

    >>> l = read_pokemon_csv()
    >>> train, test = split_pokemons(l)
    >>> m_m_values = min_max_values(train)
    >>> knn(test[0], train, 3, m_m_values) in { True, False }
    True
    """
    pass

def knn_data(test_data, train_data, k,
             distance = pokemon_manhattan_distance,
             prop = 'is_legendary'):
    """
    :param pokemon: (Pokemon) the pokemon to be classified
    :param train_data: (list of Pokemon) the train dataset
    :param k: (int) number of neighbors
    :param distance: (function) distance function used
    :return: (float) proportion of well classified data 
    
    :Exemple:

    >>> l = read_pokemon_csv()
    >>> train, test = split_pokemons(l)
    >>> knn_data(test, train, 4) > 0.6
    True
    """
    res = 0
    mini_maxi_values = min_max_values(train_data)
    for p in test_data:
        cl = knn(p, train_data, k, mini_maxi_values, distance, prop)
        if cl == p._asdict()[prop]:
            res += 1
    return res / len(test_data)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
