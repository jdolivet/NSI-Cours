def echange(tab: list, i: int, j: int) -> None:
    """Procédure qui échange les éléments du tableau d'indice i et j."""
    tmp = tab[i]
    tab[i] = tab[j]
    tab[j] = tmp
    
def tri(tab: list) -> None:
    """Procédure qui trie le tableau tab dans l'ordre croissant"""
    for i in range(len(tab)):
        # invariant : tab[0..i[ est trié et <= à tab[i..[
        # on cherche le minimum de tab[i..[
        idx_min = i
        for j in range(i + 1, len(tab)):
            if tab[j] < tab[idx_min]:
                idx_min = j
        echange(tab, i, idx_min)