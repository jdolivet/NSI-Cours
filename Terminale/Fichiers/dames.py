# Jeu de dames

# CLASSE À COMPLÉTER
#
# Méthode `coup_possible` à compléter :
# On veut déplacer un pion de la couleur donnée ('blanc' ou 'noir'), 
# à la position i, j (0,0 est la case en haut à gauche du damier)
# vers la direction ('droite' ou 'gauche' par rapport au camp du pion).
# Cette fonction doit retourner :
#   0 si le coup n'est pas permis
#   1 si on déplace le pion d'une case
#   2 si on le déplace de deux cases (en mangeant le pion qu'il saute)

import Tkinter as tk


class Jeu:
    #
    # À COMPLÉTER
    #

    def coup_possible(self, couleur, i, j, dir):
        #
        # À COMPLÉTER
        #
        return 2

# ---- La suite de ce fichier n'a pas besoin d'être modifiée ---

_root = tk.Tk()

TAILLE = 40

# Cette classe représente le damier visuellement et permet de bouger les pions à la souris.
# Le constructeur prend en paramètre un objet de la classe Jeu.
# Cette classe appelle la méthode `coup_possible` de cet objet lorsque le joueur déplace un pion.
# Il n'est pas utile de lire ni de comprendre le contenu de cette classe.

class Affichage:
    def __init__(self, jeu):
        self.jeu = jeu
        # créer le plateau de jeu
        self.grille = grille = tk.Canvas(_root, width=10*TAILLE, height=10*TAILLE)
        # créer le quadrillage et la configuration initiale
        for i in range(10):
            for j in range(10):
                if (i+j) % 2 == 1: # on ne crée que les cases sombres, sur lesquelles sont les pions
                    # coordonnées de la case
                    x1, y1 = i*TAILLE, j*TAILLE
                    x2, y2 = (i+1)*TAILLE, (j+1)*TAILLE
                    # créer la case
                    grille.create_rectangle(x1, y1, x2, y2, fill='brown')
                    # coordonnées du rectangle englobant le pion
                    x1, x2 = x1+5, x2-5
                    y1, y2 = y1+5, y2-5
                    # créer les pions noirs sur les 4 premières lignes, les blancs sur les 4 dernières
                    if j < 4:
                        grille.create_oval(x1, y1, x2, y2, fill='black', tags=('pion', 'noir'))
                    elif j > 5:
                        grille.create_oval(x1, y1, x2, y2, fill='lightgrey', tags=('pion', 'blanc'))
        # mettre les pions au-dessus des cases
        grille.tag_raise("pion")
        # déclencher un cliquer-tirer lorsque l'on clique sur un pion
        grille.tag_bind ("pion", "<ButtonPress-1>", self.start_drag)
        grille.tag_bind ("pion", "<ButtonRelease-1>", self.end_drag)
        # afficher la grille
        grille.pack()

    def start_drag (self, event):
        """ début d'un cliquer-tirer """
        # suivre les mouvements de la souris
        event.widget.bind ("<Motion>", self.drag)
        # mettre le pion au-dessus des autres et le colorer en bleu
        self.grille.tag_raise(tk.CURRENT)
        self.grille.itemconfigure(tk.CURRENT, fill ="blue")
        # enregistrer le numéro de la case de départ
        self.i = event.x // TAILLE
        self.j = event.y // TAILLE
        # et la position de départ
        self.x = self.start_x = event.x
        self.y = self.start_y = event.y

    def drag (self, event):
        """ mouvement d'un cliquer-tirer """
        # déplacer le pion du mouvement de la souris
        dx = event.x - self.x
        dy = event.y - self.y
        self.grille.move(tk.CURRENT, dx, dy)
        self.x, self.y = event.x, event.y

    def end_drag(self, event):
        """ fin d'un cliquer-tirer """
        # arrêter de suivre la souris
        event.widget.unbind ("<Motion>")

        # mouvement à effectuer pour revenir au point de départ
        # ce déplacement sera ajusté en fonction du résultat du coup
        dx = event.x - self.start_x
        dy = event.y - self.start_y

        # nombre de cases et direction dans laquelle il faudra déplacer le pion
        k = 0
        dir, xdir, ydir = None, 0, 0

        # les "tags" permettent de savoir si c'est un pion blanc ou noir
        tags = self.grille.gettags(tk.CURRENT)
        if 'blanc' in tags:
            couleur = 'blanc'
            if dy < -TAILLE/2: # il faut l'avoir déplacé vers le haut
                if dx > TAILLE/2: # et vers la droite
                    dir, xdir, ydir = 'droite', -1, 1
                elif dx < -TAILLE/2: # ou la gauche
                    dir, xdir, ydir = 'gauche', 1, 1
            # lui redonner sa couleur d'origine
            self.grille.itemconfigure(tk.CURRENT, fill ="lightgrey")
        else:
            couleur = 'noir'
            if dy > TAILLE/2: # il faut l'avoir déplacé vers le bas
                if dx > TAILLE/2: # et vers la droite (la gauche pour lui)
                    dir, xdir, ydir = 'gauche', -1, -1
                elif dx < -TAILLE/2: # et vers la gauche (la droite pour lui)
                    dir, xdir, ydir = 'droite', 1, -1
            # lui redonner sa couleur d'origine
            self.grille.itemconfigure(tk.CURRENT, fill ="black")

        # si le déplacement est dans une direction autorisée, essayer de jouer le coup
        if dir != None:
            k = self.jeu.coup_possible(couleur, self.i, self.j, dir)
            dx += xdir*k*TAILLE
            dy += ydir*k*TAILLE

        # déplacer le pion
        self.grille.move(tk.CURRENT, -dx, -dy)

        # si le déplacement était de 2 cases, cela veut dire qu'on a pris un pion
        # il faut donc retirer ce pion du damier
        if k == 2:
            # position du pion à retirer
            i, j = self.i - xdir, self.j - ydir
            x, y = i*TAILLE + TAILLE/2, j*TAILLE + TAILLE/2
            # chercher l'objet le plus proche et le retirer si c'est un pion
            prise = self.grille.find_closest(x, y, halo=5)
            if 'pion' in self.grille.gettags(prise):
                self.grille.delete(prise)

# programme principal : créer un jeu, son affichage, et laisser jouer
ecran = Affichage(Jeu())
tk.mainloop()
