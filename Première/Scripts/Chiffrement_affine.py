import os

"""CHIFFREMENT AFFINE 
Ce programme permet de crypter un message 
Le message est en majuscule et sans ponctuation 
Chiffrement monoalphabetique de X par Y avec : Y≡a*X+b[26]"""

mot=input("entrer le message a crypter : ")

erreur_typo=0                     #analyse des contraintes typographiques
for lettre in mot:   
    if ord(lettre)<65 or ord(lettre)>90:
        erreur_typo+=1
if erreur_typo!=0:
    print("Le message doit être en majuscule, sans espace et sans ponctuation!")
else:

    #si la typographie du message permet le chiffrement
    cle_a=input("entrer la valeur de a : ")
    a=int(cle_a)
    if a%2==0 or a%13==0:           #test de la cle
        print("la valeur de a ne permet pas le dechiffrement!")

    #si la valeur de la cle permet le chiffrement
    else:
        cle_b=input("entrer la valeur de b : ")
        b=int(cle_b)
        mot_crypte=str()

        for lettre in mot:          #chiffrement du message
            nb=ord(lettre)-65
            nb_crypte=(a*nb+b)%26
            lettre_crypte=chr(nb_crypte+65)
            mot_crypte=mot_crypte+lettre_crypte

        for i in range(26):         #calcul de la cle de dechiffrement
            if (i*a)%26==1:
                a_inv=i%26
                b_inv=-a_inv*b%26

        #Affichage du resultat
        print("le message crypte est : ",mot_crypte,\
              "\n Secret : pour décrypter le message \n\
              utiliser le même programme avec la cle inverse : (",a_inv,";",b_inv,")")

os.system(" pause ")
