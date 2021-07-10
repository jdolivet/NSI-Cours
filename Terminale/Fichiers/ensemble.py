def cree():
    return {'taille' : 0, 'paquets' : [[] for _ in range(32)]}

def contient(ens, val):
    p = val % len(ens['paquets'])
    return val in ens['paquets'][p]

def ajoute(ens, val):
    if contient(ens, val):
        return
    ens['taille'] += 1
    if ens['taille'] > len(ens['paquets']):
        _etend(ens)
    _ajoute_aux(ens['paquets'], val)
    
def _ajoute_aux(tab, val):
    p = val % len(tab)
    tab[p].append(val)
    
def _etend(ens):
    tmp = [[] for _ in range(2 * len(ens['paquets']))]
    for elt in enumere(ens):
        _ajoute_aux(tmp, elt)
    ens['paquets'] = tmp
    
def enumere(ens):
    tab = []
    for paquet in ens['paquets']:
        tab.extend(paquet)
    return tab