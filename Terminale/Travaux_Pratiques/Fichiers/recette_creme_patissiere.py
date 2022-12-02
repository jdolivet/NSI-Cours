# ------------------------------
#  La cuisine du système
#  - recette de la crème pâtissière
# ------------------------------------------------------------

import actions
from time import sleep

recette = "pour faire la crème pâtissière"

actions.prendre_du_sucre(recette)
four = actions.choisir_le_four()
actions.utiliser(four, recette)

print("caramélisation en cours", recette)
sleep(2.0)
print("caramel prêt", recette)

actions.prendre_du_lait(recette)
actions.prendre_de_la_farine(recette)
actions.prendre_un_oeuf(recette)

batteur = actions.choisir_le_batteur()
actions.utiliser(batteur, recette)

print("mélanger les ingrédients", recette)
sleep(2.0)
print("ajouter les ingrédients au caramel dans le four", recette)
sleep(2.0)
print("cuisson terminée", recette)

actions.liberer(four, recette)
actions.liberer(batteur, recette)
