# zad. 3.10 pp. 5

def exp(x, n):
    suma = 1
    wyraz = 1
    for i in range(n):
        wyraz *= x / (i + 1)
        suma += wyraz
    return suma


print(exp(1, 100))
print(exp(2, 100))
print(exp(2, 5))
