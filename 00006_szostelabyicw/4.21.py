def horner(x, w):
    wynik = x[len(w) - 1]
    for i in range(len(w) - 2, -1, -1):
        wynik = wynik * x + w[i]
    return wynik
