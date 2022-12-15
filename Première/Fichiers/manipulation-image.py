# ### Manipuler une image
# 
# Compléter le code du fichier `manipulation_image.py` pour manipuler la matrice d’une image afin de :
# 
# a) Charger dans une matrice m une image jpeg en couleur

# Charger dans une matrice m une image jpeg en couleur
#  (pas trop grande pour que la matrice se construise rapidement, par exemple 500 * 300 px).
#  Afficher le triplet $m[0][0]$.
# Pour charger une image, on utilisera la bibliothèque matplotlib
#  (on pourrait bien sûr aussi utiliser la bibliothèque PILLOW):
# 
# `from matplotlib import image`
# 
# `img = image.imread(chemin_de_image).tolist()`

# A compléter

# Pour `afficher` l'image stockée dans une telle matrice, on utilisera la fonction suivante:

from matplotlib import pyplot as plt
import numpy as np
def affiche_rgb(matrice, tit=''):
    """
    Entrée: matrice: list of list of couleurs 
    Une couleur est représentée par un triplet (r,g,b) (ou [r,g,b])
    où chaque valeur r (et g et b) est un flottant entre 0 et 255
    Affiche l'image stockée par la matrice.
    Le code diffère un peu de celui du TP car on suppose des entiers en entrée, et non des flottants. 
    On convertit la matrice dans un format (numpy array d'entiers sur 1 octet) reconnu par imshow.
    """
    plt.figure(1)
    plt.clf()
    plt.axis('off')
    plt.title(tit)
    plt.imshow(np.array(matrice, dtype='u1'))
    plt.show()

matrice=[[[255,155,0]]]

affiche_rgb(matrice)
affiche_rgb(img)

# b) Compléter la fonction suivante pour ajouter autour de l'image un cadre doré (R,G,B) = (255,223,0)
#  dont l'épaisseur soit 10% de la dimension la plus petite de l'image (arrondi à la valeur inférieure).


def ajoute_cadre(img):
    """ 
    Entrée: une matrice img de triplets RGB (3 entiers) représentant une image.
    Ajoute un cadre à l'image, de couleur rgb (255,223,0)
    """
    taille_cadre = # A compléter: le nombre de pixels sur le bord du cadre est 10% de la dimension (x ou y) la plus petite, arrondi inférieur.
    img2 = # A compléter: matrice aux bonnes dimension (on a ajouté un bord de cadre sur les 4 côtés), remplie de valeurs [255,223,0]
    # A compléter: recopier l'image d'origine au centre du cadre.
    return img2

img2 = ajoute_cadre(img)

affiche_rgb(img2)

# c) Calculer l'image obtenue en inversant la gauche et la droite dans l’image.

# A compléter

# d) Calculer l'image obtenue en pivotant l'image d'un quart de tour.

# A compléter


# e) Calculer l'image obtenue en convertissant l'image en nuances de gris,
#  en transformant chaque pixel (r,g,b) en (y,y,y) où `y = round(0.2126 * r  + 0.7152 * g + 0.0722 * b)`


# A compléter

