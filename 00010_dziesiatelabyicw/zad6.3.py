def rep_each(lista, k):
    n = len(lista)
    wynik = [0 for _ in range(k*n)]
    for i in range(n):
        for j in range(k):
            wynik[i*k+j] = lista[i]
    return wynik


cos = [1, 2, 3]
print(rep_each(cos, 3))
