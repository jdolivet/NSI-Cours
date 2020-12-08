# Utilisation du débogage sur Thonny
# Utiliser le mode pas à pas (entrer dans le neoud)

def est_premier(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

test1 = est_premier(4)
test2 = est_premier(5)