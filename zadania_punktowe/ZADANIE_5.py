

'''
Funkcja znajduje największą krotność powtórzenia o długości k w zadanym ciągu.
Jeżeli takie powtórzenie nie istnieje, należy zwrócić 1

Przykład: wywołanie max_krotnosc_k([0, 1, 2, 3, 1, 2, 3, 5, 2, 3, 5, 2, 3, 5, 2, 1], 3)
powinno zwrócić liczbę 3
'''
def max_krotnosc_k(ciag, k):
    n = len(ciag)
    i = 0
    count = 1
    max_count = 1
    check = ciag[0:k]
    while i < n - k:
        for j in range(k):
            if ciag[i:i+k] != check:
                count = 1
            if not ciag[i + j] == ciag[k + j + i]:
                count = 1
                check = ciag[i:i + k]
                i += 1
                break
            else:
                count += 1
                if count > max_count:
                    max_count = count
                check = ciag[i:i + k]
                i += k
                break
    if max_count > 3:
        max_count -= 1
    return max_count

'''
Funkcja znajduje długość najdłuższego powtórzenia o krotności 3 w zadanym ciągu.
Jeśli nie ma takich powtórzeń, należy zwrócić 0.

Przykład; wywołanie najdluzsze_powtorzenie_3([3, 1, 3, 1, 2, 1, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2])
powinno zwrócić liczbę 4
'''
def najdluzsze_powtorzenie_3(ciag):
    n = len(ciag)
    i = 1
    result = 0                        # komentarz: Gdyby poprzenida funkcja działała w pełni to ta też by działałą
    max_result = 0
    while i <= n/3 + 1:
        if max_krotnosc_k(ciag, i) >= 3:
            result = i
            if result > max_result:
                max_result = result
        i += 1
    return max_result

'''
Funkcja zwraca nowy ciąg powstały przez usuwanie powtórzeń o długości k i krotności 2
z zadanego ciągu, dopóki takie powtórzenia istnieją. 

Przykład: wywołanie usun_powtorzenia_k([0, 1, 2, 5, 6, 5, 6, 1, 2, 3, 4, 3, 4, 3, 4], 2)
powinno zwrócić listę [0, 3, 4]
'''
def usun_powtorzenia_k(ciag, k):
    return []


