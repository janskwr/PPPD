def czy_permutacja_sortujaca(lista, permutacja):
    for i in range(len(lista) - 1):
        if lista[permutacja[i]] > lista[permutacja[i + 1]]:
            return False
    return True


def main():
    lista = [20, 10, 30, 50, 40]
    permutacja = [1, 0, 2, 4, 3]
    print(czy_permutacja_sortujaca(lista, permutacja))


if __name__ == '__main__':
    main()
