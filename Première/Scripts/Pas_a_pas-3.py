def est_croissant(t):
    """Renvoie True si le tableau est trié par ordre croissent
    False sinon"""
    i = len(t) - 1
    while i >= 0:
        if t[i] <= t[i + 1]:
            return False
        else:
            return False
        i -= 1
        
est_croissant([1, 2, 3, 4])