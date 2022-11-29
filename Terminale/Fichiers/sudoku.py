# Sudoku

# Insérer ici le code des questions a) et b)

# Compléter ces deux fonctions afin que la visualisation de la grille
# et l'interaction avec son contenu fonctionnent

import tkinter as tk


def valeur_case(i, j):
    """ Retourne le chiffre affecté à la case i, j,
    ou bien la liste des chiffres possibles de cette case
    """
    #
    # À COMPLÉTER
    #
    return [i for i in range(1, 10)] # retourner les 9 chiffres

def changer_valeur(i, j, v):
   """ Affecte la valeur v à la case i, j """
   #
   # À COMPLÉTER
   #
   pass

# ---- La suite de ce fichier n'a pas besoin d'être modifiée ---

_root = tk.Tk()
_root.title("Sudoku")

class Affichage:
    """ Représente l'affichage de la grille de Sudoku """
    # La grille est formée de 9 blocs (pour pouvoir afficher leurs bords).
    # Chaque bloc contient 9 cases.
    # Chaque case affiche soit le nombre choisi,
    # soit les nombres possibles, en découpant la case en 9 sous-cases,
    # soit une erreur (fond rouge)

    def __init__(self):
        # initialiser le tableau de cases contenant l'état de chaque case
        self.cases = [[None for i in range(9)] for j in range(9)]
        # créer les 9 blocs, leurs cases et leurs sous-cases
        [[self.creer_bloc(i, j) for i in range(3)] for j in range(3)]

    def creer_bloc(self, i, j):
        """ Crée une grille de 3x3 blocs et la remplit de cases """
        f = tk.Frame(_root, borderwidth=2, relief='sunken')
        f.grid(row=i, column=j, sticky='nsew')
        for n in range(3):
            for m in range(3):
                self.cases[i*3+n][j*3+m] = self.creer_case(f, i*3+n, j*3+m)
        return f

    def creer_case(self, bloc, n, m):
        """ Crée les 9 cases d'un bloc, chacune contenant 9 sous-cases pour les chiffres """
        case = tk.Frame(bloc, borderwidth=2, relief='sunken')
        case.grid(row=n, column=m, sticky='nsew')
        for p in range(3):
            case.columnconfigure(p, minsize=30)
            case.rowconfigure(p, minsize=30)
        chiffres = [None]*9
        for p in range(3):
            for q in range(3):
                v = p*3+q + 1
                ch = chiffres[v-1] = tk.Label(case, text=str(v), fg = 'grey')
                ch.grid(row=p, column=q, sticky='nsew')
                # appeler self.click lorsque l'on clique sur une sous-case
                ch.bind("<Button-1>", lambda ev, v=v:self.click(n, m, v))
        # une case est représentée par un dictionnaire avec :
        #   - son état : 'chiffres', 'definitif', 'erreur' (s'il n'y a plus de chiffres possibles)
        #   - le bloc auquel elle appartient
        #   - le widget Tk qui la représente
        #   - la liste des chiffres qu'elle contient (si type == 'chiffres') ou None (si type == 'definitif')
        return {
            'type': 'chiffres',
            'bloc': bloc,
            'case': case,
            'chiffres': chiffres
        }

    def afficher_valeur(self, i, j, v):
        """ Afficher la valeur v dans la case i,j.
            v peut être un tableau de valeurs possibles,
            un chiffre définitif, ou None en cas d'erreur """
        case = self.cases[i][j]
        type = case ['type']
        bloc = case['bloc']
        chiffres = case['chiffres']

        if v == None or v == []:
            # pas de valeur : erreur dans la grille
            # détruire les sous-cases et afficher la case en rouge
            if type != 'erreur':
                case['type'] = 'erreur'
                case['case'].destroy
                case['chiffres'] = None
                erreur = case['case'] = tk.Frame(bloc, bg='red', borderwidth=2, relief='sunken')
                erreur.grid(row=i, column=j, sticky='nsew')
        elif isinstance(v, int):
            # remplacer la grille de chiffres possibles par un chiffre définitif
            if type != 'definitif':
                case['type'] = 'definitif'
                case['case'].destroy
                case['chiffres'] = None
                chiffre = case['case'] = tk.Label(bloc, text=v, font=(None, 40), borderwidth=2, relief='sunken')
                chiffre.grid(row=i, column=j, sticky='nsew')
        else:
            # mettre à jour les chiffres possibles
            # on "efface" les chiffres non possibles en les affichant en blanc
            for ch in range(1, 10):
                if ch in v:
                    chiffres[ch-1].config(fg='grey')
                else:
                    chiffres[ch-1].config(fg='white')

    def click(self, i, j, v):
        """ Fonction de rappel lorsque l'on clique sur un chiffre """
        case = self.cases[i][j]
        chiffres = case['chiffres']

        # ne rien faire s'il y a déjà un chiffre définitif
        if chiffres == None:
            return

        # ne rien faire si on a cliqué sur un chiffre blanc, donc non autorisé
        if chiffres:
            color = chiffres[v-1].cget('fg')
            if color == 'white':
                return

        # affecter le chiffre à la case
        changer_valeur(i, j, v)

        # mettre à jour la grille
        for i in range(9):
            for j in range(9):
                self.afficher_valeur(i, j, valeur_case(i, j))

# -- programme principal

# afficher la grille
ecran = Affichage()
# boucle d'interaction
tk.mainloop()
