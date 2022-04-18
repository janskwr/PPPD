def search_pattern(x, y):
    dlugosc_x = len(x)
    dlugosc_y = len(y)
    for i in range(dlugosc_y - dlugosc_x):
        czy_dopasowano = True
        for j in range(dlugosc_x):
            if x[j] != y[i + j]:
                czy_dopasowano = False
                break
        if czy_dopasowano:
            print(i)
