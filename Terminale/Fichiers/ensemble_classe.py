class Ensemble:
    def __init__(self):
        self. taille = 0
        self. paquets = [[] for _ in range(23)]
        
    def contient(self, val):
        return val in self.paquets[val % 23]
    
    def ajoute(self, val):
        if not self.contient(val):
            self.taille += 1
            self.paquets[val % 23].append(val)
            
def contient_doublon(tab):
    ens = Ensemble()
    for elt in tab:
        if ens.contient(elt):
            return True
        ens.ajoute(elt)
    return False