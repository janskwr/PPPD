def split_codes(lista_x, lista_f):
    dlugosc_list = len(lista_x)
    k = max(lista_f) + 1
    wynik = [[] for i in range(k)]
    for indeks in range(dlugosc_list):
        wartosc_f = lista_f[indeks]
        wynik[wartosc_f].append(lista_x[indeks])
    return wynik
