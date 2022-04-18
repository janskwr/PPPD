import random


def wypisz_macierz(matrix):
    print(" ", end=" ")
    for column in range(len(matrix[0])):
        if column < 10:
            print(column, end=" ")
        else:
            print(chr(ord("A") + column - 10), end=" ")
    print()
    for row in range(len(matrix)):
        if row < 10:
            print(row, end=" ")
        else:
            print(chr(ord("A") + row - 10), end=" ")
        for column in range(len(matrix[row])):
            print(f'{matrix[row][column]}', end=" ")
        print()
    print()


def losuj_ruch(plansza, gracz):
    liczba_wierszy = len(plansza)
    liczba_kolumn = len(plansza[0])
    random.seed(123)
    is_taken = False
    while not is_taken:
        random_row = random.randint(0, liczba_wierszy - 1)
        random_column = random.randint(0, liczba_kolumn - 1)
        if plansza[random_row][random_column] == 0:
            plansza[random_row][random_column] = gracz
            is_taken = True


def czy_remis(plansza):
    liczba_wierszy = len(plansza)
    liczba_kolumn = len(plansza[0])
    for wiersz in range(liczba_wierszy):
        for kolumna in range(liczba_kolumn):
            if plansza[wiersz][kolumna] == 0:
                return False
    return True


def czy_wygrana(plansza, ile_pod_rzad):
    liczba_wierszy = len(plansza)
    liczba_kolumn = len(plansza[0])
    for wiersz in range(liczba_wierszy):
        counter1 = 0
        counter2 = 0
        for kolumna in range(liczba_kolumn):
            if plansza[wiersz][kolumna] == 1:
                counter2 = 0
                counter1 += 1
                if counter1 == ile_pod_rzad:
                    return 1
            elif plansza[wiersz][kolumna] == 2:
                counter1 = 0
                counter2 += 1
                if counter2 == ile_pod_rzad:
                    return 2
            else:
                counter1 = 0
                counter2 = 0
    for kolumna in range(liczba_kolumn):
        counter1 = 0
        counter2 = 0
        for wiersz in range(liczba_wierszy):
            if plansza[wiersz][kolumna] == 1:
                counter2 = 0
                counter1 += 1
                if counter1 == ile_pod_rzad:
                    return 1
            elif plansza[wiersz][kolumna] == 2:
                counter1 = 0
                counter2 += 1
                if counter2 == ile_pod_rzad:
                    return 2
            else:
                counter1 = 0
                counter2 = 0
    if czy_remis(plansza):
        return 3
    return 0



def main():
    plansza = [[0] * 15 for i in range(10)]
    player1 = 1
    player2 = 2
    losuj_ruch(plansza, player1)
    losuj_ruch(plansza, player2)
    losuj_ruch(plansza, player1)
    turn = player2
    wypisz_macierz(plansza)
    while not czy_remis(plansza):
        losuj_ruch(plansza, turn)
        if turn == player2:
            turn = player1
        else:
            turn = player2
    nowa_plansza = [[0] * 15 for i in range(10)]
    losuj_ruch(nowa_plansza, player1)
    losuj_ruch(nowa_plansza, player2)
    losuj_ruch(nowa_plansza, player1)
    new_turn = player2
    while czy_wygrana(nowa_plansza, 5) == 0:
        losuj_ruch(nowa_plansza, new_turn)
        if new_turn == player2:
            new_turn = player1
        else:
            new_turn = player2
    wypisz_macierz(nowa_plansza)
    result = czy_wygrana(nowa_plansza, 5)
    if result == 1:
        print("WYGRAŁ GRACZ 1")
    elif result == 2:
        print("WYGRAŁ GRACZ 2")
    else:
        print("REMIS")


if __name__ == '__main__':
    main()
