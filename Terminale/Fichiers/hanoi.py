from turtle import *

# Constantes
VITESSE = 5   # Vitesse d'execution des mvts. 10:fast - 1:slow
T1_X = -270   # Abscisse Tour 1
T2_X = 0      # Abscisse Tour 2
T3_X = 270    # Abscisse Tour 3
HAUTEUR = 300 # Hauteur des tours
LARGEUR = 900 # Largeur du support

class Disque(Turtle): 
    """Chaque disque est une tortue qui va se déplacer de tour en tour
    Herite de la classe Turtle."""
    def __init__(self, n):
        """Construit la tortue dont la forme est un rectangle.
        Sa taille (et sa couleur) dépend de son numero. 
        n : numero du disque
        nb_disques : variable globale (définie dans le programme principal)"""
        Turtle.__init__(self, shape="square", visible=False)
        self.speed(VITESSE)
        self.pu() # On ne dessine pas
        self.goto(0, HAUTEUR // 2)
        self.shapesize(1, n * 1.1, 2) # On obtient un rectangle
        self.fillcolor(n / nb_disques, 0, 1 - n / nb_disques)
        self.st() # On montre la tortue
        
class Tour(list): 
    """Chaque tour est une liste, utilisée comme une pile.
    Herite de la classe list."""
    def __init__(self, x):
        """Construit la tour.
        x : abscisse de la tour"""
        self.x = x
        trace_rect(HAUTEUR, 10, self.x - 5, -HAUTEUR // 2 - 10) # On trace la tour
    def empile(self, disc):
        """Empile un disque sur la tour
        disc : objet disque"""
        disc.setx(self.x)
        disc.sety(- HAUTEUR // 2 + 20 * len(self))
        self.append(disc)
    def depile(self):
        """Depile la tour
        Renvoie le disque du sommet de la tour"""
        disc = list.pop(self)
        disc.sety(HAUTEUR // 2)
        return disc
    
def hanoi(n, origine, intermediaire, destination):
    """ Algorithme des tours de Hanoi"""
    if n >= 1:
        # déplacer la tour des n-1 premiers disques de origine vers intermediaire
        hanoi(n - 1, origine, destination, intermediaire)
        # déplacer le plus grand disque de origine vers destination
        a_deplacer = origine.depile()
        destination.empile(a_deplacer)
        # déplacer la tour des n-1 premiers disques de intermediaire vers destination
        hanoi(n - 1, intermediaire, origine, destination)
        
def trace_rect(longueur, largeur, x_start, y_start):
    """Fonction auxiliaire permettant le tracé d'un rectangle.
    dimensions : longueur et largeur
    (x_start, y_start) : coordonnées du coin en bas à gauche."""
    t = Turtle()
    t.speed(0)
    t.ht()
    t.pu()
    t.goto(x_start, y_start)
    t.fillcolor("maroon")
    t.begin_fill()
    for _ in range(2):
        t.forward(largeur)
        t.left(90)
        t.forward(longueur)
        t.left(90)
    t.end_fill()        
    
def play():
    """Gestionnaire d'évènement.
    Execute la fonction hanoi."""
    try:
        hanoi(nb_disques, t1, t2, t3)
    except Terminator:
        pass
    
def principal(nb):
    """ Fonction principale.
    nb : nombre de disques choisis.
    Trace le support des disques.
    Initialise les 3 tours.
    Empile les nb disques sur la tour de gauche.
    Lance l'algorithme de Hanoi pour déplacer les disques sur la tour de droite."""
    title("Les tours de Hanoï")
    global t1, t2, t3, nb_disques # Variables globales : utilisées par le gestionnaire.
    # Tracé du support
    trace_rect(20, LARGEUR, -LARGEUR // 2, -HAUTEUR // 2 - 30)
    # Nb disques : max 12
    nb_disques = nb
    # Initialisation des 3 tours
    t1 = Tour(T1_X)
    t2 = Tour(T2_X)
    t3 = Tour(T3_X)
    # On empile les disques sur la première tour
    for i in range(nb_disques, 0, -1):
        t1.empile(Disque(i))
    # Consignes
    ht()
    penup()
    goto(0, -HAUTEUR)
    write("Appuyer sur la touche espace pour commencer.", align="center", font=("Courier", 16, "bold"))
    # En attente d'un evenement
    onkey(play, "space") # On appelle le gestionnaire play()
    listen()
    mainloop()
    
principal(5)