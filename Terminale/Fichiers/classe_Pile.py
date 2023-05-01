class Cellule:
    """Une cellule d'une liste chaînée"""
    def __init__(self, v, s):
        self.valeur = v
        self.suivante = s

class Pile:
    """Structure de pile"""
    def __init__(self):
        self.contenu = None

    def est_vide(self):
        return self.contenu is None

    def empiler(self, v):
        self.contenu = Cellule(v, self.contenu)

    def depiler(self):
        if self.est_vide():
            raise IndexError("depiler sur une pile vide")
        v = self.contenu.valeur
        self.contenu = self.contenu.suivante
        return v