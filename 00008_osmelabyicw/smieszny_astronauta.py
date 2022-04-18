import numpy
import copy
from PIL import Image


def png_read(filepath):
    img = Image.open(filepath)
    assert len(img.size) == 2  # skala szarosci, nie RGB
    return (numpy.array(img) / 255).reshape(img.size[1], img.size[0]).tolist()


def png_write(img, filepath):
    img = Image.fromarray((numpy.array(img) * 255).astype(numpy.int8), 'L')
    img.save(filepath)


def min_max(macierz):
    wiersze = len(macierz)
    kolumny = len(macierz[0])
    minimum = macierz[0][0]
    maximum = macierz[0][0]
    for wiersz in range(wiersze):
        for kolumna in range(kolumny):
            minimum = min(macierz[wiersz][kolumna], minimum)
            maximum = max(macierz[wiersz][kolumna], maximum)
    return minimum, maximum


def rozjasnij_obrazek(obrazek, v):
    wiersze = len(obrazek)
    kolumny = len(obrazek[0])
    wynik = copy.deepcopy(obrazek)
    for wiersz in range(wiersze):
        for kolumna in range(kolumny):
            wynik[wiersz][kolumna] += v
            wynik[wiersz][kolumna] = max(min(wynik[wiersz][kolumna], 1), 0)
    return wynik


def negatyw(obrazek):
    wiersze = len(obrazek)
    kolumny = len(obrazek[0])
    nowy_obrazek = copy.deepcopy(obrazek)
    for wiersz in range(wiersze):
        for kolumna in range(kolumny):
            nowy_obrazek[wiersz][kolumna] = 1.0 - obrazek[wiersz][kolumna]
    return nowy_obrazek


def bialoczarny(obrazek, prog):
    wiersze = len(obrazek)
    kolumny = len(obrazek[0])
    nowy_obrazek = copy.deepcopy(obrazek)
    for wiersz in range(wiersze):
        for kolumna in range(kolumny):
            nowy_obrazek[wiersz][kolumna] = 1.0 if obrazek[wiersz][kolumna] >= prog else 0
    return nowy_obrazek


obrazek = png_read("skimage_astronaut.png")
#print(min_max(obrazek))
#png_write(rozjasnij_obrazek(obrazek, 0.4), "rozjasniony_obrazek_essa.png")
#png_write(negatyw(obrazek), "negatyw_astro.png")
png_write(bialoczarny(obrazek, 0.5), "czarnobialy_astro.png")
