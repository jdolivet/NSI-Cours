# Utilisation du tri Timsort
# Sa présentation par l'auteur :
# https://github.com/python/cpython/blob/main/Objects/listsort.txt
# Implémentation de la classe list (en C) :
# https://github.com/python/cpython/blob/main/Objects/listobject.c

def tri(tab: list) -> None:
    """Procédure qui trie le tableau tab dans l'ordre croissant"""
    tab.sort()