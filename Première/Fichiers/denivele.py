# ### Calcul de dénivelé en randonnée
# 
# Un randonneur est équipé d’un capteur enregistrant toutes les minutes l’altitude
#  (en nombre -pas forcément entier- de mètres) à laquelle il se trouve.
#  Compléter le code du fichier `denivele.py` pour calculer le dénivelé total, la plus longue montée et son dénivelé.

def montee(t):
    """
    Entrée: un tableau t de flottants, représentant l'altitudes du randonneur au fil du temps: 
    une mesure par minute.
    Sortie: un triplet (longueur_max, z_tot, z_maxl)
    - longueur_max indique la longueur maximale (en minutes) d'une montée.
    - z_maxl indique le dénivelé de cette plus longue montée
    - z_tot indique le dénivelé total.
    
    On définit une montée comme une suite d'au moins 2 altitude consécutives croissantes.
    On notera que la plus longue montée n'est pas forcément celle qui a le plus grand dénivelé.
    """
    longueur_max = 0
    z_tot = 0
    z_maxl = 0
    nbtemp = 0
    ztemp = 0
    # Parcourir le tableau, en maintenant les invariants suivants:
    # nbtemp = nombre d'étapes de la montée courante, 0 si on n'est pas sur une montée, au moins 1 si l'altitude courante est supérieure à la précédente...
    # ztemp = dénivelé depuis le début de la montée courante, 0 si on n'est pas sur une montée.
    # par exemple si on commence à .4 et l'altitude suivante est .6 alors nbtemp = 1, ztemp =.2
    # A compléter
    return (longueur_max, z_tot, z_maxl)

# Test:
print(montee([2.4, 1.1, .5, 1.2, 1.7,. 4, 7.2]) == (2, 8.0, 1.2))
