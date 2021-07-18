def cree():
    """crée et renvoie un ensemble de dates vide"""
    return [0] * 6

def contient(ens, val):
    """renvoie True si, et seulement si, l'ensemble ens contient la date val"""
    paquet = val // 64
    bit = val % 64
    return ens[paquet] & (1 << bit) != 0

def ajoute(ens, val):
    """ajoute la date val à l'ensemble ens"""
    paquet = val // 64
    bit = val % 64
    ens[paquet] = ens[paquet] | (1 << bit)