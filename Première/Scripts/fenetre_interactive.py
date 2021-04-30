import tkinter as tk

compteur = 0
def suivant ():
    global compteur
    compteur = compteur + 1
    return compteur

fenetre = tk.Tk()
fenetre.title("Compteur de clics")

l1 = tk.Label(fenetre, text = "Nombre de clics")
l2 = tk.Label(fenetre, text = "0")

l1.grid(row = 0, column = 0)
l2.grid(row = 1, column = 0)

def action_clic(e):
    l2.config(text = str(suivant()))

b = tk.Button(fenetre, text = "Clic !")
b.bind("<Button-1>", action_clic)
b.grid(row = 0, column = 1, rowspan = 2, columnspan = 2)

fenetre.mainloop()  