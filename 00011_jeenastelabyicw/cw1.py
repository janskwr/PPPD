from math import gcd


class Ulamek:
    __slots__ = ['licznik', 'mianownik']

    def __init__(self, licznik, mianownik):
        licznik = int(licznik)
        mianownik = int(mianownik)
        if mianownik < 0:
            licznik, mianownik = -licznik, -mianownik
        nwd = abs(gcd(licznik, mianownik))
        self.licznik = licznik//nwd
        self.mianownik = mianownik//nwd
