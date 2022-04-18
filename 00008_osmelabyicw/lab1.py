def czy_macierz(macierz):
    if type(macierz) is not list:
        return False
    for i in range(len(macierz)):
        if type(macierz) is not list:
            return False
    columns = len(macierz[0])
    rows = len(macierz)
    for i in range(1, rows):
        if columns != len(macierz[i]):
            return False
    return True


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(czy_macierz(matrix))
