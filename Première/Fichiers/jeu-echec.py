# ### Jeu d’échec (cet exercice utilise `append`)
# 
# On modélise par une matrice 8x8 une fin de partie d’échec sans roques.
#  Les cases de la matrice contiennent un tuple (couleur, pièce),
#  ex : `('noir', 'cavalier')`, sauf les cases vides qui contiennent None.
# 
# Compléter le code du fichier `jeu-echec.py` pour définir le mouvement des pièces,
#  vérifier si un plateau correspond à une situation d’échec ou d’échec et mat.
#  Le fichier se contente bien sûr de modéliser des cas "simples" et non pas une partie entière.

# a) Ecrire une fonction `est_dans_echiquier` qui prend deux entiers x,y
#  et indique si la case (x,y) fait bien partie de l'échiquier,
#  c'est-à-dire vérifie si les entiers sont bien compris entre 0 et 7.


def est_dans_echiquier(x,y):
    """ Renvoie True ssi la case est bien dans l'échiquier """
    # A compléter

# Test:
print(est_dans_echiquier(2,4)==True)
print(est_dans_echiquier(0,8)==False)
print(est_dans_echiquier(3,-1)==False)

# b) On rappelle qu'on représente une pièce `p` par une paire (couleur, nom_de_la_pièce).
#  Et un échiquier par une matrice 8x8 dont chaque élément est soit une pièce soit `None`.
#  On rappelle qu'on s'interdit les roques.
# 
# Écrire une fonction `mouvements_tour` qui prend en entrée un échiquier, une couleur,
#  et les indices `x` et `y` d'une position, et renvoie la liste des cases menacées par la tour,
#  c'est-à-dire les cases où une tour de cette couleur pourrait se déplacer si elle était placée en (x,y)
#  (y compris les cases où elle pourrait aller uniquement en exposant le roi de sa couleur, ce qui est illicite aux échecs). 
# Une tour se déplace selon un des 2 axes vertical ou horizontal.
#  La tour ne peut pas traverser une autre pièce, donc si une autre pièce se trouve sur sa trajectoire: 
# - soit cette pièce est de la couleur opposée et alors la tour peut la "prendre", donc la case fait partie du résultat. 
# - soit cette pièce est de la même couleur et alors la tour doit s'arrêter avant.
# 
# Pour cette fonction, peu importe que la tour soit réellement placée ou pas dans l'échiquier à la position `x,y`.


def mouvements_tour(echiquier,couleur,x,y):
    res = []
    for direction in [(1,0), (0,1), (-1,0), (0,-1)]:
        dx, dy = direction
        i = 1
        # Ecrire une boucle qui parcourt les cases de l'échiquier dans la direction 
        # jusqu') rencontrer une case qui ne soit pas None ou qui soit or de l'échiquier.
        # Mettre à jour res en conséquence.
        # A compléter
    return res

# Test:
m = [[None]*8 for i in range(8)]
#m[5][2]=('noir','tour')
m[5][5]=('blanc','roi')
m[1][2]=('noir','roi')
print(sorted(mouvements_tour(m,'noir',5,2))==[(2,2),(3,2),(4,2),(5,0),(5,1),(5,3),(5,4),(5,5),(6,2),(7,2)])
print(sorted(mouvements_tour(m,'blanc',5,2))==[(1,2),(2,2),(3,2),(4,2),(5,0),(5,1),(5,3),(5,4),(6,2),(7,2)])
print(sorted(mouvements_tour(m,'blanc',3,3))==[(0,3),(1,3),(2,3),(3,0),(3,1),(3,2),(3,4),(3,5),(3,6),(3,7),(4,3),(5,3),(6,3),(7,3)])

# b) Procéder de même avec les mouvements du roi
# (comme précedemment, on considère toutes les cases menacées par le roi
#  y compris celles où le roi n'a pas le droit d'aller car cela le mettrait en échec,
#  mais pas les cases où une pièce de la couleur du roi se trouve déjà).

