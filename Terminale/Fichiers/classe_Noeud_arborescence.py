import graphviz


class Noeud:
    """Un noeud d'une arborescence"""
    def __init__(self, v, f):
        self.valeur = v
        self.fils = f

    def __str__(self):
        return f"({self.valeur}, [{', '.join(str(f) for f in self.fils)}])"

    def to_dot(self):
        """Renvoie une chaîne de caractères contenant la description au format dot de self."""
        def aux(arbre):
            if arbre is None:
                description = ''
            else:
                c = arbre.valeur
                description = ''
                for i in range(len(arbre.fils)):
                    s_a = arbre.fils[i]
                    description = (description + aux(s_a) + f'\t{c} -> {s_a.valeur};\n')
            return description  
        return f'/*\n\tArborescence\n*/\ndigraph G {{\n{aux(self)}}}'   
    
    def show(self, nom="Arborescence"):
        """Visualise l'arbre et produit deux fichiers : filename et filename.png
        le premier contenant la description de l'arbre au format dot, 
        le second contenant l'image au format PNG."""
        graphviz.Source(self.to_dot(), format='png').view(filename=nom)
