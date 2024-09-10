class Cellule:
    """Une cellule d'une liste chaînée"""
    def __init__(self, v, s):
        self.valeur = v
        self.suivante = s

class File:
    """Structure de file"""
    def __init__(self):
        self.tete = None
        self.queue = None

    def est_vide(self) -> bool:
        return self.tete is None

    def ajouter(self, x) -> None:
        c = Cellule(x, None)
        if self.est_vide():
            self.tete = c
        else:
            self.queue.suivante = c
        self.queue = c

    def retirer(self):
        if self.est_vide():
            raise IndexError("retirer sur une file vide")
        v = self.tete.valeur
        self.tete = self.tete.suivante
        if self.tete is None:
            self.queue = None
        return v