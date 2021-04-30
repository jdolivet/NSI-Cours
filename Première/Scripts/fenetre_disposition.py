import tkinter as tk

fenetre = tk.Tk()
l1 = tk.Label(fenetre, text = "Nombre de clics")
l2 = tk.Label(fenetre, text = "0")
b = tk.Button(fenetre, text = "Clic !")
l1.grid(row = 0, column = 0)                               # coin supérieur gauche
l2.grid(row = 1, column = 0)                               # coin inférieur gauche
b.grid(row = 0, column = 1, rowspan = 2, columnspan = 2)   # moitié droite
fenetre.mainloop()  