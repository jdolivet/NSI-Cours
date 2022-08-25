import string
from random import randint, shuffle
from math import log10
from time import perf_counter


caracteres = string.ascii_letters + string.digits + '!#$%&()*+,-./:;<=>?@[]^_`{|}~'
cles = string.ascii_uppercase
chiffres = string.digits

def generateur_Merkle(nb_lignes = 100_000, long_secret = 15, long_cle = 4):
    """Génère deux fichiers textes, de longueur nb_lignes
    Chaque ligne fournit une association identifiant - secret
    La longueur de l'identifiant vaut int(log10(nb_lignes) + 1
    La longueur du secret est long_secret
        * un fichier texte public, chiffré, avec un chiffrement XOR,
        avec une clé différente pour chaque ligne (longueur de la clé : long_cle)
        destiné à être divulgué.
        Chaque ligne du fichier public est une chaîne de caractère correspondant à un objet de type bytes :
        elle peut être copié-collé pour être utilisé comme un objet de type bytes en Python.
        * un fichier texte privé, permettant d'associer un identifiant avec un mot de passe."""
    ens_ids = set()
    liste_lignes = [''] * nb_lignes
    long_id = int(log10(nb_lignes)) + 2
    
    with open("Merkle_public.txt", 'w') as public:
        for i in range(nb_lignes):
            identifiant = ''
            for _ in range(long_id):
                identifiant += chiffres[randint(0, len(chiffres) - 1)]
            while identifiant in ens_ids: # on ne peut avoir 2 ids identiques
                identifiant = ''
                for _ in range(long_id):
                    identifiant += chiffres[randint(0, len(chiffres) - 1)]
            ens_ids.add(identifiant)
            password = ''
            for _ in range(long_secret):
                password += caracteres[randint(0, len(caracteres) - 1)]
            cle = ''
            for _ in range(long_cle):
                cle += cles[randint(0, len(cles) - 1)]
            ligne = f"identifiant : {identifiant}, mot de passe : {password}"
            liste_lignes[i] = ligne # On conserve la ligne pour le fichier prive
            resultat = [ligne.encode()[j] ^ cle.encode()[j % len(cle)] for j in range(len(ligne))] # chiffrement
            chiffre = bytes(resultat)
            public.write(f"{chiffre}\n")
            
    with open("Merkle_prive.txt", 'w') as prive:
        shuffle(liste_lignes) # evite une correspondance entre les lignes des fichiers prive et public
        for l in liste_lignes:
            prive.write(f"{l}\n")
