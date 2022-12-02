# Routage par vecteurs de distance

import copy
# la fonction copy.copy(s) retourne une copie de la structure de données s,
# qui peut être un tuple, un tableau, un dictionnaire ou un objet.

  #  ┌──┐         ┌──┐          ┌──┐         ┌──┐   
  #  │R1│─────1───│R2│───1──────│R4│─────1───│R5│   
  #  └──┘         └──┘          └──┘         └──┘   
  #    │            │             │            │    
  #   1│            │             │           1│    
  #    │            │             │            │    
  #  ┌──┐           │             │          ┌──┐   
  #  │R3│─────1─────┘             └─────1────│R6│   
  #  └──┘                                    └──┘

class RIBItem():
  """ Représente une entrée de la table de routage """
  def __init__(self, router, distance, via):
    # à compléter

class Router():
  def __init__(self, name):
    # à compléter
  
  def addLink(self, router, distance):
    # à compléter

  def announce(self, level = 0):
    # à compléter

  def findLink(self, name):
    # à compléter

  def receive(self, fromRouterName, table, level):
    # à compléter

  def __str__(self):
    # à compléter

