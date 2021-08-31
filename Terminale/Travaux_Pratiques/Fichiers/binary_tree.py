import time
import graphviz

WHITE = '#FFFFFF'
BLACK = '#000000'

def escape_str(obj):
    '''
    convertit l'objet obj en une chaîne de caractères ASCII
    fct utile pour méthode to_dot des BinaryTree
    '''
    chaine = str(obj)
    chaine_echap = ''
    for c in chaine:
        n = ord(c)
        if 32 <= n <= 126 and c != '"':
            chaine_echap += c
        else:
            chaine_echap += '\\x{:04X}'.format(n)
    return chaine_echap
    
class BinaryTreeError(Exception):
    def __init__(self, msg):
        self.message = msg


class BinaryTree():
    def __init__(self, *args):
        if len(args) == 0:
            self.__content = None
        elif len(args) != 3:
            raise BinaryTreeError('bad arguments number for binary tree building')
        elif not isinstance(args[1], BinaryTree) or not isinstance(args[2], BinaryTree):
            raise BinaryTreeError('bad arguments type for binary tree building')
        else:
            self.__content = (args[0], args[1], args[2])

    def is_empty(self):
        return self.__content is None
        
    def get_data(self):
        try:
            return self.__content[0]
        except TypeError:
            raise BinaryTreeError('empty tree has no root')

    def get_left_subtree(self):
        try:
            return self.__content[1]
        except TypeError:
            raise BinaryTreeError('empty tree has no left subtree')

    def get_right_subtree(self):
        try:
            return self.__content[2]
        except TypeError:
            raise BinaryTreeError('empty tree has no right subtree')
            
    def __str__(self):
        if self.is_empty():
            return '()'
        else:
            repr_left = str(self.get_left_subtree())
            repr_right = str(self.get_right_subtree())
            return '({:s}, {:s}, {:s})'.format(str(self.get_data()), repr_left, repr_right)

    def is_leaf(self):
        '''
        prédicat pour tester si un arbre est une feuille ou non, i.e. un arbre de taille 1.
        '''
        return (not self.is_empty() and 
                self.get_left_subtree().is_empty() and
                self.get_right_subtree().is_empty())
    
    def to_dot(self, background_color=WHITE):
        '''
        renvoie une chaîne de caractères contenant la description au format dot de self.
        '''
        LIEN = '\t"N({:s})" -> "N({:s})" [color="{:s}", label="{:s}", fontsize="8"];\n'
        def aux(arbre, prefix=''):
            if arbre.is_empty():
                descr = '\t"N({:s})" [color="{:s}", label=""];\n'.format(prefix,
                                                                         background_color)
            else:
                c = arbre.get_data()
                descr = '\t"N({:s})" [label="{:s}"];\n'.format(prefix, escape_str(c))
                s_a_g = arbre.get_left_subtree()
                label_lien, couleur_lien = ('0', BLACK) if not s_a_g.is_empty() else ('', background_color)
                descr = (descr +
                         aux(s_a_g, prefix+'0') +
                         LIEN.format(prefix, prefix+'0', couleur_lien, label_lien))
                s_a_d = arbre.get_right_subtree()
                label_lien, couleur_lien = ('1', BLACK) if not s_a_d.is_empty() else ('', background_color)
                descr = (descr +
                         aux(s_a_d, prefix+'1') +
                         LIEN.format(prefix, prefix+'1', couleur_lien, label_lien))

            return descr
    
        return '''/*
  Binary Tree

  Date: {}

*/

digraph G {{
\tbgcolor="{:s}";

{:s}
}}
'''.format(time.strftime('%c'), background_color, aux(self))       
    
    def show(self, filename='arbre', background_color=WHITE):
        '''
        visualise l'arbre et produit deux fichiers : filename et filename.png
        le premier contenant la description de l'arbre au format dot, 
        le second contenant l'image au format PNG.
        '''
        graphviz.Source(self.to_dot(background_color=background_color), format='png').view(filename=filename)
        
if __name__ == '__main__':
   import doctest
   doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)


