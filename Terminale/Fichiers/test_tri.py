def occurrences(tab):
    """renvoie le dictionnaire des occurrences de tab"""
    dico = {}
    for elt in tab:
        if elt in dico:
            dico[elt] += 1
        else:
            dico[elt] = 1
    return dico

def identiques(d1, d2):
    """deux dictionnaires sont identiques"""
    for cle in d1:
        assert cle in d2
        assert d1[cle] == d2[cle]
    for cle in d2:
        assert cle in d1
        assert d2[cle] == d1[cle]

def test(tab):
    """teste la fonction tri sur le tableau t"""
    occ = occurrences(tab)
    tri(tab)
    for i in range(0, len(tab) - 1):
        assert tab[i] <= tab[i + 1]
    identiques(occ, occurrences(tab))