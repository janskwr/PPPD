import sys

def main():
    waga = float(input("Podaj wagę."))
    wzrost = int(input("Podaj wzrost."))

    if waga < 0:
        sys.exit()

    if wzrost < 0:
        sys.exit()

    bmi = waga / (wzrost / 100 * wzrost / 100)

    if bmi <= 18.5:
        print("niedowaga")
    elif bmi <= 25:
        print("waga prawidłowa")
    elif bmi <= 30:
        print("nadwaga")
    else:
        print("otyłość")

    # Zadanie 1.04 o BMI


if __name__ == '__main__':
    main()
