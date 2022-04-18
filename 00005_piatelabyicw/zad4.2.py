import random


def mieszaj(lista):
    for i in range(len(lista)):
        j = random.randint(i, len(lista) - 1)
        lista[i], lista[j] = lista[j], lista[i]


a = [1, 2, 3, 4]
mieszaj(a)
print(a)
