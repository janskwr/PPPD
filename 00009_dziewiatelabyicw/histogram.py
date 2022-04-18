import math


def histogram(x):
    najmniejsza = x[0]
    najwieksza = x[0]
    for cos in x:
        najmniejsza = min(cos, najmniejsza)
        najwieksza = max(cos, najwieksza)
    # ptrmax1 = math.modf(najwieksza)[0]
    ptrmax2 = math.modf(round(najwieksza, 1)[1]
    # ptrmin1 = math.modf(najmniejsza)[0]
    ptrmin2 = math.modf(round(najmniejsza, 1))[1]
    elementy = [[] for _ in range(int(ptrmax2 - ptrmin2 + 1))]





def main():
    test = math.modf(2.6)
    print(test)

if __name__ == '__main__':
    main()