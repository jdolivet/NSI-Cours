# parseur simple utilisé pour le TP

# Classe arbre binaire
class Noeud:
    def __init__(self, *args):
        if len(args) == 0:
            self.contenu = None
        else:
            self.contenu = (args[0], args[1], args[2])

    def etiquette(self):
        return(self.contenu[0])

    def gauche(self):
        return(self.contenu[1])
        
    def droit(self):
        return(self.contenu[2])
    
    def est_vide(self):
        return self.contenu == None
    
    def est_feuille(self):
        return (not self.est_vide() and self.gauche().est_vide() and self.droit().est_vide())
    
    def __repr__(self):
        return "()" if self.est_vide() else '(' + str(self.etiquette()) + str(self.gauche()) + str(self.droit()) + ')'


# Classe arbre binaire mutable (basée sur des listes et non des tuples)
class NoeudMutable:
    def __init__(self, *args):
        if len(args) == 0:
            self.contenu = None
        else:
            self.contenu = [args[0], args[1], args[2]]# je passe aux listes pour pouvoir modifier

    def etiquette(self):
        return(self.contenu[0])

    def gauche(self):
        return(self.contenu[1])
        
    def droit(self):
        return(self.contenu[2])
    
    def est_vide(self):
        return self.contenu == None
    
    def __repr__(self):
        return "()" if self.est_vide() else '(' + str(self.etiquette()) + str(self.gauche()) + str(self.droit()) + ')'

    # ajout de méthodes
    def insere_etiquette(self, valeur):
        self.contenu[0] = valeur

    def insere_gauche(self, valeur):
        self.contenu[1] = NoeudMutable(valeur, NoeudMutable(), NoeudMutable())
        
    def insere_droit(self, valeur):
        self.contenu[2] = NoeudMutable(valeur, NoeudMutable(), NoeudMutable())
        
        
def copie_immuable(arbre_mutable):
    """ retourne la copie d'un arbre mutable en arbre immuable
    entree : NoeudMutable
    sortie : Noeud"""
    if arbre_mutable.est_vide():
        return Noeud()
    else:
        return Noeud(arbre_mutable.etiquette(),
                     copie_immuable(arbre_mutable.gauche()),
                     copie_immuable(arbre_mutable.droit()))
    
# classe Pile
class Maillon:
    def __init__(self, element, suivant=None):
        self.element = element
        self.suivant = suivant

class Pile:
    def __init__(self):
        """Crée une pile vide"""
        self.premier = None
        self.longueur = 0
        
    def __len__(self):
        """Donne la taille de la pile"""
        return self.longueur

    def empiler(self, elt):
        """Ajoute un élément sur le sommet de la pile"""
        premier = Maillon(elt)
        premier.suivant = self.premier
        self.premier = premier
        self.longueur += 1
        
    def depiler(self):
        """Enlève et renvoie l'élément situé sur le sommet de la pile"""
        if len(self) == 0:
            raise ValueError("depiler une pile vide")
        element = self.premier.element
        self.premier = self.premier.suivant
        self.longueur -= 1
        return element
    
    def est_vide(self):
        """Verifie si la pile est vide"""
        return self.longueur == 0

    def __repr__(self):
        maillon = self.premier
        resultat = ''
        for _ in range(len(self)):
            resultat += str(maillon.element) + '  '
            maillon = maillon.suivant
        return resultat
    
# Parseur
VIDE = NoeudMutable('', NoeudMutable(), NoeudMutable())
OPERATEURS = {'+', '-', '*', '/'}

def analyseSyntaxe(exp):
    """ Entree : string bien parenthésée
    Les operateurs doivent apparaître explicitement.
    Exemples :
        15 * 5 + (2 + 3) doit être ((15*5)+(2+3))
        6(9 + 7) + (7 − 14) doit être ((6*(9+7))+(7-14))
    Autrement dit : autant de couples de parenthèses que d'operateurs.
    Sortie : arbre binaire de la représentation syntaxique de l'expression."""
    # Tests
    # On verifie qu'il y a autant de parenthèses ouvrantes que de fermantes
    assert exp.count('(') == exp.count(')'),\
           "Attention, il faut autant de parenthèses ouvrantes que fermantes"
    # On verifie qu'il y a autant de parenthèses ouvrantes que d'operateurs
    assert exp.count('(') == sum([exp.count(op) for op in OPERATEURS]),\
           "Attention, il faut autant de couples de parenthèses que d'opérateurs"
    
    # Analyse lexicale
    # On fait un traitement pour pouvoir differencier '(', ')', '*', '-', '/', '+' et nbs.
    for car in OPERATEURS:
        exp = exp.replace(car, ' ' + car + ' ')
    for car in {'(', ')'}:
        exp = exp.replace(car, ' ' + car + ' ') 
    liste = exp.split()
    
    # Analyse syntaxique
    # On construit l'arbre mutable
    pile = Pile()
    arbre = VIDE
    pile.empiler(arbre)
    enCours = arbre
    # On parcourt la liste des operandes, operateurs et parentheses
    for elt in liste:
        if elt == '(':
            enCours.insere_gauche('')
            pile.empiler(enCours)
            enCours = enCours.gauche()
        elif elt in OPERATEURS:
            enCours.insere_etiquette(elt)
            enCours.insere_droit('')
            pile.empiler(enCours)
            enCours = enCours.droit()
        elif elt == ')':
            enCours = pile.depiler()
        else:
            enCours.insere_etiquette(int(elt))
            parent = pile.depiler()
            enCours = parent
    # on convertit en un arbre immuable (de la classe Noeud du cours)
    arbreBinaire = copie_immuable(arbre) 
    return arbreBinaire 
    
# tree1 = analyseSyntaxe('(3+(4*5  )     )')
# print(type(tree1))
# print(tree1)
# 
# tree2 = analyseSyntaxe('((6 * (9 + 7)) + (7 - 14))')
# print(tree2)