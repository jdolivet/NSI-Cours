# Sortie de labyrinthe

from random import randint
from math import sqrt, ceil, floor

# Changements de directions possibles depuis les
# coordonnées d'une salle du labyrinthe : 
#                   Haut, droite,   bas,   gauche
direction_diff = [(0, 1), (1, 0), (0, -1), (-1, 0)]

class Salle:
    def __init__(self, mur=True, entree=False, sortie=False):
        self.mur = mur
        self.entree = entree
        self.sortie = sortie
        self.visites = 0
        
    def __repr__(self):
        """ Fonction appelée par défaut par `print()`
            pour représenter un objet sous forme 
            textuelle. """
        
        resultat = ""
        if self.mur:
            resultat += "Mur"
        elif self.entree:
            resultat += "Entrée"
        elif self.sortie:
            resultat += "Sortie"
        else:
            resultat += "Salle"
            
        if self.visites > 0:
            resultat += f" [{self.visites}]"
        return resultat

class Labyrinthe:
    
    def __init__(self, salles, entree, sortie):
        self.salles = salles
        self.coord_entree = entree # coordonnées
        self.coord_sortie = sortie # coordonnées
        self.direction = 0
        
    def __repr__(self):
        """ Fonction appelée par défaut par `print()`
            pour représenter un objet sous forme 
            textuelle. """
        
        return f"Labyrinthe de {len(self.salles)} x {len(self.salles[0])} : {self.coord_entree} vers {self.coord_sortie}"
    
    def salle(self, coords):
        """ Renvoie la Salle correspondant aux `coords`
            passées en argument, si elle existe. """
        
        if 0 <= coords[0] < len(self.salles):
            if 0 <= coords[1] < len(self.salles[coords[0]]):
                return self.salles[coords[0]][coords[1]]
            
        return None
    
    def montrer(self):
        """ Renvoie une représentation textuelle du 
            labyinthe représentant ses murs, son entrée,
            sa sortie, et les salles déjà visitées. """
        
        resultat = " " + "-"*2*len(self.salles[0]) + "\n|"
        for l in range(len(self.salles)):
            for h in range(len(self.salles[l])):
                if self.salles[l][h].mur:
                    resultat += "█▊"
                elif self.salles[l][h].entree:
                    resultat += 'E '
                elif self.salles[l][h].sortie:
                    resultat += 'S '
                elif self.salles[l][h].visites > 0:
                    resultat += '. '
                else:
                    resultat += '  '
            if h < len(self.salles[0])-1:
                resultat += "-"*2*(len(self.salles[0])-len(self.salles[-1]))
            resultat += "|\n|"
        resultat = resultat[:-1] + "-"*2*len(self.salles[-1])
        return resultat
    
    def reinitialiser(self):
        """ Remet à zéro le nombre de visites
            des salles du labyrinthe. """
        
        for i in range(len(self.salles)):
            for j in range(len(self.salles[i])):
                self.salles[i][j].visites = 0
                
    def voisins(self, coords):
        """ Retourne la liste des coordonnées des salles 
            voisines à la salle aux coordonnées `coords`. """
        
        global direction_diff
        voisins = [ [ coords[i]+direction_diff[j][i] 
                      for i in range(len(coords)) ] 
                    for j in range(len(direction_diff)) ]
        
        return [ tuple(v) for v in voisins if self.salle(v) is not None ]
    
    def nb_aretes(self, coords):
        """ Nombre « d'arêtes » de la salle aux coordonnées 
            fournies, c'est à dire le nombre de ses voisins 
            qui ne sont pas des murs. """
        nb_aretes = 0
        for v in self.voisins(coords):
            s = self.salle(v)
            if (s is not None) and (not s.mur) and (not s.entree) and not s.sortie:
                nb_aretes += 1
        return nb_aretes
                
    def coords_direction(self, coords, nombre):
        """ Met à jour self.direction de `nombre`
        quarts de tour dans le sense antihoraire,
        et renvoie les coordonnées contigues à 
        `coords` dans cette direction. """
        
        global direction_diff
        self.direction = (self.direction + nombre) % 4
        diff = direction_diff[self.direction]
        return (coords[0] + diff[0], coords[1] + diff[1])
    

def creer_labyrinthe(nb_salles):
    """ Fonction utilisée pour générer des labyrinthes
        simples lors du chargement de `labyrinthe.py`. """
    
    largeur = int( floor( sqrt( nb_salles ) ) )
    hauteur = int( ceil( nb_salles / largeur ) )
    salles = [ [ Salle() for i in range(hauteur) ] for j in range(largeur) ]
    
    coord_entree = (randint(1, largeur//2-1), 0)
    coord_sortie = (randint(largeur//2, largeur-1), hauteur-1)
    salles[coord_entree[0]][coord_entree[1]].entree = True
    salles[coord_sortie[0]][coord_sortie[1]].sortie = True
    salles[coord_entree[0]][coord_entree[1]].mur = False
    salles[coord_sortie[0]][coord_sortie[1]].mur = False
    
    x = coord_entree[0]
    cds = False
    for h in range(1, hauteur):
        salles[x][h].mur = False
        if ((h%2==0) or abs(coord_sortie[0]-x)==hauteur-h) and x != coord_sortie[0]:
            diff = coord_sortie[0] - x
            x += diff // abs(diff)
            salles[x][h].mur = False
            
        if cds:
            cds = False
        elif randint(0, 10) > 2:
            cds = True
            direction = randint(0, 1) * 2 - 1
            for i in range(x+direction, max(1, min(largeur-1, x + 4 * direction)), direction):
                salles[i][h].mur = False
    
            
    return Labyrinthe(salles, coord_entree, coord_sortie)

labyrinthe_simple = creer_labyrinthe(200)

salles2 = [ [Salle() for i in range(10)] for j in range(10) ]
salles2[0][5].entree = True
salles2[5][5].sortie = True
salles2[0][5].mur = False
salles2[5][5].mur = False
for i in range(1, 9):
    salles2[i][1].mur = False
    salles2[i][8].mur = False
    salles2[1][i].mur = False
    salles2[8][i].mur = False
salles2[6][5].mur = False
salles2[7][5].mur = False
labyrinthe_complexe_1 = Labyrinthe(salles2, (0, 5), (5, 5))

salles3 = [ [Salle() for i in range(10)] for j in range(10) ]
salles3[0][5].entree = True
salles3[5][5].sortie = True
salles3[0][5].mur = False
salles3[5][5].mur = False
for i in range(1, 9):
    salles3[i][1].mur = False
    salles3[i][8].mur = False
    salles3[1][i].mur = False
    salles3[8][i].mur = False
labyrinthe_complexe_2 = Labyrinthe(salles3, (0, 5), (5, 5))
