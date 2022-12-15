
# ### Sudoku
# 
# Un jeu de Sudoku est une matrice de 9 x 9 chiffres où chaque ligne, chaque colonne
#  (et aussi les 9 blocs 3 x 3 couvrant la grille) doivent comporter chacun des 9 chiffres.
#  Compléter le code du fichier `sudoku.py` pour vérifier une solution de sudoku.
#  Notre solution se contentera de renvoyer une réponse booléenne;
#   on ne cherchera pas à localiser les violations des propriétés.

# Une grille complétée de Sudoku de dimensions 9x9 est une solution valide si
#  elle satisfait les 4 propriétés suivantes:
# 
# - P0: la grille ne contient que des entiers entre 1 et 9.
# - P1: chaque ligne de la grille contient les 9 chiffres
# - P2: chaque colonne de la grille contient les 9 chiffres
# - P3: chacun des 9 carrés 3x3 qui décomposent la grille contient les 9 chiffres 


# a) Compléter le code de la fonction `verifie_tableau` qui prend en entrée un tableau de 9 valeurs
# et vérifie que chacun des chiffres apparaît une et unique fois.

def verifie_tableau(t):
    """
    Entrée: un tableau t de taille 9
    Renvoie: True ssi chaque chiffre entre 1 et 9 apparaît une et unique fois dans t.
    
    Pour cela, la fonction combine un tableau de booléens et un compteur. 
    On utilisera isinstance(z,int) pour vérifier qu'une valeur z est un entier.
    """
    v=[False]*10 # *9 suffirait, mais *10 est plus pratique
    n=0
    for z in t :
        if ... :# A compléter: 3 conditions
            # A compléter: ici, mettre à jour v
            n += 1
    return n==9

# Test:
print(verifie_tableau([3,1,4,8,2,5,9,6,7])==True)
print(verifie_tableau([3,1,4,8,6,5,9,6,7])==False)
print(verifie_tableau([3.2,1,4,8,2,5,9,6,7])==False)

# Nous allons désormais représenter une grille de sudoku par une matrice de 9x9 valeurs
#  (nous n'en vérifierons pas les dimensions supposées correctes). 
# 
# b) En vous aidant de la fonction ci-dessus,
#  compléter le code de la fonction `verifie_horizontal` qui prend
#  en entrée une matrice de 9x9 valeurs et vérifie la propriété P1 (et P0).

def verifie_horizontal(g):
    """
    Entrée: une grille g de dimension 9x9 représentée par un tableau de tableaux.
    Renvoie: True ssi la grille satisfait P0 et P1.
    """
    # A compléter

# Test:
print(verifie_horizontal([[3,1,4,8,2,5,9,6,7] for i in range(9)])==True)
print(verifie_horizontal([[3,1,4,8,2,5,9,6,7] for i in range(8)]+[[3,1,4,8,6,5,9,6,7]])==False)


# c) Ecrire de même une fonction `verifie_vertical` qui prend
#  en entrée une matrice de 9x9 valeurs et vérifie la propriété P2 (et P0).

def verifie_vertical(g):
    """
    Entrée: une grille g de dimension 9x9 représentée par un tableau de tableaux.
    Renvoie: True ssi la grille satisfait P0 et P2.
    """
    # A compléter

# Test:
print(verifie_vertical([[3,1,4,8,2,5,9,6,7] for i in range(9)])==False)
print(verifie_vertical([[3,1,4,8,2,5,9,6,7] for i in range(8)]+[[3,1,4,8,6,5,9,6,7]])==False)

# d) Ecrire un code qui afficher la paire `(i//3,i%3)` pour chaque `i` entre 0 et 9.
#  Comparer avec l'ordre dans lequel sont parcourues les cases d'une sous-grille 3x3 sur la Figure ci-dessus.
# Puis compléter le code  de la fonction suivante pour qu'elle vérifie la propriété P3 (et P0).
# On peut observer qu'il y a 9 carrés 3x3 à évaluer, et que ces 9 carrés sont eux-même agencés
#  selon un carré 3x3, donc on peut s'inspirer du code affichant les paires pour énumérer les petits carrés si on écrit
# les indices appartenant à un petit carré sous la forme suivante:
# ("numéro de la ligne à l'intérieur du petit carré"+"un décalage dépendant de la position du petit carré à l'intérieur du grand",
#  et pareil avec les colonnes). 

# Le code affichant (i//3,i%3)

def verifie_carre(g):
    """
    Entrée: une grille g de dimension 9x9 représentée par un tableau de tableaux.
    Renvoie: True ssi la grille satisfait P0 et P3.
    """
    for i in range(9):
        if not verifie_tableau([... for j in range(9)]) # A compléter:
            return False
    return True

# Test:
print(verifie_carre([[3,6,7,5,1,2,8,4,9]
,[9,8,1,7,6,4,2,3,5]
,[5,2,4,8,3,9,7,6,1]
,[1,9,6,4,8,5,3,7,2]
,[2,4,8,1,7,3,9,5,6]
,[7,5,3,2,9,6,1,8,4]
,[4,1,5,3,2,7,6,9,8]
,[8,3,9,6,5,1,4,2,7]
,[6,7,2,9,4,8,5,1,3]])==True)
print(verifie_carre([[3,1,4,8,2,5,9,6,7] for i in range(9)])==False)
print(verifie_carre([[3,1,4,8,2,5,9,6,7] for i in range(8)]+[[3,1,4,8,6,5,9,6,7]])==False)

# !!e) Déduire des fonctions précédente une fonction qui vérifie la validité d'une solution

def verifie_solution(g):
    """ 
    Entrée: une grille g de dimension 9x9 représentée par un tableau de tableaux.
    Renvoie: True ssi g est une solution valide (satisfaisant P0,p1,P2,et P3).
    """
    return # A compléter


# Test:
print(verifie_solution([[3,6,7,5,1,2,8,4,9]
,[9,8,1,7,6,4,2,3,5]
,[5,2,4,8,3,9,7,6,1]
,[1,9,6,4,8,5,3,7,2]
,[2,4,8,1,7,3,9,5,6]
,[7,5,3,2,9,6,1,8,4]
,[4,1,5,3,2,7,6,9,8]
,[8,3,9,6,5,1,4,2,7]
,[6,7,2,9,4,8,5,1,3]])==True)
print(verifie_solution([[3,1,4,8,2,5,9,6,7] for i in range(9)])==False)
print(verifie_solution([[3,1,4,8,2,5,9,6,7] for i in range(8)]+[[3,1,4,8,6,5,9,6,7]])==False)
