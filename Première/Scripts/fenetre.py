import tkinter as tk         # on importe la bibliotheque sous l'alias tk

fenetre = tk.Tk()            # fonction principale. La valeur renvoyée est la fenetre principale
fenetre.title("Bonjour !")   # définit le titre
fenetre.geometry("800x400")  # définit les dimensions (en pixels)
fenetre.mainloop()           # fonction qui crée la fenêtre. jusqu'à ce que l'utilisateur ferme la fenetre