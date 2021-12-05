from turtle import *
from random import randint
from time import sleep

# Constantes
VITESSE = 6     # Vitesse d'execution des mvts. 10:fast - 1:slow
LARGEUR = 500   # taille du tableau
TAILLE_MAX = 10 # taille max d'une barre
HAUTEUR = 250   # demi hauteur de l'animation

class Barre(Turtle): 
    """Chaque barre est une tortue qui va se déplacer
    Herite de la classe Turtle."""
    def __init__(self, taille):
        """Construit la tortue dont la forme est un rectangle.
        Sa taille (et sa couleur) dépend de son numero. 
        taille : taille de la barre
        nb_barres : variable globale (définie dans le programme principal)
        longueur : attribut de la barre"""
        Turtle.__init__(self, shape="square", visible=False)
        self.speed(VITESSE)
        self.longueur = taille       # attribut
        self.pu()                    # On ne dessine pas
        self.shapesize(taille, 1, 2) # rectangle
        self.fillcolor(taille / TAILLE_MAX, 0, 1 - taille / TAILLE_MAX)
        self.st()
        
    def __gt__(self, b):
        """ Surcharge de la methode de comparaison : >"""
        self.sety(- HAUTEUR + 10 * self.longueur)
        b.sety(- HAUTEUR + 10 * b.longueur)
        sleep(0.5)
        self.sety(0 + 10 * self.longueur)
        b.sety(0 + 10 * b.longueur)
        return self.longueur > b.longueur
    
    def __lt__(self, b):
        """ Surcharge de la methode de comparaison : <"""
        self.sety(- HAUTEUR + 10 * self.longueur)
        b.sety(- HAUTEUR + 10 * b.longueur)
        sleep(0.5)
        self.sety(0 + 10 * self.longueur)
        b.sety(0 + 10 * b.longueur)
        return self.longueur < b.longueur
    
        
class Tableau(list):
    """Tableau contenant les Barres."""
    def __init__(self, nb, x=- LARGEUR // 2):
        """Construit un tableau vide de taille nb.
        x : abscisse du depart du tableau.
        nb : taille du tableau"""
        for _ in range(nb):
            self.append(None)
        self.origine = x   # abscisse
        self.taille = nb
        trace_tab(self)
        
    def __setitem__(self, idx, barre):
        """Surcharge de la méthode d'affection de l'élément d'indice idx."""
        barre.sety(- HAUTEUR + 10 * barre.longueur)
        barre.setx(self.origine + idx * 30)
        barre.sety(0 + 10 * barre.longueur)
        super().__setitem__(idx, barre)
        
class Case(Tableau):
    """Tableau contenant une Barre."""
    def __init__(self, x=LARGEUR // 2):
        super().__init__(1, x)

def trace_tab(tab):
    """ Fonction auxiliaire permettant de tracer le support du tableau."""
    t = Turtle(visible=False)
    t.speed(0)
    t.width(2)
    t.ht()
    t.pu()
    t.goto(tab.origine - 15, 0)
    t.fillcolor("maroon")
    t.pd()
    t.sety(5)
    t.sety(0)
    for i in range(tab.taille + 1):
        t.setx(tab.origine - 15  + i * 30)
        t.sety(5)
        t.sety(0)