def mouvements_roi(echiquier,couleur,x,y):
    tx = [-1,0,1]
    ty = [-1,0,1]
    # Indice: si on énumère les paires (indice dans tx, indice dans ty) on obtient 9 directions. 
    # Le roi peut se déplacer dans 8 de ces directions.
    # A compléter

# Test:
m = [[None]*8 for i in range(8)]
m[5][5]=('blanc','roi')
m[4][4]=('noir','tour')
print(sorted(mouvements_roi(m,'noir',1,2))==[(0,1),(0,2),(0,3),(1,1),(1,3),(2,1),(2,2),(2,3)])
print(sorted(mouvements_roi(m,'noir',4,5))==[(3,4),(3,5),(3,6),(4,6),(5,4),(5,5),(5,6)])


# c) On suppose désormais (et pour tout le reste de l'exercice) que l'échiquier comporte un et un seul roi de chaque couleur.
# Ecrire une fonction qui prend en entrée un échiquier, une couleur et renvoie la position du roi de cette couleur.

def trouve_roi(echiquier, couleur_roi):
    """ Renvoie la position du roi couleur_roi """
    # A compléter

# Test:
m = [[None]*8 for i in range(8)]
#m[5][2]=('noir','tour')
m[5][5]=('blanc','roi')
m[1][2]=('noir','roi')
m[3][2]=('noir','tour')
print(trouve_roi(m,'noir')==(1,2))

# d) En réutilisant les fonctions `mouvements_tour` et `mouvements_roi` ci-dessus, écrire une fonction 
# `cases_menacees` qui prend en entrée un échiquier,
#  une position x et y à laquelle se trouve une pièce de l'échiquier,
#  et renvoie toutes les cases que la pièce menace
#  (c'est-à-dire toutes les cases qui lui sont accessibles y compris par un mouvement qui exposerait le roi).


def cases_menacees(echiquier, x, y):
    """ Renvoie les positions accessibles, y compris celles en prises pour le roi """
    # A compléter

# Test:
m = [[None]*8 for i in range(8)]
m[5][0]=('blanc','roi')
m[7][2]=('noir','roi')
m[7][0]=('noir','tour')
print(sorted(cases_menacees(m,7,0))==[(5, 0), (6, 0), (7, 1)])
m = [[None]*8 for i in range(8)]
m[5][0]=('blanc','roi')
m[7][2]=('noir','tour')
m[7][0]=('noir','roi')
print(sorted(cases_menacees(m,7,0))==[(6, 0), (6, 1), (7, 1)])

# e) En déduire une fonction `echec` qui prend en entrée un échiquier et une couleur,
#  et qui indique si le roi de cette couleur est en échec.

def echec(echiquier, couleur_roi):
    """ 
    Renvoie True ssi le roi de couleur couleur_roi est en echec 
    """
    # A compléter

m = [[None]*8 for i in range(8)]
m[5][2]=('noir','tour')
m[5][5]=('blanc','roi')
m[1][2]=('noir','roi')
print(echec(m, 'blanc'))

# f) Ecrire une fonction `mouvements_valides` qui, comme `cases_menacees` prend en entrée un échiquier,
#  et la position x et y d'une pièce de l'échiquier.
#  Par contre, `mouvements_valides` ne renvoie que les cases à laquelle la pièce peut aller
#   sans que cela mette ou laisse en échec le roi. 
# Une façon simple (à défaut d'être très efficace) d'implémenter cette fonction est de réutiliser
#  les fonctions `cases_menacees` et `echec` ci-dessus, pour filtrer parmi les cases menacées celles qui sont admissibles.
#  On peut construire pour chaque déplacement possible un échiquier "hypothétique" représentant le résultat du déplacement,
#  puis vérifier si le roi est en échec sur cet échiquier hypothétique. 
# 
# Pour cela:
# - soit on copie l'échiquier avec `[t.copy() for t in echiquier]`
# - soit on modifie l'échiquier plutôt qu'en créer un nouveau à chaque fois.
#   En ce cas ne pas oublier de remettre l'échiquier dans la position initiale après évaluer chaque position.


