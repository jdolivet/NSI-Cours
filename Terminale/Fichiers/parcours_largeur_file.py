from classe_File import File

class Graphe:
    """Un graphe orienté comme un dictionnaire d'adjacence."""
    
    def __init__(self):
        self.adj = {}
        
    def ajouter_sommet(self, s) -> None:
        if not (s in self.adj.keys()):
            self.adj[s] = set()
            
    def ajouter_arc(self, s1, s2) -> None:
        """Creation d'un lien s1 -> s2."""
        self.ajouter_sommet(s1)
        self.ajouter_sommet(s2)
        self.adj[s1].add(s2)
        
    def arc(self, s1, s2) -> bool:
        return s2 in self.adj[s1]
    
    def sommets(self) -> list:
        return list(self.adj.keys())
    
    def voisins(self, s) -> set:
        return self.adj[s]
        
def parcours(g: Graphe, vus: set, s) -> None:
    """Parcours en largeur depuis le sommet s.
    Version itérative. Avec la classe File."""
    file = File()
    file.ajouter(s)
    while not file.est_vide():
        s = file.retirer()
        if s not in vus:
            vus.add(s)
            for v in g.voisins(s):
                file.ajouter(v)

# Tests
g0 = Graphe()
g0.ajouter_arc('A', 'B')
g0.ajouter_arc('A', 'D')
g0.ajouter_arc('D', 'E')
g0.ajouter_arc('E', 'B')
g0.ajouter_arc('B', 'C')
g0.ajouter_arc('C', 'E')
g0.ajouter_arc('C', 'F')
g0.ajouter_arc('G', 'C')

visites = set()
parcours(g0, visites, 'A')
for sommet in ['A','B','C','D','E','F']:
    assert sommet in visites
assert not 'G' in visites