def cree():
    """Crée et renvoie un ensemble de dates vide"""
    return [0] * 6

def contient(ens, val) -> bool:
    """Renvoie True si, et seulement si, l'ensemble ens contient la date val"""
    if val < 1 or val > 366:
        return False
    paquet = val // 64
    bit = val % 64
    return ens[paquet] & (1 << bit) != 0

# Tests
s0 = cree()
assert contient(s0, 45) == False

def ajoute(ens, val) -> None:
    """Ajoute l'élément val à l'ensemble ens si i <= x <= 366 
    et lève une exception ValueError sinon"""
    if val < 1 or val > 366:
        raise ValueError(f"date {val} invalide")
    paquet = val // 64
    bit = val % 64
    ens[paquet] = ens[paquet] | (1 << bit)
    
# Tests
ajoute(s0, 45)
assert contient(s0, 45) == True
ajoute(s0, 279)
assert contient(s0, 279) == True
try:
    ajoute(s0, 389)
except ValueError:
    assert contient(s0, 389) == False