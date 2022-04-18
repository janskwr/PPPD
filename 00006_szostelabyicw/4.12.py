def add_vectorized(x, y):
    dlugosc = max(len(x), len(y))
    lista = [None for i in range(dlugosc)]
    for i in range(dlugosc):
        lista[i] = x[i%len(x)] + y[i%len(y)]
    return lista


