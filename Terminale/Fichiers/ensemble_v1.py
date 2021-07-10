def cree():
    return [[] for _ in range(23)]

def contient(ens, val):
    return val in ens[val % 23]

def ajoute(ens, val):
    ens[val % 23].append(val)
    
def enumere(ens):
    tab = []
    for paquet in ens:
        tab.extend(paquet)
    return tabv