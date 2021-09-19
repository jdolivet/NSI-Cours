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

