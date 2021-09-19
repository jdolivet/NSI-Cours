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
    