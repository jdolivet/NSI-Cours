def cree():
    return [0] * 6

def contient(ens, val):
    paquet = val // 64
    bit = val % 64
    return ens[paquet] & (1 << bit) != 0

def ajoute(ens, val):
    paquet = val // 64
    bit = val % 64
    ens[paquet] = ens[paquet] | (1 << bit)