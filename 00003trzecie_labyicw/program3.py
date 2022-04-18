#zad 3.11

def pierwiastek(liczba, eps=1e-3):
    przyblizenie1 = 1
    przyblizenie2 = liczba
    while abs(przyblizenie2 - przyblizenie1) > eps:
        przyblizenie1 = przyblizenie2
        przyblizenie2 = (przyblizenie2 + liczba / przyblizenie2) / 2
    return przyblizenie2


print(pierwiastek(121))
