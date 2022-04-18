# zad. 3.9

def oblicz_e(eps=1e-9):
    suma = 2.5
    wyraz = 0.5
    poprzedni_wyraz = 1
    k = 3
    while abs(wyraz - poprzedni_wyraz) >= eps:
        poprzedni_wyraz = wyraz
        wyraz /= k
        suma += wyraz
        k += 1
    return suma

print(oblicz_e())