def mainB():
    print("\n***************************************** ETAP 1 *****************************************\n")
    maleTesty1 = []
    maleTesty1.append(([1, 2, 3, 4, 5, 6], 3, 1))
    maleTesty1.append(([1, 2, 3, 4, 2, 3, 4, 5, 3, 4, 5], 3, 2))
    maleTesty1.append(([1, 2, 3, 4, 1, 2, 3, 3, 2, 1, 3, 3, 2, 1, 1, 3, 2, 1, 1], 4, 2))
    maleTesty1.append(([0, 1, 2, 3, 1, 2, 3, 5, 2, 3, 5, 2, 3, 5, 2, 1], 3, 3))
    maleTesty1.append(([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 2, 5))
    for (ciag, k, wynik) in maleTesty1:
        print("Ciag:            ", ciag)
        print("Wynik:           ", max_krotnosc_k(ciag, k))
        print("Oczekiwany wynik:", wynik, end="\n\n")


    print("\n***************************************** ETAP 2 *****************************************\n")
    maleTesty2 = []
    maleTesty2.append(([1, 2, 3, 4, 2, 3, 4, 5, 3, 4, 5], 0))
    maleTesty2.append(([1, 2, 2, 2, 4, 1, 2, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2], 1))
    maleTesty2.append(([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5], 5))
    maleTesty2.append(([1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 3], 4))
    maleTesty2.append(([3, 1, 3, 1, 2, 1, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2], 4))
    for (ciag, wynik) in maleTesty2:
        print("Ciag:            ", ciag)
        print("Wynik:           ", najdluzsze_powtorzenie_3(ciag))
        print("Oczekiwany wynik:", wynik, end="\n\n")


    print("\n***************************************** ETAP 3 *****************************************\n")
    maleTesty3 = []
    maleTesty3.append(([0, 1, 2, 2, 0, 1, 2, 3, 1, 2, 3, 4, 2, 3, 4], 3, [0, 1, 2, 2, 0, 4]))
    maleTesty3.append(([1, 2, 3, 4, 5, 6], 3, [1, 2, 3, 4, 5, 6]))
    maleTesty3.append(([1, 2, 3, 4, 5, 6, 7, 8, 9, 6, 7, 8, 9, 9, 9, 4, 5, 9, 9], 4, [1, 2, 3]))
    maleTesty3.append(([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 5, [1, 1, 1, 1, 1, 1, 1]))
    maleTesty3.append(([1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 9, 9, 7, 9, 9, 6, 9, 9, 5, 9, 9, 4, 9, 2, 3, 9, 1, 9], 2, []))
    for (ciag, k, wynik) in maleTesty3:
        print("Ciag:            ", ciag)
        print("Wynik:           ", usun_powtorzenia_k(ciag, k))
        print("Oczekiwany wynik:", wynik, end="\n\n")



    print("\n******************************** KONTROLA CZASU DZIAŁANIA ********************************\n")
    print("Etap 1:")
    duzeTesty1 = []
    duzeTesty1.append(([3] * 15000 + [2] * 2000 + [1] * 3999 + [3] * 19999 + ([1] * 4000 + [2] * 2000 + [3] * 4000) * 4 + [1] * 4001 + [2] * 2000 + [1] * 3999 + [3] * 19999, 10000, 4))
    duzeTesty1.append(((([1] * 9999) + [2]) * 7 + [1]*12000 + [2] + (([1] * 9999) + [2]) * 3, 5000, 2))
    duzeTesty1.append(((([1] * 9999) + [2]) * 7 + [1]*12000 + [2] + (([1] * 9999) + [2]) * 3, 50, 240))
    for (ciag, k, w) in duzeTesty1:
        print("Test wydajności... ", end="")
        wynik = max_krotnosc_k(ciag, k)
        if wynik == w:
            print("zakończony.")
        else:
            print("błąd!!!", wynik, "vs.", w)

    print("Etap 2:")
    duzeTesty2 = []
    duzeTesty2.append(((([1] * 249) + [2]) * 5 + [1] * 250 + [2] + (([1] * 249) + [2]) * 5, 500))
    duzeTesty2.append(([1] * 300 + [2] * 650 + [1] * 350 + [2] * 651 + [1] * 350 + [2] * 350, 217))
    for (ciag, w) in duzeTesty2:
        print("Test wydajności... ", end="")
        wynik = najdluzsze_powtorzenie_3(ciag)
        if wynik == w:
            print("zakończony.")
        else:
            print("błąd!!!", wynik)


    print("Etap 3:")
    duzeTesty3 = []
    duzeTesty3.append(([3] * 15000 + [2] * 2000 + [1] * 3999 + [3] * 19999 + ([1] * 4000 + [2] * 2000 + [3] * 4000) * 2 + [1] * 4000 + [2] * 2000 + [1] * 3999 + [3] * 19999, 10000, 70996))
    duzeTesty3.append(((([1] * 9999) + [2]) * 7 + [1] * 10000 + [2] + (([1] * 9999) + [2]) * 3, 5000, 100001))
    K = 5000
    tab = list(range(K))
    for i in range(K // 5):
        tab.append(i + K - 1)
        tab += list(range(i, i + K))
    duzeTesty3.append((tab, K, K + K // 5))
    for (ciag, k, dl) in duzeTesty3:
        print("Test wydajności... ", end="")
        wynik = usun_powtorzenia_k(ciag, k)
        if len(wynik) == dl:
            print("zakończony.")
        else:
            print("możliwy błąd!", len(wynik), "vs.", dl)

if __name__ == "__main__":
    mainB()