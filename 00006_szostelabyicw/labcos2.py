def permutacja_sortujaca_zapetlona(lista, permutacja):
    length = len(lista)
    for i in range(length):
        is_sorted = True
        for j in range(length - 1):
            if lista[permutacja[(i + j) % length]] > lista[permutacja[(i + j + 1) % length]]:
                is_sorted = False
                break
        if is_sorted:
            return i
    return -1


def main():
    lista = [20, 10, 30, 50, 40]
    permutacja = [4, 3, 1, 0, 2]   # [40, 50, 10, 20, 30]
    print(permutacja_sortujaca_zapetlona(lista, permutacja))


if __name__ == '__main__':
    main()
