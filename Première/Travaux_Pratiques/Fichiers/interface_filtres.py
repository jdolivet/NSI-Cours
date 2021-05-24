import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import filtres


fenetre = tk.Tk()
fenetre.title("Traitement images")

canevas_gauche = tk.Canvas(fenetre, width = 256, height = 400, background = "grey")
canevas_gauche.pack(padx = 8, pady = 8, side = tk.LEFT)

panneau_boutons = tk.Frame(fenetre)
panneau_boutons.pack(side = tk.LEFT)

canevas_droite = tk.Canvas(fenetre, width = 256, height = 400, background = "grey")
canevas_droite.pack(padx = 8, pady = 8)

btn_fichier = tk.Button(panneau_boutons, text = "Ouvrir")
btn_fichier.pack(fill = tk.X)
btn_suppr_rouge = tk.Button(panneau_boutons, text = "Supprimer Rouge")
btn_suppr_rouge.pack(fill = tk.X)

def ouvrir_fichier(event):
    """ Gestionnaire d'événements
    Ouvre un sélecteur de fichier.
    L'utilisateur choisit une image : elle devient l'image de gauche de l'interface.    """
    global image_originale
    global image_originale_affichage
    filename = filedialog.askopenfilename()
    with Image.open(filename) as img:
        image_originale = img.copy()
        image_originale_affichage = ImageTk.PhotoImage(image = img)
    canevas_gauche.create_image(0, 0, image = image_originale_affichage, anchor = tk.NW)
    
def mise_a_jour_images():
    """ Cette procédure doit être appelée après toute modification de image_transforme. """
    global image_transforme_affichage
    image_transforme_affichage = ImageTk.PhotoImage(image = image_transforme)
    canevas_droite.create_image(0, 0, image = image_transforme_affichage, anchor = tk.NW)

def applique_filtre_supprime_rouge(event):
    """
    Procédure appliquant le filtre à l'image orginale
    """
    global image_transforme
    image_transforme = filtres.filtre_supprime_rouge(image_originale)
    mise_a_jour_images()
    
    
btn_fichier.bind("<Button-1>", ouvrir_fichier)
btn_suppr_rouge.bind("<Button-1>", applique_filtre_supprime_rouge)

fenetre.mainloop()