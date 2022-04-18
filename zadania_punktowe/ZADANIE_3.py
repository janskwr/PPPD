import random
import math
import copy


def wygeneruj_prosta_sciezke(n):
    sciezka = [0] * n
    for i in range(n):
        sciezka[i] = i
    return sciezka
    """
    Zwraca n-elementową listę [0,1,2,3,...,n-1]
    :param n: długość listy
    :return: lista
    """
    #pass


def wygeneruj_miasta_B(n, min_x=-10, max_x=10, min_y=-10, max_y=10):
    towns = [0] * n
    for i in range(n):
        tup = (random.uniform(min_x, max_x), random.uniform(min_y, max_y))
        towns[i] = tup
    return towns
    """
    Generuje listę krotek (pierwszy element krotki to współrzędna x, a drugi element krotki to współrzędna y)
    reprezentujące współrzędne miast.
    Współrzędne miast są losowane z rozkładu jednostajnego U[min_x, max_x] dla współrzędnych x oraz U[min_y, max_y]
    dla współrzędnych y.
    :param n: liczba miast
    :param min_x: minimalna współrzędna x
    :param max_x: maksymalna współrzędna x
    :param min_y: minimalna współrzędna y
    :param max_y: maksymalna współrzędna y
    :return: n-elementowa lista krotek dwuelementowych
    """
    #pass


def oblicz_dlugosc_sciezki_B(miasta, sciezka):
    dlugosc_cyklu = 0
    x = [x[0] for x in miasta]
    y = [y[1] for y in miasta]
    for i in range(len(sciezka) - 1):
        dlugosc_cyklu += math.sqrt((((x[sciezka[i + 1]]) - (x[sciezka[i]]))**2) + (((y[sciezka[i + 1]]) - (y[sciezka[i]]))**2))
    dlugosc_cyklu += math.sqrt((((x[sciezka[0]]) - (x[sciezka[len(sciezka) - 1]]))**2) + (((y[sciezka[0]]) - (y[sciezka[len(sciezka) - 1]]))**2))
    return dlugosc_cyklu
    """
    Dla zadanej listy indeksów miast oblicz długość cyklu. Wyjaśnijmy: pomimo nazwy parametru "sciezka" mamy na myśli
    cykl: z ostatniego miasta przechodzimy z powrotem do pierwszego (zerowego).
    :param miasta: lista współrzędnych miast
    :param sciezka: lista indeksów miast, zgodnie z którą przemieszczamy się od miasta do miasta. Z ostatniego miasta
    przechodzimy z powrotem do pierwszego (zerowego).
    :return: pojedyncza liczba typu float oznaczająca długość cyklu
    """
    #pass


def mutuj_B(sciezka, k=3):
    temp = random.sample(sciezka, k)
    nowa_sciezka = sciezka.copy()
    for x in range(k):
        for i in range(len(nowa_sciezka)):
            if nowa_sciezka[i] == temp[x]:
                if i == len(nowa_sciezka) - 1:
                    nowa_sciezka[i], nowa_sciezka[0] = nowa_sciezka[0], nowa_sciezka[i]
                else:
                    nowa_sciezka[i], nowa_sciezka[(i + 1)] = nowa_sciezka[(i + 1)], nowa_sciezka[i]
    return nowa_sciezka
    """
    Funkcja mutuje podaną listę indeksów. Funkcja nie modyfikuje argumentów wejściowych. Funkcja zwraca zmodyfikowaną kopię.
    Funkcja działa w sposób następujący: losowane jest k indeksów listy bez zwracania. Następnie dla każdego indeksu i
    zamieniane miejscami (swapowane) są indeksy i oraz i+1 z zawijaniem.
    Przykładowo, jeśli lista to [1,11,2,3,22,4,5,33], a wylosowane indeksy to [1,4,7] (dwucyfrowe elementy
    z listy) to wynikowa ścieżka powinna być równa [33,2,11,3,4,22,5,1].
    Można (należy) użyć random.sample().
    :param sciezka: Lista indeksów, którą należy zmutować.
    :param k: Liczba indeksów do wylosowania (domyślnie równy 3)
    :return: Zmutowana kopia ścieżki
    """
    #pass


