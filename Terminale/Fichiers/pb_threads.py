import threading
COMPTEUR = 0

def incrc():
    global COMPTEUR
    for c in range(100000):
        v = COMPTEUR
        COMPTEUR = v + 1

th = []
for n in range(4):
    t = threading.Thread(target=incrc, args=[])
    t.start()
    th.append(t)

for t in th:
    t.join()
print ("valeur finale", COMPTEUR)