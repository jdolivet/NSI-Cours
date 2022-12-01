# Automates à états finis

class Etat:
    """ Un état dans un automate à états, qui décrit ses
        propres transitions et à qui on peut assigner des
        actions en entrée et en sortie. """
    
    def __init__(self, nom, entree=None, sortie=None):
        """ • nom : nom de l'état (chaîne de caractères). 
                    Doit être unique dans un même 
                    automate à états.
            • entree : fonction appelée lors de l'entrée
                       dans l'état. `None` par défaut.
            • sortie : fonction appelée lors de la sortie
                       d'un état. `None` par défaut.  """
        self.nom = nom 
        self.entree_ = entree
        self.sortie_ = sortie
        
        # Pour facilement accéder à l'automate
        self.automate = None
        
        # Ajoutées au fur et à mesure, après la création
        # des états de l'automate.
        self.transitions = {}
    
    
    def entree(self, transition, evt):
        """ Fonction appelée lors de l'entrée dans un 
            état. Ne fait rien si aucune fonction 
            d'entrée n'a été définie. """
        if self.entree_ is not None:
            self.entree_(self, transition, evt)
        
    def sortie(self, transition, evt):
        """ Fonction appelée lors de la sortie d'un 
            état. Ne fait rien si aucune fonction 
            d'entrée n'a été définie. """
        if self.sortie_ is not None:
            self.sortie_(self, transition, evt)
    
    def applique(self, evt):
        """ Applique la transition correspondant à
            l'événement `evt`. """
        transition = self.transitions[evt.nom]
        transition.action(evt)
        
    def __repr__(self):
        """ Fonction appelée par défaut par `print()`
            pour représenter un objet sous forme 
            textuelle. """
        return f"État '{self.nom}'"
        
    
    
class Evenement:
    """ Un événement pouvant survenir dans notre automate
        à états, composé d'un nom (le type d'événement) 
        et de paramètres optionnels permettant de décrire
        les caractéristiques de l'événement si 
        nécessaire. 
        Par exemple, un événement "Insérer pièce" 
        nécessite de spécifier un montant.            """
    
    def __init__(self, nom, parametres=[]):
        self.nom = nom
        self.parametres = parametres
        
    def __repr__(self):
        """ Fonction appelée par défaut par `print()`
            pour représenter un objet sous forme 
            textuelle. """
        return f"['{self.nom}': {self.parametres}]"
        
      
    
class Automate:
    """ Un automate à états, composé d'`Etat`s et de 
        `Transition`s et permettant d'appliquer des
        `Evenement`s. """
    
    def __init__(self, liste_etats, etat_initial):
        """ • liste_etats : liste des états qui vont 
              composer l'automate. Chaque état ne doit 
              apparaître qu'une seule fois dans la liste.
            • etat_initial : l'état dans lequel 
              l'automate se trouve après son 
              initialisation.   """
        
        self.etats = {}
        for etat in liste_etats:
            if etat.nom in self.etats.keys():
                raise Exception(f"Un état nommé {etat.nom} existe déjà dans cet automate.")
            self.etats[etat.nom] = etat
            etat.automate = self
            
        self.etat_courant = etat_initial
        
        # On appelle la fonction d'entreée de l'état initial.
        self.etat_courant.entree(None, None)
        
    def evenement(self, evt):
        """ Applique l'événement `evt` à son état 
            courant, si cet état dispose d'une 
            `Transition` correspondante. """
        
        print(f"===> {evt.nom} ({evt.parametres})")
        if evt.nom in self.etat_courant.transitions.keys():
            # print(f"\tTransition {evt.nom} depuis {self.etat_courant.nom}")
            self.etat_courant.applique(evt)
        else:
            print(f'\tL’état courant "{self.etat_courant.nom}" ne traite pas les événements "{evt.nom}".')
        

        
