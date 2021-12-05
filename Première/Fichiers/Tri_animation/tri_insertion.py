from animation_tri import *

# On importe un module permettant de manipuler des tableaux de barres
# La taille de la barre correspond à sa valeur
# L'animation est construite à partir du module Turtle
        
def insere(tab, i, val):
    """Procédure qui insère val dans tab[0..i[ supposé trié"""
    j = i
    while j > 0 and tab[j - 1] > val:
        tab[j] = tab[j - 1]
        j = j - 1
    tab[j] = val
    
def tri_par_insertion(tab):
    """Procédure qui trie le tableau tab dans l'ordre croissant"""
    tmp = Case() # On créé un tableau de taille 1
    for i in range(1, len(tab)):
        # invariant : tab[0..i[ est trié
        tmp[0] = tab[i]
        insere(tab, i, tmp[0])

def play():
    """Gestionnaire d'évènement.
    Execute la fonction tri_par_insertion sur le tableau."""
    try:
        tri_par_insertion(tableau)
    except Terminator:
        pass
    
def animation(nb_barres):
    """ Fonction principale.
    nb_barres : nombre de barres choisis. Maximum : 15
    Lance l'algorithme de tri pour déplacer les barres et les trier."""
    title("Algorithme de tri par insertion")
    global tableau # Variables globales : utilisées par le gestionnaire.
    # On cree un tableau
    tableau = Tableau(nb_barres)
    # On le remplit
    for i in range(nb_barres):
        taille = randint(1, 10) # TAILLE_MAX=10 : taille maximale d'une barre
        tableau[i] = Barre(taille)
    # Consignes
    ht()
    penup()
    goto(0, 250) # HAUTEUR=250 : demi hauteur de l'animation
    write("Appuyer sur la touche espace pour commencer.", align="center", font=("Courier", 16, "bold"))
    # En attente d'un evenement
    onkey(play, "space") # On appelle le gestionnaire play()
    listen()
    mainloop()
    
animation(7)