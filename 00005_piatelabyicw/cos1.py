def f(lista):
    maksimum = lista[0]
    minimum = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > maksimum:
            maksimum = lista[i]
        if lista[i] < minimum:
            minimum = lista[i]
    return minimum, maksimum


print(f([2, 10, 2, 123, 2, 1]))
