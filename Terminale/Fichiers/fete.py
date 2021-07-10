from dates import cree, contient, ajoute
from random import randint

def fete_continue():
    compteur = 0
    nombre_dates = 0
    ens = cree()
    while nombre_dates < 366:
        compteur += 1
        val = randint(1, 366)
        if not contient(ens, val):
            nombre_dates += 1
            ajoute(ens, val)
    return compteur

n = 0
for _ in range(1000):
    n += fete_continue()
print("En moyenne", n / 1000, "élèves")