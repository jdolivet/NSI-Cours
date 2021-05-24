def filtre_supprime_rouge(img1):
    """ Entree : PIL.Image
    Sortie : PIL.Image """
    img2 = img1.copy()
    pimg1 = img1.load()
    pimg2 = img2.load()
    for i in range(img2.size[0]):
        for j in range(img2.size[1]):
            (r, v, b) = pimg1[i, j]
            pimg2[i, j] = (0, v, b)
    return img2