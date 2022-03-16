def cree():
    """Crée et renvoie un ensemble de dates vide"""
    return [[] for _ in range(23)]

def contient(ens, val) -> bool:
    """Renvoie True si, et seulement si, l'ensemble ens contient la date val"""
    return val in ens[val % 23]

# Tests
s0 = cree()
assert contient(s0, 45) == False


def ajoute(ens, val) -> None:
    """Ajoute l'élément val à l'ensemble ens si i <= x <= 366 
    et lève une exception ValueError sinon"""
    if val < 1 or val > 366:
        raise ValueError(f"date {val} invalide")
    ens[val % 23].append(val)
    
# Tests
ajoute(s0, 45)
assert contient(s0, 45) == True
ajoute(s0, 279)
assert contient(s0, 279) == True
try:
    ajoute(s0, 389)
except ValueError:
    assert contient(s0, 389) == False
    
    
def enumere(ens) -> list:
    """Renvoie un tableau contenant les éléments de l'ensemble ens."""
    tab = []
    for paquet in ens:
        tab.extend(paquet)
    return tab

# Tests
s1 = cree()
assert type(enumere(s1)) is list
assert len(enumere(s1)) == 0

ajoute(s1, 45)
assert len(enumere(s1)) == 1
assert 45 in enumere(s1)

ajoute(s1, 257)
assert len(enumere(s1)) == 2
assert 257 in enumere(s1)

ajoute(s1, 63)
assert len(enumere(s1)) == 3
assert 63 in enumere(s1)