#
# Chapitre 09 - TP 2 - Chemin le plus court avec l’algorithme de Dijkstra
#

from collections import defaultdict
# `defaultdict` fonctionne comme un `dict` Python.
# La seule différence est la valeur par défaut d'une clé :
# Dans un `dict` Python, une clé absente produit une erreur :
#   d1 = {}           # un dictionnaire Python standard
#   print(d1['toto']) # erreur !
#
# Dans un `defaultdict`, on peut choisir une valeur par défaut,
# par exemple une liste vide [] :
#   d2 = defaultdict(list)    # un dictionnaire dont les valeurs par défaut sont []
#   print(d2['toto'])         # []
#   d2['toto'].append('tutu') # d2['toto'] vaut ['tutu']

class Graphe:
  def __init__(self):
    self.noeuds = set()
    self.liens = defaultdict(list)
    self.distances = {}
        
  def ajout_noeud(self, valeur):
    self.noeuds.add(valeur)
    
  def ajout_lien(self, noeud_src, noeud_dest, distance):
    self.liens[noeud_src].append(noeud_dest)
    self.distances[(noeud_src, noeud_dest)] = distance

  def dijkstra(self, source):
    # copier ici le code de la fonction dijkstra 
    # de la partie cours
    return visite, chemin
  
  def chemin_vers(self, chemin, source, dest):
    resultat = []
    # à compléter
    return resultat

  def imprimer_chemin(self, chemin, source, dest): # ici chemin est un dictionaire 
    # à compléter

  def imprimer_tous_les_chemins(self,visite, chemin, source): # ici chemin est un dictionaire  
    # à compléter

  def route_vers(self, chemin, source, dest):
    # à compléter
    return (dest, ps) #ps est l'identifiant d'un noeud, le prochain saut.

  def routes_de(self, visite, chemin, source):
    table = dict() # dest -> prochain saut
    # à compléter
    return table

  def toutes_les_routes(self):
    tables = dict() # source -> dest -> prochain saut
    # à compléter
    return tables

  def imprimer_les_tables(self, tables):
    # à compléter