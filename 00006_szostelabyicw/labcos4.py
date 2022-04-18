def nastepny_wiersz_pascal(wiersz):
    length = len(wiersz)
    next_row = [0] * (length + 1)
    next_row[0] = wiersz[0]
    next_row[length] = wiersz[length - 1]
    for i in range(1, length):
        next_row[i] = wiersz[i - 1] + wiersz[i]
    return next_row


def n_ty_wiersz_pascala(n, a=1, b=1, c=1):
    if n == 1:
        return [a]
    wiersz = [b, c]
    for i in range(n - 2):
        wiersz = nastepny_wiersz_pascal(wiersz)
    return wiersz


def main():
    pass #główna funkcja


if __name__ == '__main__':
    main()
