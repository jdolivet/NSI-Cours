# Ce fichier est le squelette d'une interface textuelle pour appeler les différentes
# fonctions à écrire dans le TP, il est à compléter. 
# Dans la version présente ces fonctions sont définies en début de fichier (elles
# sont vide, elles sont à écrire dans le TP).
# On peut les organiser ainsi, ou les regrouper dans un autre fichier dédié,
# qui pourra être importé depuis le présent fichier. 


#########################################################################################
# Ce menu contient les 5 fonctions à écrire dans le TP.
# Toutes les autres manipulations sont faites par l'utilisateur dans un client interactif :
# les fonctionnalités demandées dans le TP, et aussi les interrogations de la base (utiles aussi pour débuguer). 

def relance():
    print("Ici la fonction relance.")

def analyse():
    print("Ici la fonction analyse.")

def expedition():
    print("Ici la fonction expedition.")    

def achat():
    print("Ici la fonction achat.")

def paiement():
    print("Ici la fonction paiement.")

def menu():
    while True:
        print("""\
------------------------------------------
Bienvenue chez LCER
Entrez un entier :
  0 : Sortir du menu et du programme
Menu dirigeant :
  1 : Relance pour le paiement d'un débit
  2 : Analyse des ventes
  3 : Expédition d'un achat
Menu clients :
  4 : Achat d'un produit
  5 : Paiement du débit
------------------------------------------
""")
        n = int(input('Entrez votre choix : '))
        if n == 0:
            return
        elif n == 1:
            relance()
        elif n == 2:
            analyse()
        elif n == 3:
            expedition()
        elif n == 4:
            achat()
        elif n == 5:
            paiement()
        else:
            print('Choix non disponible')


menu()

###############################################################################
