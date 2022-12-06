# ------------------------------
#  Coller quatre images (de Mandelbrot)
# ------------------------------------------------------------

from PIL import Image
import sys

if __name__=="__main__":
    if len(sys.argv) != 6:
        print("usage: coller.py image1.png image2.png image3.png image4.png collage.png")
        sys.exit(1)

    i1 = Image.open(sys.argv[1])
    i2 = Image.open(sys.argv[2])
    i3 = Image.open(sys.argv[3])
    i4 = Image.open(sys.argv[4])

    w = i1.size[0]
    h = i1.size[1]
    w += max(i2.size[0], i3.size[0], i4.size[0])
    h += max(i2.size[1], i3.size[1], i4.size[1])

    res = Image.new('RGB', (w, h))

    res.paste(i1, (0, 0))
    res.paste(i2, (i1.size[0], 0))
    res.paste(i3, (0, i1.size[1]))
    res.paste(i4, (i1.size[0], i1.size[1]))
    res.save(sys.argv[5])