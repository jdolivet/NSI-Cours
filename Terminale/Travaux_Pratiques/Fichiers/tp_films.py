# Indexer une collection avec un ABR 

from csv import DictReader  # utilisé pour lire le fichier csv.
import time  # utilisé pour chronométrer les durées d'exécution


##################################################################
# Question 3 (a) : insertion dans un tableau
##################################################################
class Film:
    def __init__(self, movie_id, titre, genres):
        self.movie_id = movie_id
        self.titre = titre
        self.genres = genres


liste_films = []
with open("movies.csv") as f:
    for ligne_f in DictReader(f):
        ligne = dict(ligne_f)
        # list(ligne.keys()) == ['movieId', 'title', 'genres']
        # A compléter pour insérer des objets films dans liste_films.


##################################################################
# Question 3 (b) : insertion dans un ABR, trié par titre.
##################################################################


class ABR:
    """L'implémentation des Arbres Binaires de Recherche.
    A un détail près, on a renommé certains attributs car
    la recherche s'effectue sur une clé (titre de film), mais on insère un film."""

    def __init__(self, racine=None):
        self.racine = racine

    def recherche(self, cle):
        """ Suppose que l'arbre est organisé comme un ABR.
        Renvoie un NoeudABR correspondant à la clé, None s'il n'y en a pas 
        Entrée: 
        cle: une chaîne de caractères (représente un titre de film). """
        if self.racine is None:
            return None
        else:
            return self.racine.recherche(cle)

    def insere(self, film):
        """ Insère le film dans une feuille de l'arbre 
        si la clé (film.titre) n'est pas déjà présente dans l'arbre. 
        Si la clé apparaît déjà dans l'arbre, l'arbre n'est pas modifié.
        Préserve la propriété des ABR : pour chaque noeud de l'arbre,
        - les clés présentes dans son sous-arbre gauche sont plus petites que la clé du noeud.
        - les clés présentes dans son sous-arbre droit sont plus grandes que la clé du noeud. """
        if self.racine is None:
            self.racine = NoeudABR(None, None, film)
        else:
            self.racine.insere(film)


class NoeudABR:
    def __init__(self, g=None, d=None, f=0):
        """ Créée un noeud contenant le film f. """
        self.fils_g = g
        self.fils_d = d
        self.cle = f.titre
        self.movie_id = f.movie_id
        self.genres = f.genres

    def recherche(self, cle):
        """ Suppose que l'arbre est un ABR.
        Renvoie un NoeudABR correspondant à la clé, None s'il n'y en a pas 
        cle: une chaîne de caractères (représente un titre de film). """
        if cle == self.cle:
            return self
        elif cle < self.cle and self.fils_g is not None:
            return self.fils_g.recherche(cle)
        elif cle > self.cle and self.fils_d is not None:
            return self.fils_d.recherche(cle)
        else:  # le sous-arbre où poursuivre la recherche est vide
            return None

    def insere(self, f):
        """ Insère la clé f dans une feuille sous un descendant du noeud, si elle n'y est pas déjà. 
        Si la clé est déjà dans un descendant, l'arbre n'est pas modifié.
        Préserve la propriété des ABR : pour chaque noeud de l'arbre,
        - les clés présentes dans son sous-arbre gauche sont plus petites que la clé du noeud.
        - les clés présentes dans son sous-arbre droit sont plus grandes que la clé du noeud. """
        c = f.titre
        if c < self.cle:
            if self.fils_g is not None:
                self.fils_g.insere(f)
            else:
                self.fils_g = NoeudABR(None, None, f)
        elif c > self.cle:
            if self.fils_d is not None:
                self.fils_d.insere(f)
            else:
                self.fils_d = NoeudABR(None, None, f)


def creer_arbre_films(l_films, nb_films):
    """ Insère les "nb_films" premiers films dans un ABR. """
    assert nb_films <= len(l_films)
    # A compléter


abr_films = creer_arbre_films(liste_films, len(liste_films))

##################################################################
# Question 4 (a) : hauteur de l'ABR
##################################################################
def hauteur(noeud_arbre):
    """ Calcul de la hauteur du sous-arbre sous noeud_arbre par DFS
    Entrée: un NoeudABR
    Complexité : linéaire """
    # A compléter


# En déduire comment calculer la hauteur de abr_films :


##################################################################
# Question 4 (b) : profondeur moyenne des noeuds de l'ABR
##################################################################
def prof_aux(noeud_arbre):
    """ Calcule par DFS une paire (s, n) où
    - s est la somme de la profondeur de tous les noeuds de l'arbre
    (plus exactement la somme de la profondeur dans l'arbre complet 
    des noeuds qui se trouvent dans le sous_arbre sous noeud_arbre).
    s vaut 1 pour un arbre comportant un seul Noeud non vide
    - n est le nombre de noeuds du sous_arbre sous noeud_arbre
    Entrée: un NoeudABR
    Complexité : linéaire """
    if noeud_arbre is None:
        return 0, 0
    else:
        sommeg, nbg = prof_aux(noeud_arbre.fils_g)
        sommed, nbd = prof_aux(noeud_arbre.fils_d)
        return  # A compléter


def profondeur_moyenne(arbre):
    """ Calcul de la profondeur moyenne des noeuds de arbre par DFS
    Entrée: un NoeudABR
    Complexité : linéaire """
    # A compléter


# En déduire la profondeur moyenne de abr_films :
print(profondeur_moyenne(abr_films))


##################################################################
# Question 5 : comparaisons
##################################################################
# Implémenter ci dessous:
# - la fonction recherche_lineaire
# - l'insertion de film un par un dans un tableau trié : insertion_tableau_un_par_un
# - la recherche dichotomique : f


def film_titre(film):
    return film.titre


