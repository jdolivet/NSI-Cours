# ### Crible d’Eratosthène
# 
# Implémenter le crible d’Eratosthène en suivant les indications du fichier `eratosthene.py`.

# Définir une variable `n` à 100.
#  Puis créer un tableau `premier` de taille _n+1_ dont les 2 premiers éléments sont `False` et les suivants `True`.
# Mettre à jour ce tableau de sorte que pour tout $i\leq n$, `premier[i]` vaille `True` ssi `i` est premier.

# A compléter

# Test:
print(len(premier)==101 and premier[0]==False and premier[1]==False and premier[2]==True and premier[100]==True)

# Implémenter une version naïve du crible:
#  pour chaque entier `x` plus grand que 2, on marque à `False` tous les multiples de `x`.
#  Le code mettra directement à jour le tableau `premier` (inutile de l'encapsuler dans une fonction).

# A compléter

# Test:
print(premier[2]==True and premier[3]==True and premier[4]==False and premier[15]==False and premier[25]==False and premier[30]==False and premier[97]==True and premier[99]==False)

# Implémenter une version moins naïve du crible, en exploitant l'idée suivante.
#  Soit `x` un entier. On suppose que pour chaque entier `x1<x`, les multiples de `x1` ont été marqués.
#  Alors les seuls multiples de `x` qui restent à marquer sont de la forme `x*y` où `x<=y`.

premier = [False, False]
premier = premier + [True]*(n-1)

# A compléter

# Test:
print(premier[2]==True and premier[3]==True and premier[4]==False and premier[15]==False and premier[25]==False and premier[30]==False and premier[97]==True and premier[99]==False)

# En déduire une ligne de code renvoyant les nombres premiers inférieurs à n en parcourant `premier`.
