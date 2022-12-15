# ### croisements dans le plan
# 
# On donne dans un tableau la position, l’orientation (Nord, Sud, Est ou Ouest)
#  et la vitesse de voitures sur un plan routier en forme de grille (comme Manhattan).
#  Deux voitures se croisent à une intersection si elles y arrivent exactement au même moment.
#  Les voitures, considérées comme de simples points, peuvent se doubler sans ralentir.
#  Compléter le code du fichier `croisements.py` pour identifier les voitures qui se croisent.


# On représente un ensemble de n voitures à l'instant 0 par 3 tableaux d'entiers. 
# 
# 
# 
#  - tx[i] donne la position de la voiture _i_ sur l'axe x (un nombre de mètres entier),
#  - ty[i] la position sur l'axe y (un nombre de mètres entier)
#  - tv[i] la vitesse (en rm/s).
#  - to[i] l'orientation (parmi 'Nord', 'Sud', 'Est', et 'Ouest').
# 
# 
# Pour tester les fonctions on pourra utiliser les jeux de données ci-dessous.

# Test
tx = [0,0]
ty = [0,4]
tv = [3,2]
to = ['Nord','Nord']
#croisement car 0 rattrape 1

# Test
tx = [0,0]
ty = [0,4]
tv = [3,2]
to = ['Nord','Sud']
#croisement frontal

# Test
tx = [4,0]
ty = [0,4]
tv = [1,1]
to = ['Nord','Est']
#croisement orthogonal

# Test
tx = [4,1,6]
ty = [1,4,5]
tv = [1,2,4]
to = ['Nord','Est','Sud']
# 3 voitures, pas de croisements

# On considère que deux voitures se croisent si les deux se retrouvent sur le même point à un même moment.
# 
# Pour que le problème ne soit pas trop compliqué, on fait les suppositions suivantes :
# - à l'instant de départ aucune voiture n'est en croisement;
#  deux voitures ne peuvent pas être simultanément à la même position sur x et y à l'instant 0
# - les voitures se résument à un point 
# - les voitures ont une vitesse constante
# - les vitesses et les positions de départ sont des tableaux d'entiers.
# 
# a) Commencer par implémenter fonction `vitesses` spécifiée ci-dessous.
# 
# `vitesse(i)` Renvoie une paire `(vx, vy)`, où 
# - `vx` est la vitesse horizontale de la voiture `i`
# (positive si la voiture va vers l'Est, négative sinon), 
# - `vy` est la vitesse verticale de la voiture `i` (positive si la voiture va vers le nord, négative sinon) 

def vitesses(i):
    """
    Renvoie une paire (vx, vy), où 
    - vx est la vitesse horizontale de la voiture i 
    (positive si la voiture va vers l'Est, négative sinon), 
    - vy est la vitesse verticale de la voiture i (positive si la voiture va vers le nord, négative sinon) 
    """
    v = None
    # A compléter
    return v


# Test
tx = [0,0]
ty = [0,4]
tv = [3,2]
to = ['Nord','Nord']

print(vitesses(1)==(0,2))

# Test
tx = [4,1,6]
ty = [1,4,5]
tv = [1,2,4]
to = ['Nord','Est','Sud']

print(vitesses(2)==(0,-4))

# Pour calculer les croisements, nous allons d'abord mettre le problème en équations.
# 
# La position de i à l'instant u est donnée par les équations:
# 
# `x(i,u) = tx[i] + u*vitesses(i)[0]`
# 
# `y(i,u) = ty[i] + u*vitesses(i)[1]`
# 
# On a un croisement s'il existe `u>0` tel que 
# 
# `x(i,u) = x(j,u)`
# 
# et 
# 
# `y(i,u) = y(j,u)`
# 
# Vous pouvez essayer d'en déduire par vous-même les conditions à vérifier pour déterminer s'il y a un croisement. 
# Mais si vous préférez vous contenter de coder les conditions, ces conditions vous sont données ci-dessous :
# 
# `(tx[i]-tx[j])*(vitesses(j)[1]-vitesses(i)[1]) = (ty[i]-ty[j])*(vitesses(j)[0]-vitesses(i)[0])`
# 
# et 
# 
# `(tx[i]-tx[j])*(vitesses(j)[0]-vitesses(i)[0]) + (ty[i]-ty[j])*(vitesses(j)[1]-vitesses(i)[1])>0`

# b) Ecrire une fonction `croisement(i,j)` qui renvoie `True` ssi les voitures `i` et `j` se croisent.
# Est-ce que la supposition que les positions initiales et les vitesses sont entières
#  suffit à garantir qu'il n'y aura pas d'erreur d'arithmétique flottante lors des calculs?
#  Expliquer pourquoi ce serait ou ne serait pas le cas, et le cas échéant adapter le code si nécessaire.

def croisement(i,j):
    """ Renvoie True ssi les voitures i et j se croisent """
    # A compléter

# Test
tx = [0,0]
ty = [0,4]
tv = [3,2]
to = ['Nord','Nord']
#collision car 0 rattrape 1

print(croisement(0,1)==True)

# c) Ecrire un code renvoyant dans un tableau `liste_croisements` toutes les paires de voitures (distinctes)
#  qui se croisent Chaque paire, considérée comme non-ordonnée, devra apparaître une unique fois,
#  donc on ne renverra pas à la fois la paire (1,2) et la paire (2,1), par exemple.
#  Vous pouvez utiliser `append` si vous le souhaitez.


# Test
tx = [0,0]
ty = [0,4]
tv = [3,2]
to = ['Nord','Nord']
#collision car 0 rattrape 1

# Compléter ici avec votre code.

print(liste_croisements == [(0, 1)] or liste_croisements == [(1, 0)])


