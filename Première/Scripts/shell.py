import sys

print("Oh là là !", file = sys.stderr)
msg = sys.stdin.readline()                # se comporte comme input() mais avec \n en fin de chaîne
sys.stdout.write("Tu m'as dit : " + msg)  # se comporte comme print() mais sans \n en fin de chaîne