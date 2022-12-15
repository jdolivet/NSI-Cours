# ### Vote majoritaire Boyer-Moore
# 
# L’algorithme de vote majoritaire Boyer-Moore itère une seule fois sur un tableau `t` de valeurs,
#  en stockant à tout moment uniquement une valeur de `t` et un compteur,
#  et renvoie la valeur majoritaire dans `t` s’il y en a une, et une valeur arbitraire de `t` sinon.
# 
# En vous aidant du code dans `majorite-bm.py` :
# 
# a) Implémenter cet algorithme.


def majorite_boyer_moore(t):
    """ Algorithme de Vote majoritaire de boyer moore
    Si t contient une valeur v au moins len(t)/2 fois, alors renvoie v
    Sinon renvoie une valeur quelconque parmi celles dans t
    Complexite : ...
    Espace utilise en memoire : juste une valeur et un entier.
    
    Description de l'algorithme:
    On parcourt les éléments de t l'un après l'autre.
    Tant que la "valeur courante" a un compteur supérieur à 0: 
    - chaque fois qu'on rencontre cette valeur on incrémente le compteur de 1
    - chaque fois qu'on rencontre une autre valeur on décrémente le compteur de 1
    Lorsque le compteur tombe à 0, la prochaine valeur lue devient la valeur courante.
    """
    val = t[0] # la valeur courante. 
    nb = 1 # le compteur
    # A compléter : il reste à traiter la suite du tableau: t[1]...
    

#Test:
print(majorite_boyer_moore(['a','b','b','c','b'])=='b') # 'b' qui est bien majoritaire.
print(majorite_boyer_moore(['a','b','a','c','a','d','a','d'])=='a') # 'a' qui est bien majoritaire.
print(majorite_boyer_moore(['a','b','b','c','d'])) # 'd', il n'y a en fait pas d'element majoritaire.

# La complexité est linéaire.
# En fait c'est même un exemple célèbre d'algorithme de "streaming",
#  un algorithme capable de traiter une séquence de valeurs données au fur à mesure sans les stocker,
#  et en utilisant une quantité de mémoire limitée. 


# b) Écrire un code qui vérifie si le nombre renvoyé est bien majoritaire.


def verifie(t,v):
    """ renvoie True ssi v est majoritaire dans t
    Complexite: lineaire
    """
    # A compléter

# Test
print(verifie(['a','b','b','c','b'],'b'))
print(verifie(['a','b','b','c','d'],'b')==False)