def mouvements_valides(echiquier, x, y):
    """Renvoie les cases où la pièce peut aller sans mettre ou laisser le roi en échec"""
    couleur, nom =  echiquier[x][y]
    res = []
    for nx,ny in cases_menacees(echiquier, x, y):
        piece_prise_eventuelle = echiquier[nx][ny]
        # A compléter
     return res

# Test
m = [[None]*8 for i in range(8)]
m[5][4]=('noir','tour')
m[4][2]=('blanc','roi')
m[2][2]=('noir','roi')
print(mouvements_valides(m,4,2)==[(4,1),(4,3)])

# g) A l'aide de la fonction précédente, écrire une fonction `echec_et_mat`
#  qui prend en entrée un échiquier et une couleur,
#  et qui indique si le roi de cette couleur est en "mat", "pat" ou "survit" au moins un tour.

def echec_et_mat(echiquier,couleur):
    """ 
    Suppose que c'est à couleur de jouer.
    Renvoie mat/pat/survie en fonction de la situation au tour courant.
    """
    couleur_adverse = {'blanc':'noir', 'noir':'blanc'}[couleur]
    listes_mvts_valides = []
    # A compléter

m = [[None]*8 for i in range(8)]
m[5][2]=('noir','tour')
m[5][5]=('blanc','roi')
m[1][2]=('noir','roi')
print(echec_et_mat(m,'blanc')=='survit')

m = [[None]*8 for i in range(8)]
m[1][5]=('noir','tour')
m[0][0]=('blanc','roi')
m[0][2]=('noir','roi')
print(echec_et_mat(m,'blanc')=='pat')

m = [[None]*8 for i in range(8)]
m[7][0]=('noir','tour')
m[3][0]=('blanc','roi')
m[3][2]=('noir','roi')
print(echec_et_mat(m,'blanc')=='mat')

# Pour aller plus loin:
# 
# - On trouvera ci dessous: des fonctions permettant de visualiser un échiquier,
#   mais qui nécessitent d'installer la librairie chess.
# - On peut étendre à d'autre pièces les mouvements à d'autres pièces (fou, reine, cavalier.
#   Le pion est sans doute trop compliqué à gérer même au dernier tour à cause des cas particuliers: prise en passant, promotion...).
# - On peut écrire une fonction qui étudie s'il existe un mouvement valide qui permette de faire échec et mat en un tour.

#Si la librairie chess est installée:
import chess
import chess.svg

def board_to_string(echiquier):
    """ 
    Renvoie une chaine de caractere qui represente l'echiquier. 
    Le format est celui de la bibliothèque chess 
    P.S. "from itertools import groupby" permettrait un code un peu plus elegant
    """
    d = {'roi':'k', 'reine':'q', 'tour':'r', 'fou':'b', 'cavalier':'n', 'pion':'p'}
    board_string = ''
    none_counter = 0
    for y in range(7,-1,-1):
        s = ''
        for x in range(8):
            if echiquier[x][y] is None:
                none_counter += 1
            else:
                couleur, piece = echiquier[x][y]
                if none_counter > 0:
                    s += str(none_counter)
                    none_counter = 0
                s += d[piece] if couleur == 'noir' else d[piece].upper()
        if none_counter > 0:
            s += str(none_counter)
            none_counter = 0
        board_string += s
        if y > 0:
            board_string += '/'
        # else we could add  w - - 0 1 to indicate white, turns...
    return board_string


def board_to_svg(echiquier):
    """ 
    Cree un fichier svg qui rempresente l'echiquier. 
    """
    board = chess.Board(board_to_string(echiquier))
    with open("/Users/benoitgroz/Documents/temp.svg","w") as f:
        f.write(chess.svg.board(board, size=350))


m = [[None]*8 for i in range(8)]
m[7][4]=('noir','tour')
m[3][0]=('blanc','roi')
m[3][2]=('noir','roi')
board_to_svg(m)