def recherche_lineaire(t, x):
    """ recherche linéaire : cherche x dans le tableau t
    Renvoie True si x est présent dans t, False sinon
    Complexité: O(len(t)) """
    pass  # A implémenter


def insertion_tableau_un_par_un(l_films, nb_films):
    """ Insère les "nb_films" premiers films dans un tableau (list Python), 
    et trie la liste après (lors de) chaque insertion, à l'aide du tri par insertion. """
    assert nb_films <= len(l_films)
    t = []
    for i in range(nb_films):
        f = l_films[i]
        t.append(f)
        # A ce point, t[-1] n'est pas nécessairement à sa place,
        # mais les éléments précédents du tableau sont triés.
        # A compléter :
        # réorganiser le tableau pour qu'il soit trié en utilisant le principe du tri par insertion
    return t


def f(t, x, a, b):
    """ Implémente la recherche dichotomique par titre de film
    Entrée: 
    - tableau t d'objets de classe Film, supposé triés par titre croissants.
    - x : chaîne de caractère (titre du film cherché)
    - a, b : indice minimal et maximal entre lequel on cherche le film dans t
    ----
    Renvoie:
    True s'il existe un film de titre x, False sinon
    ----
    Complexité: O(log(b-a)). """
    # A compléter


def recherche_dicho(t, x):
    """ Renvoie:
    True s'il existe un film de titre x dans t, False sinon
    ----
    Complexité: O(log(len(t))). """
    return f(t, x, 0, len(t) - 1)


def comparer_requetes(liste_non_triee, liste_triee, arbre_film):
    """ Entrée : 
    - une liste de films non triée, 
    - une liste comportant les mêms films triés par nom
    - un abr comportant les même films triés par nom
    Renvoie : d1, d2, d3 où :
    - d1 est le temps total nécessaire pour chercher tous les films, 1 par 1, par dichotomie dans la liste
    - d2 le temps total nécessaire pour chercher tous les films, 1 par 1, dans l'abr
    - d3 le temps total nécessaire pour chercher tous les films, 1 par 1, dans la liste non triée """
    debut = time.time()
    for x in liste_non_triee:
        _ = recherche_dicho(liste_triee, x.titre)
    temps1 = time.time()
    for x in liste_non_triee:
        _ = arbre_film.recherche(x.titre)
    temps2 = time.time()
    for x in liste_non_triee:
        _ = recherche_lineaire(liste_non_triee, x.titre)
    temps3 = time.time()
    return temps1 - debut, temps2 - temps1, temps3 - temps2


def comparer_construction_et_requetes(nb_films):
    """ Exécute l'insertion de nb_films, puis une requête par valeur insérée.
    Renvoie d0, d1, d2, d3, d4, d5 où:
    - d0 est la durée pour insérer nb_films dans le tableau non trié (on se contente donc de copier  les nb_films premiers films)
    - d1 est la durée pour insérer nb_films dans un tableau qu'on maintient trié après chaque insertion
    - d2 est la durée pour insérer nb_films dans un ABR
    - d3 est la durée totale pour nb_fims requêtes par dichotomie sur le tableau trié
    - d4 est la durée totale pour nb_fims requêtes sur l'ABR
    - d5 est la durée totale pour nb_fims requêtes par recherche lineaire sur le tableau
    ------
    Comme l'exécution est déjà relativement lente, 
    on se contentera de mesurer la durée d'une exécution de chaque algorithme, plutôt
    que d'évaluer la moyenne en répétant l'exécution. On néglige pour simplifier l'influence 
    des caches mémoire, etc. (ce qui n'est pas une très bonne pratique). """
    t0 = time.time()
    liste_non_triee = []
    for i in range(nb_films):
        liste_non_triee.append(liste_films[i])
    t1 = time.time()
    tableau_films = insertion_tableau_un_par_un(liste_films, nb_films)  # Très long.
    t2 = time.time()
    abr_films = creer_arbre_films(liste_films, nb_films)
    t3 = time.time()
    d3, d4, d5 = comparer_requetes(liste_non_triee, tableau_films, abr_films)
    return t1 - t0, t2 - t1, t3 - t2, d3, d4, d5


nb_films = 1000
liste_nbs = []
liste_durees = []
duree_max = 0
while nb_films <= len(liste_films) and duree_max < 5:
    print(nb_films)
    nouvelles_durees = comparer_construction_et_requetes(nb_films)
    liste_nbs.append(nb_films)
    liste_durees.append(nouvelles_durees)
    nb_films += 1000
    duree_max = max(nouvelles_durees)

print(liste_durees)
print(liste_nbs)

import timeit
from math import log
from matplotlib import pyplot

pyplot.plot(liste_nbs, [x[0] for x in liste_durees])
pyplot.plot(liste_nbs, [x[1] for x in liste_durees])
pyplot.plot(liste_nbs, [x[2] for x in liste_durees])
# pyplot.plot(liste_nbs, [x[2] for x in liste_durees])
pyplot.legend(
    [
        "tableau : copie non triée",
        "tableau : tri après chaque insertion",
        "insertion dans ABR",
    ]
)
pyplot.title("Durée totale des insertions en fonction du nombre de films")
# pyplot.savefig('tp_abr_cout_insertions.pdf')
pyplot.show()


from math import log
from matplotlib import pyplot

pyplot.plot(liste_nbs, [x[3] for x in liste_durees])
pyplot.plot(liste_nbs, [x[4] for x in liste_durees])
pyplot.plot(liste_nbs, [x[5] for x in liste_durees])
pyplot.legend(["recherches dichotomiques", "recherches abr", "recherches linéaires"])
pyplot.title("Durée totale des recherches en fonction du nombre de films")
# pyplot.savefig('tp_abr_cout_requetes.pdf')
pyplot.show()