def krzyzuj_B(sciezka1, sciezka2):
    key = random.randint(1, len(sciezka1) - 1)
    sciezka3 = sciezka1.copy()
    ptr = key
    ptr2 = key
    for x in range(key):
        sciezka3[x] = sciezka1[ptr - 1]
        ptr -= 1
    for i in range(key, len(sciezka1)):
        for y in range(len(sciezka1)):
            if sciezka2[y] not in [sciezka3]:
                sciezka2[ptr2] = sciezka1[y]
                ptr2 += 1
    return sciezka3
    """
    Funkcja dokonuje krzyżowania dwóch ścieżek. Krzyżowanie polega na wylosowaniu pewnego indeksu z zakresu {1, 2,..., n-2}
    (gdzie n to długość jednej ścieżki), a następnie przepisanie elementów ze ścieżki 1 do dziecka od zera do wylosowanego indeksu
    z odwróceniem kolejności.
    Reszta indeksów miast powinna zostać wpisana w pozostałe miejsca zgodnie z kolejnością występowania na sciezka2.
    Przykładowo, jeśli sciezka1=[0,1,2,3,4,5,6], a sciezka2=[6,5,4,3,2,1,0], a wylosowany index=3, to dziecko powinno mieć
    postać [2,1,0,6,5,4,3].
    :param sciezka1: lista indeksów miast
    :param sciezka2: lista indeksów miast
    :return: lista indeksów miast
    """
    #pass


def znajdz_rozwiazanie_optymalne_B(miasta):
    """
    Znajduje rozwiązanie optymalne problemu komiwojażera poprzez rozpatrzenie wszystkich permutacji miast.
    :param miasta: lista współrzędnych miast
    :return: krotka, której pierwszym elementem jest optymalna długość cyklu, a drugim optymalna lista indeksów miast
    """
    pass


def main_B():
    random.seed(321)
    n = 7
    min_x, max_x, min_y, max_y = -5, 4, -4, 5

    # etap 1
    print("0. Generujemy miasta")
    miasta = wygeneruj_miasta_B(n, min_x, max_x, min_y, max_y)
    print(miasta)

    print("\n\n1. Szukamy prostą mutacją")
    sciezka = wygeneruj_prosta_sciezke(n)
    print(f"Prosta sciezka: {sciezka}")
    best_sciezka = sciezka
    best_wartosc = oblicz_dlugosc_sciezki_B(miasta, sciezka)
    print(f"Dla prostej ścieżki długość ścieżki to: {best_wartosc}")

    print(f"mutuj_B([0,1,2,3,4,5,6], 3) = {mutuj_B([0, 1, 2, 3, 4, 5, 6], 3)}")
    print(f"mutuj_B([0,1,2,3,4,5,6], 4) = {mutuj_B([0, 1, 2, 3, 4, 5, 6], 4)}")
    print(f"mutuj_B([0,1,2,3,4,5,6], 5) = {mutuj_B([0, 1, 2, 3, 4, 5, 6], 5)}")

    # [TO UZUPELNIJ]
    # 100 razy wykonaj:
    # mutację aktualnie najlepszej ścieżki
    # sprawdzenie, czy zmutowana ścieżka daje krótszy (lepszy) cykl
    # jeśli tak, zapisz lepszy wynik w zmiennych best_sciezka, best_wartosc
    for i in range(100):
        x = mutuj_B(sciezka)
        cos = oblicz_dlugosc_sciezki_B(miasta, x)
        if cos < best_sciezka:
            best_sciezka = x
            best_wartosc = cos


    print(f"Po mutacjach długość ścieżki {best_sciezka} to: {best_wartosc}")

    print("\n\n2. Szukamy przez krzyzowanie")

    sciezka1 = mutuj_B(wygeneruj_prosta_sciezke(n), n - 2)
    sciezka2 = mutuj_B(wygeneruj_prosta_sciezke(n), n - 2)
    wartosc1 = oblicz_dlugosc_sciezki_B(miasta, sciezka1)
    wartosc2 = oblicz_dlugosc_sciezki_B(miasta, sciezka2)

    # [TO UZUPELNIJ]
    # Nasza populacja składa się ze sciezka1 i sciezka2
    # Powtórz 1000 razy:
    # skrzyżuj ścieżkę1 i ścieżkę2
    # otrzymane w ten sposób dziecko zmutuj (k domyślne)
    # oblicz długość cyklu dla dziecka
    # pozostaw w zmiennych sciezka1, wartosc1 i sciezka2, wartosc2 wartosci odpowiadajace dwóm najlepszym wynikom z trzech możliwych (sciezka1, sciezka2, dziecko)
    # Podpowiedz: uzyj mechanizmu jak przy sortowaniu przez wstawianie.

    print(f"\n\nPo krzyżowaniu długość ścieżki {sciezka1} to: {wartosc1}")

    # etap 5:
    optymalne = znajdz_rozwiazanie_optymalne_B(miasta)
    print(f"\n\n3. Optymalny wynik to {optymalne}")


if __name__ == "__main__":
    main_B()
