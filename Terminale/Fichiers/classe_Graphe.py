import graphviz


class Graphe:
    """Un graphe non orienté comme un dictionnaire d'adjacence"""

    def __init__(self):
        self.adj = {}

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

    def to_dot(self):
        """Renvoie une chaîne de caractères contenant la description au format dot de self."""
        description = '/*\n\tGraphe\n*/\nstrict graph G {\n\tbgcolor="#FFFFFF";\n'
        for s in self.sommets():
            description += f'\t"{s}";\n'
            for v in self.voisins(s):
                description += f'\t"{s}" -- "{v}";\n'
        return description + '}'
    
    def show(self, nom="Graphe"):
        """Visualise l'arbre et produit deux fichiers : filename et filename.png
        le premier contenant la description de l'arbre au format dot, 
        le second contenant l'image au format PNG."""
        graphviz.Source(self.to_dot(), format='png').view(filename=nom)

