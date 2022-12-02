## Déchiffrement de la méthode de Vigenère par analyse de fréquences

# Question 1

# À l'aide de la fonction extraire_lettres, on lit le fichier tp-vigenere-chiffre.txt 
# et on met l'ensemble des lettres du message chiffré dans une chaîne de caractères 
# nommé lettres_du_message. On ignore les caractères qui ne sont pas des lettres
# majuscules.

def extraire_lettres(nom_fichier):
    # On commence par lire le fichier et récupérer son contenu.
    f = open(nom_fichier)
    contenu = f.read()
    # On crée une liste qui va contenir uniquement les lettres majuscules
    # du fichier.
    lettres = ""
    # Pour chaque caractère du contenu, on regarde si c'est une majuscule
    # (donc comprise entre "A" et "Z" dans la table) et on l'ajoute
    # à la liste lettres si c'est le cas.
    for c in contenu:
        if ord(c)... # À COMPLÉTER
            lettres += ... # À COMPLÉTER            
    return lettres

# On peut alors afficher les lettres du message chiffré contenu 
# dans le fichier tp-vigenere-chiffre.txt .

lettres_du_message = extraire_lettres("tp-vigenere-chiffre.txt")
print(lettres_du_message)

# Question 2

# La fonction suivante sépare la chaîne donnée en paramètre en trois paquets.

def separer_en_paquets(chaine):
    p1, p2, p3 = [], [], []
    for i in range(len(chaine)):
        if i % 3 == 0:
            p1.append(chaine[i])
        # À COMPLÉTER
    return (p1, p2, p3)

# On la teste sur la chaîne "ABCDEFG".

chaine_test = "ABCDEFG"
print(separer_en_paquets(chaine_test))

# On l'applique ensuite sur la chaîne lettres_du_message obtenue précédemment.
# Indication : chacun doit contenir 123 caractères.

paquet_1, paquet_2, paquet_3 = separer_en_paquets(lettres_du_message)
print(paquet_1, paquet_2, paquet_3)

# Question 3

# La fonction suivante renvoie la lettre la plus fréquente d'une liste l
# donnée en paramètre.

def trouver_lettre_la_plus_frequente(l):
    # Les clefs du dictionnaire occurrences sont les lettres rencontrées
    # dans la liste l, et ses valeurs sont le nombre de fois où ces lettres
    # apparaissent dans la liste l.
    occurrences = {}
    # On initialise la valeur de lettre_la_plus_frequente à la première
    # lettre de la liste l.
    lettre_la_plus_frequente = l[0]
    # Son nombre d'occurrences est donc temporairement égal à 1.
    occurrences[lettre_la_plus_frequente] = 1
    # Le nombre maximal d'occurrences d'une lettre est donc lui aussi
    # initialisé à 1.
    occurrence_max = 1

    # On parcourt alors la liste l. Pour chaque lettre rencontrée,
    # on met à jour son nombre d'occurrences. Si ce dernier devient
    # supérieur au nombre maximal occurrence_max, on met également
    # occurrence_max et lettre_la_plus_frequente à jour.
    for lettre in l[1:]:
        occurrences[lettre] = ... # À COMPLÉTER
        if occurrences[lettre] > occurrence_max:
            occurrence_max = ... # À COMPLÉTER
            lettre_la_plus_frequente = ... # À COMPLÉTER
    return lettre_la_plus_frequente

lettre_la_plus_frequente_1 = trouver_lettre_la_plus_frequente(paquet_1)
lettre_la_plus_frequente_2 = trouver_lettre_la_plus_frequente(paquet_2)
lettre_la_plus_frequente_3 = trouver_lettre_la_plus_frequente(paquet_3)
print(lettre_la_plus_frequente_1,lettre_la_plus_frequente_2,lettre_la_plus_frequente_3)

# Question 4

# On compare le code ord("E")=69 et celui de la lettre la plus fréquente 
# trouvée précédemment afin de trouver le décalage (éventuellement négatif).

def trouver_decalage(lettre_la_plus_frequente):
    lettre_E_en_clair = ord("E")
    lettre_E_chiffree = ... # À COMPLÉTER
    return ... # À COMPLÉTER
    
# On applique cette fonction aux lettres les plus fréquentes des trois paquets.

d1 = trouver_decalage(lettre_la_plus_frequente_1)
d2 = trouver_decalage(lettre_la_plus_frequente_2)
d3 = trouver_decalage(lettre_la_plus_frequente_3)
print(d1, d2, d3)

# On en déduit le mot-clef représentant le décalage.

clef_1 = chr(d1)
clef_2 = chr(d2)
clef_3 = chr(d3)
clef = clef_1 + clef_2 + clef_3
print(clef)


# Question 5

def dechiffrement(nom_fichier, d1, d2, d3):
    # On commence par lire le fichier et récupérer son contenu.
    f = open(nom_fichier)
    contenu = f.read()
    # On utilise les décalages obtenus précédemment.
    decalages = [d1, d2, d3]
    # On initialise le décalage à utiliser sur la lettre en cours 
    # à d1 = decalages[0].
    decalage_en_cours = 0
    # On prépare une variable pour stocker le résultat
    message_clair = ""

    # Pour chaque caractère du contenu, on regarde si c'est une majuscule
    # (donc comprise entre "A" et "Z" dans la table) et on l'ajoute
    # à la liste lettres si c'est le cas.
    for c in contenu:
        if ord(c)... # À COMPLÉTER
            # On récupère le code de la lettre chiffrée en cours.
            lettre_chiffree = ord(c) - ord("A")
            # On lui applique le décalage nécessaire.
            lettre_en_clair = (lettre_chiffree ...) % 26 # À COMPLÉTER
            # On retransforme le code obtenu en lettre.
            c = chr(...) # À COMPLÉTER
            # On passe au décalage suivant pour la lettre suivante.
            decalage_en_cours = (...) % 3 # À COMPLÉTER
        message_clair = message_clair + c
    return message_clair

print(dechiffrement("tp-vigenere-chiffre.txt",d1, d2, d3))

# Question 6

def dechiffrement_complet(nom_fichier):
    lettres = extraire_lettres(nom_fichier)
    p1, p2, p3 = separer_en_paquets(lettres)
    d1 = trouver_decalage(trouver_lettre_la_plus_frequente(p1))
    d2 = trouver_decalage(trouver_lettre_la_plus_frequente(p2))
    d3 = trouver_decalage(trouver_lettre_la_plus_frequente(p3))
    return dechiffrement(nom_fichier, d1, d2, d3)

print(dechiffrement_complet("tp-vigenere-chiffre.txt"))



