def trace(M):
    n = len(M)
    suma = 0
    for i in range(n):
        suma += M[i][i]
    return suma
