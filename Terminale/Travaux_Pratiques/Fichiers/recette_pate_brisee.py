# ------------------------------
#  La cuisine du système
#  - recette de la pâte brisée 
# ------------------------------------------------------------

import actions
from time import sleep

recette = "pour faire la pâte brisée"

actions.prendre_du_beurre(recette)
actions.prendre_de_la_farine(recette)
actions.prendre_du_sucre(recette)

batteur = actions.choisir_le_batteur()
actions.utiliser(batteur, recette)

print("mélanger les ingrédients", recette)
sleep(2.0)

four = actions.choisir_le_four()
actions.utiliser(four, recette)

print("cuisson en cours", recette)
sleep(5.0)
print("fin de cuisson", recette)

actions.liberer(four, recette)
actions.liberer(batteur, recette)
