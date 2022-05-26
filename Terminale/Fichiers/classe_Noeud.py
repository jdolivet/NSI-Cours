import graphviz


WHITE = "#FFFFFF"
BLACK = "#000000"

class Noeud:
    """Un noeud d'un arbre binaire"""
    def __init__(self, g, v, d):
        self.gauche = g
        self.valeur = v
        self.droit  = d

    def to_dot(self):
        """Renvoie une chaîne de caractères contenant la description au format dot de self."""
        def aux(arbre, prefixe=''):
            if arbre is None:
                description = f'\t"N({prefixe})" [color="{WHITE}", label=""];\n'
            else:
                c = arbre.valeur
                description = f'\t"N({prefixe})" [label="{c}"];\n'
                s_a_g = arbre.gauche
                description = (description +
                         aux(s_a_g, prefixe+'0') +
                         f'\t"N({prefixe})" -> "N({prefixe}0)" [color="{BLACK}", fontsize="8"];\n')
                s_a_d = arbre.droit
                description = (description +
                         aux(s_a_d, prefixe+'1') +
                          f'\t"N({prefixe})" -> "N({prefixe}1)" [color="{BLACK}", fontsize="8"];\n')
            return description  
        return f'/*\n\tArbre binaire\n*/\ndigraph G {{\n\tbgcolor="{WHITE}";\n{aux(self)}\n}}'   
    
    def show(self, nom="Arbre_binaire"):
        """Visualise l'arbre et produit deux fichiers : filename et filename.png
        le premier contenant la description de l'arbre au format dot, 
        le second contenant l'image au format PNG."""
        graphviz.Source(self.to_dot(), format='png').view(filename=nom)
