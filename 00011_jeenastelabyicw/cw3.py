def __sub__(self, other):
    licznik = self.licznik*other.mianownik - other.licznik*self.mianownik
    mianownk = self.mianownik*other.mianownik
    return Ulamek(licznik, mianownk)


def __le__(self, other):
    roznica = self - other
    return roznica.licznik <= 0