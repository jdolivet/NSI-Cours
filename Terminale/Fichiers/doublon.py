from dates import cree, contient, ajoute

def contient_doublon(tab : list) -> bool:
    """Le tableau tab contient-il un doublon?"""
    ens = cree()
    for elt in tab:
        if contient(ens, elt):
            return True
        ajoute(ens, elt)
    return False