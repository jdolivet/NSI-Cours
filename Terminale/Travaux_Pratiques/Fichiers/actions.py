# ------------------------------
#  La cuisine du système
#  - les actions possibles
# ------------------------------------------------------------

#
# Prendre des ingrédients
#

def prendre(filename):
    file = open(filename)
    quantite = int(file.readline())
    file.close()
    if quantite > 0: 
       quantite = quantite - 1
    file = open(filename,"w")
    file.write(str(quantite))
    file.close()
    return quantite

def prendre_un_abricot(pourquoi):
    print("Prendre un abricot,", pourquoi)
    return prendre("ingredients/abricot")

#
# Utiliser les ustensiles
#

def choisir_le_four():
    return "four", FileLock("ustensiles/four.lock")

def choisir_le_batteur():
    return "batteur", FileLock("ustensiles/batteur.lock")

def utiliser(ustensile, pourquoi):
    ustensile[1].acquire()
    print("Utiliser le", ustensile[0], pourquoi)

def liberer(ustensile, pourquoi):
    print("Nettoyer le", ustensile[0], pourquoi)
    ustensile[1].release()
