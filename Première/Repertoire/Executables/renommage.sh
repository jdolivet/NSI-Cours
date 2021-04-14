#!/bin/bash
# Ce script va parcourir les fichiers du répertoire courant et renommer les fichiers jpg
# Remarques : 
# il faut donner les droits d'exécution au fichier ( chmod +x renommage.sh )
# lancer l'exécution du script avec la commande ./renommage.sh

cpt=0; 
for file in *; 
	do 
		if [ "${file##*.}" = "jpg" ]; then 
			cpt=$((cpt + 1)); 
			mv "$file" "photos-$cpt.jpg"; 
		fi; 
	done
