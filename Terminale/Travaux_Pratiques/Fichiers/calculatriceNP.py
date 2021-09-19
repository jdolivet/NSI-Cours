# Classe Pile
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
    

# Variables globales
operateurs = { '*' : (lambda a, b : a * b), '+' : (lambda a,b : a + b), 
              '/' : (lambda a,b : a / b), '-': (lambda a,b : a - b)}
pileCalcul = Pile()

print('Calculatrice simplifiée')
print('Entrer un nb entier ou un operateur')
print('Pour retourner le resultat : =')

def calcul():
    """Procédure permettant d'effectuer un calcul en Notation Polonaise """
    #il faut vider la pile de calcul, si erreur dans le dernier calc
    while not pileCalcul.est_vide():   
        pileCalcul.depiler()
    pileCalcul.empiler('end')
    while True:
        # on rentre des nbs entiers, ou opérateurs. '=' pour arrêter
        entree = input('Instruction calculatrice : ') 
        if entree == '=':
            break
        elif entree in operateurs:
            pileCalcul.empiler(entree)
        else: # si c'est un nb 
            suivant = pileCalcul.depiler()
            while (suivant != 'end') and (suivant not in operateurs): # si c'est un nb et pas la fin de la pile
                op = pileCalcul.depiler()
                entree = operateurs[op](float(suivant), float(entree))
                suivant = pileCalcul.depiler()
            pileCalcul.empiler(suivant)
            pileCalcul.empiler(entree)
        print('Pile :', pileCalcul)
    final = pileCalcul.depiler()
    print('Résultat :', final)   # pas de return
