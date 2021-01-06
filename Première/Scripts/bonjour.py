import sys

nom = "à toi"
if len(sys.argv) == 2:
    nom = sys.argv[1]
    
print("Bonjour", nom, '!')