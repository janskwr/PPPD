import sys

def main():
    stairs = int(input("Podaj liczbe schodow, ktore pokonales"))

    if stairs < 0 or stairs > 300:
        print("Schody poza zakresem")
        sys.exit()

    pietro_pod = stairs // 15
    pietro_nad = pietro_pod + 1

    if stairs % 15 == 0:
        print("Jestes na " + str(stairs / 15) + " pietrze.")
        if (stairs / 15) % 2 == 0:
            print("Masz 0 schodkow do toalety.")
        else:
            print("Musisz pokonac 15 schodkow w gore albo w dol do najblizszej toalety.")
    else:
        print("Jestes pomiedzy " + str(pietro_pod) + ", a " + str(pietro_nad) + " pietrem.")
        if pietro_pod % 2 == 0:
            print("Musisz pokonac " + str(stairs % 15) + " schodkow w dol do najblizszej toalety.")
        else:
            print("Musisz pokonac " + str(15 -(stairs % 15)) + " schodkow w gore do najblizszej toalety.")


if __name__ == '__main__':
    main()
