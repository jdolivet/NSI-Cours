class Graphe:
    """Un graphe non - orienté représenté par un dictionnaire d'adjacence."""
    
    def __init__(self):
        self.adj = dict()
        
    def ajouter_sommet(self, s) -> None:
        if s not in self.adj:
            self.adj[s] = set()
            
    def ajouter_arc(self, s1, s2) -> None:
        self.ajouter_sommet(s1)
        self.ajouter_sommet(s2)
        self.adj[s1].add(s2)
        self.adj[s2].add(s1)
        
    def arc(self, s1, s2) -> bool:
        return s2 in self.adj[s1]
    
    def sommets(self) -> list:
        return list(self.adj)
    
    def voisins(self, s) -> set:
        return self.adj[s]
    
# Graphe des régions
g1 = Graphe()
g1.ajouter_sommet("Guadeloupe")
g1.ajouter_sommet("Martinique")
g1.ajouter_sommet("Guyane")
g1.ajouter_sommet("Mayotte")
g1.ajouter_sommet("La Réunion")
g1.ajouter_sommet("Corse")
g1.ajouter_arc("Hauts-de-France", "Normandie")
g1.ajouter_arc("Hauts-de-France", "Île-de-France")
g1.ajouter_arc("Hauts-de-France", "Grand Est")
g1.ajouter_arc("Normandie", "Île-de-France")
g1.ajouter_arc("Normandie", "Centre-Val de Loire")
g1.ajouter_arc("Normandie", "Pays de la Loire")
g1.ajouter_arc("Normandie", "Bretagne")
g1.ajouter_arc("Pays de la Loire", "Bretagne")
g1.ajouter_arc("Île-de-France", "Grand Est")
g1.ajouter_arc("Île-de-France", "Centre-Val de Loire")
g1.ajouter_arc("Île-de-France", "Bourgogne-Franche-Comté")
g1.ajouter_arc("Bourgogne-Franche-Comté", "Grand Est")
g1.ajouter_arc("Centre-Val de Loire", "Pays de la Loire")
g1.ajouter_arc("Centre-Val de Loire", "Bourgogne-Franche-Comté")
g1.ajouter_arc("Centre-Val de Loire", "Nouvelle-Aquitaine")
g1.ajouter_arc("Centre-Val de Loire", "Auvergne-Rhône-Alpes")
g1.ajouter_arc("Pays de la Loire", "Nouvelle-Aquitaine")
g1.ajouter_arc("Bourgogne-Franche-Comté", "Auvergne-Rhône-Alpes")
g1.ajouter_arc("Occitanie", "Nouvelle-Aquitaine")
g1.ajouter_arc("Auvergne-Rhône-Alpes", "Nouvelle-Aquitaine")
g1.ajouter_arc("Auvergne-Rhône-Alpes", "Occitanie")
g1.ajouter_arc("Auvergne-Rhône-Alpes", "Provence-Alpes-Côte d'Azur")
g1.ajouter_arc("Occitanie", "Provence-Alpes-Côte d'Azur")

assert len(g1.sommets()) == 18