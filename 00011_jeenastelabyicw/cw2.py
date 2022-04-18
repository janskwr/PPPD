import math


class Ulamek():
    __slots__ = ["licznik","mianownik"]

    def __init__(self,licznik,mianownik):
        d = math.gcd(licznik,mianownik)
        self.licznik = licznik//d
        self.mianownik = mianownik//d
        if mianownik < 0:
            (self.licznik,self.mianownik) = (-self.licznik,-self.mianownik)

    def __mul__(self,other):
        if type(other) is int:
            return Ulamek(self.licznik*other,self.mianownik)
        else:
            return Ulamek(self.licznik*other.licznik,self.mianownik*other.mianownik)

    def __rmul__(self,other):
        return self*other

    def __repr__(self):
        return f"Ulamek(licznik={self.licznik},mianownik={self.mianownik})"

    def __str__(self):
        return f"{self.licznik}/{self.mianownik}"