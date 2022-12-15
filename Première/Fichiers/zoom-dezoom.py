# ### Dézoomer sur une image
# 
# Le fichier `zoom-dezoom.py` contient un squelette de code si nécessaire.
# 
# a) Écrire une fonction qui prend en entrée une matrice et un entier k,
#  et qui renvoie une nouvelle matrice de taille réduite en ne conservant qu’une colonne et ligne sur k de la matrice (les 0,k,2k…​).


def reduit(m,k):
    return [ [m[k*i][k*j] for j in range(len(m[0])//k) ] for i in range(len(m)//k) ]


# b) Tester sur une petite matrice, puis observer l’effet sur une image en utilisant les fonctions `charge_img` et `affiche`

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def charge_img(filename):
    """
    Entrée: filename: text (chemin d'accès au fichier)
    Enregistre l'image sous forme d'une matrice de flottants dans [0,1.].
    Renvoie cette matrice.
    """
    return (np.array(Image.open(filename))/255).tolist()

def affiche(matrice, tit=''):
    """
    Entrée: matrice: list of list of float (tit: string)
    Affiche l'image stockée par la matrice.
    Si chaque valeur de la matrice est : 
    - un float entre 0 et 1. , alors échelle de gris 0 noir, 1. blanc
    - un triplets de 3 flottants entre 0 et 1, alors couleur (r,g,b), avec (0,0,0) noir, (0,0,.5) bleu un peu sombre, (1.,1.,1.) blanc

    Attention, les valeurs sont rééchelonnées de sorte que le min est noir, le max est blanc.
    Exemples: affiche([[1.,.9],[.5,0]])
    affiche([[(.1,.8,.1),(.2,.2,.2)]])
    """
    plt.figure(1)
    plt.clf()
    plt.axis('off')
    plt.title(tit)
    plt.imshow(matrice,cmap='Greys_r')
    plt.show()


# Il vaut mieux essayer avec une petite valeur de k: 2, 3 ou 4 pour que le résultat ressemble à l'image de départ.
# 
# Si on voulait une image un peu moins pixellisée on pourrait calculer la moyenne des pixels voisins,
# mais l'exercice serait plus compliqué. 

import urllib
url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Kingfisher-2046453.jpg/320px-Kingfisher-2046453.jpg'

m=[[ 1.,  2.,  3.,  4.],
[ 0.,  12.,  13.,  0.],
[ 0.,  22.,  23.,  0.],
[ 31.,  0.,  0.,  34.]]

print(reduit(m,2))

img = charge_img(urllib.request.urlopen(url))
affiche(reduit(img,4))

# c) De quel facteur diminue le nombre de pixels de la matrice si les dimensions de la matrice sont un multiple de k ?


# Le nombre de pixels est divisé par $k^2$ lorsque les 2 dimensions sont un multiple de $k$, et un peu moins sinon. 

