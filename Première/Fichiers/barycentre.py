# ### Le barycentre
# 
# Compléter dans le fichier `barycentre.py` une fonction qui prend en entrée un ensemble de points,
#  chaque point étant représenté par un tuple à 2 coordonnées, et renvoie leur barycentre.


# L'énoncé propose de se limiter aux tuples à 2 coordonnées, donc des points de dimension d=2.
# Nous suggérons d'essayer de résoudre le problème pour des points de dimension d quelconque.
# On commencera dans la fonction par déduire d de la longueur du premier point.
def f(mat):
    """ Entrée: mat est une matrice contenant n points de dimension d (pour un certain n et d). 
    Cette matrice est représentée 
    - soit par un tableau de tuples (d-uplets) 
    - soit par un tableau de tableaux (de longueur d).
    Renvoie un tableau représentant le barycentre.
    """
    # A compléter

# Test:
print(f([(1,2),(2,2),(0,0),(2,2)])==[1.25, 1.5])
print(f([[1,2,4],[2,2,6],[0,0,0],[2,2,6]])==[1.25, 1.5, 4.0])
