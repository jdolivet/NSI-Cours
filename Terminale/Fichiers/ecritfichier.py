from os import getpid
pid = str(getpid())
with open ("test.txt", "w") as fichier:
    for i in range (1000):
        fichier.write(pid + " : " + str(i) + "\n")
        fichier.flush()
