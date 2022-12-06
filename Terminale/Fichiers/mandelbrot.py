# ------------------------------
#  Production d'une image de Mandelbrot
# ------------------------------------------------------------

from PIL import Image
import sys

MAX_ITERATIONS = 255

def couleur(i):
    g = int(256*i/MAX_ITERATIONS)
    return (g, g, g)

def mandelbrot(x, y):
    c1 = x + y * 1j
    c2 = 0
    for n in range(1, MAX_ITERATIONS):
        if abs(c2) > 2:
            return n
        c2 = c2 * c2 + c1
    return 0

def tracer(min_x, min_y, max_x, max_y, taille_x, taille_y):
    image = Image.new('RGB', (taille_x, taille_y))
    echelle_x = (max_x-min_x) / taille_x
    echelle_y = (max_y-min_y) / taille_y
    for image_x in range(0, taille_x-1):
        x = min_x + image_x * echelle_x
        for image_y in range(0, taille_y-1):
            y = min_y + image_y * echelle_y
            n = mandelbrot(x, y)
            image.putpixel((image_x, image_y), couleur(n))
    return image

if __name__ == "__main__":
    if len(sys.argv) != 8:
        print("usage: ./mandelbrot x_min y_min x_max y_max nb_pixel_x nb_pixel_y fichier.png")
        sys.exit(1)

    i = tracer(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]))
    i.save(sys.argv[7])