# Les Quadtrees (arbres quaternaires)

from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as img
from matplotlib.patches import Rectangle

##################################################################
# Question 1 : implémenter les quadtree
# Compléter le constructeur de QtNode. Il s'agit de 
# - déterminer si le carré de pixels est uniforme
# - construire récursivement les 4 sous-arbres.
##################################################################

##################################################################
# Questions suivantes: implémenter les méthodes correspondant à l'énoncé.
##################################################################

class QtNode:
    """ Classe qui implémente un sous-arbre du quadtree. """

    def __init__(self, matrix, i_min, i_max, j_min, j_max):
        """ Entrée:
        - matrix : une matrice carrée à valeurs dans {0,1}.
            La matrice est de dimension d*d où d est de la forme 2**n
        - 4 entiers entre 0 et d : i_min < i_max et j_min < j_max.
            Ces entiers délimitent un carré de pixels entre (i_min,j_min) et (i_max,j_max).
            Il faut que tous les appels récursifs restend des carrés, donc il faut que
            i_max - i_min = j_max- j_min = d' où d' est de la forme 2**n'.
        Renvoie:
            un quadtree qui représente la partie de l'image matrix délimitée par les entiers.
        ----
        On indice les pixels de matrix de façon classique pour une matrice:
        m[i][j] est le pixel j (en partant de la gauche) sur la ligne i en partant du haut
        (i_min,j_min) : coin supérieur gauche.
        (i_max,j_min) : coin supérieur droite.
        (i_max,j_max) : coin inférieur droite.
        ----
        Complexité:
        Au plus profondeur du quadtree * nb_pixels_dans_le_carré.
        (en fait, la boucle while se termine dès qu'elle détecte que le carré n'est pas uniforme, donc la borne supérieure ci-dessus est trop pessimiste. 
        Les quadtree se construisent en temps linéaire dans le nombre de pixels de façon évidente sur certaines implémentations). """
        assert i_max <= len(matrix)
        assert i_max <= len(matrix[0])
        assert (i_max - i_min)%2 == 0 or (i_max - i_min) == 1
        assert (j_max - j_min)%2 == 0 or (i_max - i_min) == 1
        # Les frontières du carré représenté par le noeud.
        self.i_min = i_min
        self.j_min = j_min
        self.i_max = i_max
        self.j_max = j_max
        # La couleur du carré, None si non uniforme.
        self.couleur = None
        # Les 4 sous-arbres
        self.no = None
        self.ne = None
        self.so = None
        self.se = None


        # A compléter : parcourir le carré pour vérifier s'il est uniforme.
        # Créer une variable uniforme qui vaut True ssi le carré délimité est de couleur uniforme.

        if uniforme:
            self.couleur = c
        else:
            i_mid = (i_min + i_max) // 2
            j_mid = (j_min + j_max) // 2
            # A compléter : construire les 3 sous-arbres manquants
            self.se = QtNode(matrix, i_mid, i_max, j_mid, j_max)

    def recherche_pixel(self, i, j):
        """ Renvoie la couleur du pixel matrix[i][j] à partir du quadtree. """
        assert i_min <= i and i < i_max
        assert j_min <= j and j < j_max
        # A compléter

    def quadtree_to_matrix(self, matrix):
        """ Attention: cette méthode modifie son argument matrix.
        Entrée: une matrice initialement vide (None) sur les pixels délimités par le noeud.
        Attribue aux pixels de la matrice délimités par le noeud leur vraie couleur. """
        # A compléter

    def dessine(self, ax):
        """ Dessine un carré rouge autour de chaque chaque zone de l'image représentée par un noeud de couleur uniforme. """
        if self.couleur is None:
            self.no.dessine(ax)
            self.ne.dessine(ax)
            self.so.dessine(ax)
            self.se.dessine(ax)
        else:
            ax.add_patch(
                Rectangle(
                    (self.i_min, self.j_min),
                    self.i_max - self.i_min,
                    self.j_max - self.j_min,
                    linewidth=1,
                    edgecolor="r",
                    facecolor="none",
                )
            )


class QT:
    """ Classe qui implémente le quadtree.
    Notre implémentation est un peu naive, 
    mais les implémentations optimisées du quadtree permettent de compresser efficacement les images sans perte d'information. """

    def __init__(self, matrix):
        """ Constructeur : construit le quadtree à partir d'une image """
        self.largeur = len(matrix[0])
        self.hauteur = len(matrix)
        assert self.largeur == self.hauteur
        self.racine = QtNode(matrix, 0, self.hauteur, 0, self.largeur)

    def to_matrix(self):
        matrix = [[None for j in range(self.largeur)] for i in range(self.hauteur)]
        self.racine.quadtree_to_matrix(matrix)
        return matrix

    def dessine(self, matrix):
        self.racine.dessine(ax)


# Test:
m1 = QT([[0, 0], [0, 0]])
print(m1.racine.couleur == 0)
m2 = QT([[0, 0], [1, 0]])
print(m2.racine.couleur is None)
print(m2.racine.no.couleur == 0)
print(m2.racine.ne.couleur == 1)


with Image.open("./python256.png") as image:
    # Construction du Quadtree
    # image.show()
    w = image.width
    h = image.height
    liste = image.getdata()
    matrix = [[liste[i * w + j] for j in range(w)] for i in range(h)]
    quadtree = QT(matrix)

    # Conversion du quadtree en image : on reconstruit l'image à partir du quadtree.
    matrix2 = quadtree.to_matrix()
    # verifier que tous les pixels sont affectes
    assert (
        len([(i, j) for i in range(h) for j in range(w) if matrix2[i][j] is None]) == 0
    )
    liste = [matrix2[i][j] for j in range(w) for i in range(h)]
    image2 = Image.new(image.mode, (w, h))
    image2.putdata(liste)
    # image2.show()

    # Affichage du quadtree
    fig, ax = plt.subplots()
    ax.imshow(image2)
    quadtree.dessine(ax)
    plt.show()
