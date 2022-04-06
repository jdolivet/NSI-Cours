def insere(tab: list, i: int, val) -> None:
    """Procédure qui insère val dans tab[0..i[ supposé trié"""
    j = i
    while j > 0 and tab[j - 1] > val:
        tab[j] = tab[j - 1]
        j = j - 1
    tab[j] = val
    
def tri(tab: list) -> None:
    """Procédure qui trie le tableau tab dans l'ordre croissant"""
    for i in range(1, len(tab)):
        # invariant : tab[0..i[ est trié
        tmp = tab[i]
        insere(tab, i, tmp)