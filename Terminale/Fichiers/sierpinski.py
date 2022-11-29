# Triangle de Sierpiński (page 132)

from turtle import forward, speed, left, right, pencolor, hideturtle, setheading

reset()


def t(d) -> None:
    """ Dessine un triangle donc chaque côté a pour longueur d.
    La tortue trace les trois côtés à partir de la position de départ, 
    en commençant par un trait horizontal vers la droite, puis vers le sommet en haut, 
    puis revient à la position de départ en étant orientée vers la droite."""
    speed(0)
    setheading(0)
    pencolor("blue")
    hideturtle()
    forward(d)
    left(120)
    # A compléter


def s(n: int, d) -> None:
    """ Dessine un triangle de sierpinski de niveau n dont les côtés ont pour longueur d (pour la figure complète).
    Le dessin commence par un trait horizontal vers la droite, 
    et termine à la position de départ, la tortue étant alors orientée vers la droite. """
    pass  # A compléter


def sierpinski(n: int) -> None:
    pass  # A compléter


# Sierpinski(n) risque de ne pas être très visible. Donc pour vérifier on pourra tracer s(3,100)
