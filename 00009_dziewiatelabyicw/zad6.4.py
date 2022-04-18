import math


def trim_nan(t):
    n = len(t)
    i = 0
    wynik = []
    while i < n and math.isnan(t[i]):
        i += 1
    j = n - 1
    while j >= 0 and math.isnan(t[j]):
        j -= 1
    for k in range(i, j + 1):
        wynik.append(t[k])
    return wynik
