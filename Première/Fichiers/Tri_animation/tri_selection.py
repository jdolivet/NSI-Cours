from animation_tri import *

# On importe un module permettant de manipuler des tableaux de barres
# La taille de la barre correspond à sa valeur
# L'animation est construite à partir du module Turtle
        
def echange(tab, i, j):
    """Procédure qui échange les éléments du tableau d'indice i et j."""
    tmp = Case() # On créé un tableau de taille 1
    tmp[0] = tab[i]
    tab[i] = tab[j]
    tab[j] = tmp[0]
    
def tri_par_selection(tab):
    """Procédure qui trie le tableau tab dans l'ordre croissant"""
    for i in range(len(tab)):
        # invariant : tab[0..i[ est trié et <= à tab[i..[
        # on cherche le minimum de tab[i..[
        idx_min = i
        for j in range(i + 1, len(tab)):
            if tab[j] < tab[idx_min]:
                idx_min = j
        echange(tab, i, idx_min)
            
def play():
    """Gestionnaire d'évènement.
    Execute la fonction tri_par_selection sur le tableau."""
    try:
        tri_par_selection(tableau)
    except Terminator:
        pass
    
def animation(nb_barres):
    """ Fonction principale.
    nb_barres : nombre de barres choisis. Maximum : 15
    Lance l'algorithme de tri pour déplacer les barres et les trier."""
    title("Algorithme de tri par selection")
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