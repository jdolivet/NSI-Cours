# ### Goniométrie
# 
# On dispose de deux stations radios que l’on supposera placées dans un plan aux coordonnées (0,0) et (0,10).
#  Ces stations cherchent à identifier la position d’un émetteur radio en mouvement.
#  Chaque minute, les stations enregistrent l’angle (en degrés) d’où parvient le signal par rapport à l’axe (Ox).
# 
# On a donc un tableau *t1* pour la station 1, et *t2* pour la station 2. 
# 
# a) Compléter le code du fichier `goniometrie.py` pour calculer à chaque instant la position de l’émetteur.
# 
# > **Note**
# >
# > La goniométrie (mesure des angles) sert depuis l’antiquité pour la navigation et la topographie.
# La radio goniométrie a servi à guider les navires et avions du début XXe jusqu’aux années 1970.
# Elle a depuis été remplacée dans cette application par le GPS, plus précis.

# Exemple de données:
t1 = [0.24497866312686414, 0.46364760900080615, 0.7853981633974483, 1.0303768265243125, 0.7086262721276703]
t2 = [2.976443976175166, 2.819842099193151, 2.7367008673047097, 2.5213431676069717, 2.0344439357957027]

# Code de la solution:
from math import pi, tan
def position(a1,a2):
    """ 
    Entrée: 
    - l'angle a1 entre l'axe Ox et l'émetteur depuis la station 1
    - l'angle a2 entre l'axe Ox et l'émetteur depuis la station 2
    On suppose que 0<a1<180; l'émetteur reste à des coordonnées (x,y) avec y>0.
    Renvoie: la position (x,y) de l'émetteur. 
    """
    # A compléter.

[position(t1[i],t2[i]) for i in range(len(t1))]

# b) On veut écrire un test qui vérifie que la fonction `position` calcule correctement la position.
# On sait que pour un bateau à la position (4,1), les stations indiquent des angles `x1,x2`.
#  Pourquoi le test  `print(position(x1,x2)==(4,1))` est-il incorrect ? Adapter ce test.
