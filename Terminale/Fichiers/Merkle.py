from string import ascii_letters, digits, ascii_uppercase
from random import randint
from math import log10


caracteres = ascii_letters + digits + '!#$%&()*+,-./:;<=>?@[]^_`{|}~'
cles = ascii_uppercase
chiffres = digits

def generateur_Merkle(nb_lignes=100_000, long_secret=15, long_cle=4):
    """Génère deux fichiers textes, de longueur nb_lignes
    Chaque ligne fournit une association identifiant - secret
    La longueur de l'identifiant vaut int(log10(nb_lignes) + 1
    La longueur du secret est long_secret
        * un fichier texte public, chiffré, avec un chiffrement XOR,
        avec une clé différente pour chaque ligne (longueur de la clé : long_cle)
        composé de majuscules, sans accent. Il est destiné à être divulgué.
        Chaque ligne du fichier public est une chaîne de caractère correspondant à un objet de type bytes :
        elle peut être copié-collé pour être utilisé comme un objet de type bytes en Python.
        * un fichier texte privé, permettant d'associer un identifiant avec un mot de passe."""
    ens_ids = {''}
    long_id = int(log10(nb_lignes)) + 2
    with open("Merkle_public.txt", 'w') as public:
        with open("Merkle_prive.txt", 'w') as prive:
            for i in range(nb_lignes):
                # Création d'un identifiant (taille fixe, différent pour chaque ligne)
                identifiant = ''
                while identifiant in ens_ids: # on ne peut avoir 2 ids identiques
                    identifiant = ''
                    for _ in range(long_id):
                        identifiant += chiffres[randint(0, len(chiffres) - 1)]
                ens_ids.add(identifiant)
                # Création d'un message secret : c'est la clé que l'on veut transmettre
                secret = ''
                for _ in range(long_secret):
                    secret += caracteres[randint(0, len(caracteres) - 1)]
                # Création d'une petite clé qui permet de chiffrer (XOR) la ligne
                cle = ''
                for _ in range(long_cle):
                    cle += cles[randint(0, len(cles) - 1)]
                # On conserve les infos dans le fichier prive
                ligne = f"identifiant : {identifiant}, secret : {secret}"
                prive.write(f"{ligne}\n")
                # On chiffre la ligne puis l'ecrit dans le fichier public
                resultat = [ligne.encode()[j] ^ cle.encode()[j % len(cle)] for j in range(len(ligne))] # chiffrement
                chiffre = bytes(resultat)
                public.write(f"{chiffre}\n")
