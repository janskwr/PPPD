def __add__(self, other):
    licznik = self.licznik * other.mianownik + other.licznik * self.mianownik
    mianownk = self.mianownik * other.mianownik
    return Ulamek(licznik, mianownk)


def odwroc(self):
    self.licznik, self.mianownik = self.mianownik, self.licznik
    if self.mianownik < 0:
        (self.licznik,self.mianownik) = (-self.licznik,-self.mianownik)