def cree():
    """crée et renvoie un ensemble de dates vide"""
    return [0] * 6

def contient(ens, val) -> bool:
    """renvoie True si, et seulement si, l'ensemble ens contient la date val"""
    if val < 1 or val > 366:
        return False
    paquet = val // 64
    bit = val % 64
    return ens[paquet] & (1 << bit) != 0

def ajoute(ens, val) -> None:
    """ajoute la date val à l'ensemble ens"""
    if val < 1 or val > 366
        raise ValueError("date " + str(val) + " invalide")
    paquet = val // 64
    bit = val % 64
    ens[paquet] = ens[paquet] | (1 << bit)