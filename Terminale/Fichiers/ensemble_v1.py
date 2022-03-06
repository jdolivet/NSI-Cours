def cree():
    """crée et renvoie un ensemble de dates vide"""
    return [[] for _ in range(23)]

def contient(ens, val) -> bool:
    """renvoie True si, et seulement si, l'ensemble ens contient la date val"""
    return val in ens[val % 23]

def ajoute(ens, val) -> None:
    """ajoute la date val à l'ensemble ens"""
    ens[val % 23].append(val)
    
def enumere(ens) -> list:
    """Renvoie un tableau contenant les éléments de l'ensemble ens."""
    tab = []
    for paquet in ens:
        tab.extend(paquet)
    return tab