class Transition:
    """ L'ensemble des tests et actions à entreprendre 
        lorsqu'un `Evenement` survient dans un `Etat`.
        Permet de spécifier deux états de sortie et deux 
        actions à effectuer lors de la transition, selon 
        que la garde est vraie ou fausse. """
    
    def __init__( self, 
                  etat_sortie, 
                  etat_sortie_non_garde=None, 
                  action=None, 
                  action_non_garde=None,
                  garde=None ):
        """ • etat_sortie : l'`Etat` de sortie de la 
              transition quand la garde renvoie `True`. 
              Peut être le même que l'état d'entrée.
            • etat_sortie_non_garde : [option] l'`Etat`
              de sortie lorsque la garde renvoie `False`.
            • action : [option] une fonction à appeler 
              lorsque la transition s'effectue quand la
              garde renvoie `True`.
            • action_non_garde : [option] fonction à 
              appeler lorsque la transition s'effectue 
              quand la garde renvoie `True`. 
            • garde : [option] fonction renvoyant un 
              booléen qui définit si la transition doit 
              être effectuée. """
        
        self.etat_sortie = etat_sortie
        self.etat_sortie_non_garde = etat_sortie_non_garde
        self.action_ = action
        self.action_non_garde_ = action_non_garde
        self.garde_  = garde
        
        # Pour facilement accéder à l'automate
        self.automate = etat_sortie.automate
    
    def action(self, evt):
        """ Appelée lorsqu'une transition est effectuée. 
            Teste la garde, appelle les différentes 
            fonctions `action` définies à 
            l'initialisation de la Transition, et passe à
            l'`Etat` suivant de l'`Automate`. """
        
        if self.garde(evt):
            if self.action_ is not None:
                self.action_(self, evt)
                
            # Passage à l'état suivant dans l'automate et
            # appel aux fonctions `sortie()` et `entree()`
            # correspondantes si elles existent.
            self.automate.etat_courant.sortie(self, evt)
            self.automate.etat_courant = self.etat_sortie
            self.automate.etat_courant.entree(self, evt)
                
        else: 
            # Pour le cas où on a également défini une 
            # transition quand la garde renvoie `False`.
            
            if self.action_non_garde_ is not None:
                self.action_non_garde_(self, evt)
                
            if self.etat_sortie_non_garde is not None:
                self.automate.etat_courant.sortie(self, evt)
                self.automate.etat_courant = self.etat_sortie_non_garde
                self.automate.etat_courant.entree(self, evt)
        
    def garde(self, evt):
        """ Appelle la fonction `garde` spécifiée à 
            l'initialisation si elle existe. """
        if self.garde_ is not None:
            return self.garde_(self, evt)
        else:
            return True
    
    
    
# Un exemple de machine simple

def A_entree(etat, transition, evt):
    print(f"On entre dans {etat.nom}.")
def A_sortie(etat, transition, evt):
    print(f"On sort de {etat.nom}.")
def B_entree(etat, transition, evt):
    print(f"Nous voilà dans {etat.nom}.")
def B_sortie(etat, transition, evt):
    print(f"Derrière nous, {etat.nom}.")
def C_entree(etat, transition, evt):
    print(f"Entrons dans dans {etat.nom}.")
def C_sortie(etat, transition, evt):
    print(f"Sortons de {etat.nom}.")
    
# Notez qu'il ne s'agit ici que d'exemples, 
# les fonctions d'entrée et de sortie peuvent
# faire autre chose que des print() !
          
a = Etat(nom="A", entree=A_entree) # Pas de fonction de sortie
b = Etat(nom="B", entree=B_entree, sortie=B_sortie)
c = Etat(nom="C", entree=C_entree, sortie=C_sortie)

automate = Automate( liste_etats=[a, b, c], 
                     etat_initial=a )

def clic_action(transition, evt):
    print(f"\tevt est {evt}, on boucle sur A !")
def pluc_garde(transition, evt):
    return len(evt.parametres) > 0 and type(evt.parametres[0]) == int
def pouac_action(transition, evt):
    print(f"\tevt est {evt}, on va vers {transition.etat_sortie}")
def pouac_garde(transition, evt):
    return "b" in evt.parametres
    
a.transitions["clic"] = Transition(etat_sortie=a, 
                                    action=clic_action)
a.transitions["pluc"] = Transition(etat_sortie=b, 
                                    garde=pluc_garde)
b.transitions["pouac"] = Transition(etat_sortie=c, 
                                     action=pouac_action,
                                     garde=pouac_garde)
c.transitions["gnouf"] = Transition(etat_sortie=a,)

sequence_evenements = [
    Evenement("clic", ),
    Evenement("clic", (1, 2, 3)),
    Evenement("pluc", ),
    Evenement("pluc", [31]),
    Evenement("pluc", ),
    Evenement("pouac", [1, 2, 'a']),
    Evenement("pouac", ['b', 2, 'a']),
    Evenement("gnouf", (None,)),
]

def tester_automate():
    for evt in sequence_evenements:
        automate.evenement(evt)