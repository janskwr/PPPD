def generuj(lista, liczba_jedynek, index_start=0):
    if liczba_jedynek == 0:
        print(lista)
    else:
        for i in range(index_start, len(lista) - liczba_jedynek + 1):
            lista[i] = 1
            generuj(lista, liczba_jedynek - 1, i + 1)
            lista[i] = 0


def main():
    n = 100
    k = 15
    lista = [0] * n
    generuj(lista, k)


if __name__ == '__main__':
    main()
