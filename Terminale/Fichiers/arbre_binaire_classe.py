import graphviz


WHITE = "#FFFFFF"
BLACK = "#000000"

class Noeud:
    """Un noeud d'un arbre binaire"""
    def __init__(self, g, v, d):
        self.gauche = g
        self.valeur = v
        self.droit  = d

    def to_dot(self, background_color=WHITE):
        """Renvoie une chaîne de caractères contenant la description au format dot de self."""
        def aux(arbre, prefixe=''):
            if arbre is None:
                description = f'\t"N({prefixe})" [color="{background_color}", label=""];\n'
            else:
                c = arbre.valeur
                description = f'\t"N({prefixe})" [label="{c}"];\n'
                s_a_g = arbre.gauche
                couleur_lien = BLACK
                description = (description +
                         aux(s_a_g, prefixe+'0') +
                         f'\t"N({prefixe})" -> "N({prefixe}0)" [color="{couleur_lien}", fontsize="8"];\n')
                s_a_d = arbre.droit
                couleur_lien = BLACK
                description = (description +
                         aux(s_a_d, prefixe+'1') +
                          f'\t"N({prefixe})" -> "N({prefixe}1)" [color="{couleur_lien}", fontsize="8"];\n')
            return description  
        return f'/*\n\tArbre binaire\n*/\ndigraph G {{\n\tbgcolor="{background_color}";\n{aux(self)}\n}}'   
    
    def show(self, filename="Arbre_binaire", background_color=WHITE):
        """Visualise l'arbre et produit deux fichiers : filename et filename.png
        le premier contenant la description de l'arbre au format dot, 
        le second contenant l'image au format PNG."""
        graphviz.Source(self.to_dot(background_color=background_color), format='png').view(filename=filename)
