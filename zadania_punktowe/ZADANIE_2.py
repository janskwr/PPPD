import random


def wypisz_akcje():
    print("Co chcesz zrobić?")
    print("1 - skok")
    print("2 - mucha")
    print("3 - atak")


def wybor_akcji():
    action = int(input())
    if action < 1 or action > 3:
        raise ValueError("Podano zły numer!")
    if action == 1 or action == 2 or action == 3:
        return action


def skok():
    if random.uniform(0, 1) < 0.6:
        jump = 2
    else:
        jump = 4
    return jump


def atak():
    back = 0
    if random.uniform(0, 1) < 0.7:
        back = random.randint(1, 5)
    return back


def mucha():
    if random.uniform(0, 1) < 0.5:
        return True
    else:
        return False


def main():
    random.seed(2020)
    frog1 = 0
    frog2 = 0
    boost1 = 0
    boost2 = 0
    while frog1 < 30 and frog2 < 30:
        print("Ruch żaby 1.")
        wypisz_akcje()
        action1 = wybor_akcji()
        if action1 == 1:
            jumped1 = skok()
            if boost1 == 1:
                frog1 += 3 * jumped1
                print(f"Żaba skoczyła o {jumped1 * 3} pól/pola.")
            else:
                frog1 += jumped1
                print(f"Żaba skoczyła o {jumped1} pól/pola.")
            boost1 = 0
        elif action1 == 2:
            lunch1 = mucha()
            if lunch1:
                print("Żaba zjadła muchę")
                boost1 = 1
            else:
                print("Żaba nie zjadła muchy")
                boost1 = 0
        elif action1 == 3:
            back1 = atak()
            frog2 -= back1
            if back1 == 0:
                print("Atak nie powiódł się.")
            else:
                print(f"Atak powiódł się, przeciwnik cofnął się o {back1} pól.")
            if frog2 < 0:
                frog2 = 0
            boost1 = 0
        print(f"Pozycja żaby 1: {frog1}")
        print(f"Pozycja żaby 2: {frog2}")
        print("Ruch żaby 2.")
        wypisz_akcje()
        action2 = wybor_akcji()
        if action2 == 1:
            jumped2 = skok()
            if boost2 == 1:
                frog2 += 3 * jumped2
                print(f"Żaba skoczyła o {jumped2 * 3} pól/pola.")
            else:
                frog2 += jumped2
                print(f"Żaba skoczyła o {jumped2} pól/pola.")
            boost2 = 0
        elif action2 == 2:
            lunch2 = mucha()
            if lunch2:
                print("Żaba zjadła muchę")
                boost2 = 1
            else:
                print("Żaba nie zjadła muchy")
                boost2 = 0
        elif action2 == 3:
            back2 = atak()
            frog1 -= back2
            if back2 == 0:
                print("Atak nie powiódł się.")
            else:
                print(f"Atak powiódł się, przeciwnik cofnął się o {back2} pól.")
            if frog1 < 0:
                frog1 = 0
            boost2 = 0
            print(f"Pozycja żaby 1: {frog1}")
            print(f"Pozycja żaby 2: {frog2}")
        with open("file1234.txt", "a") as file:
            if action1 == 1:
                file.write("Żaba 1 wybór: skok. Ruch: " + str(jumped1))
                file.write("\n")
            elif action1 == 2:
                file.write("Żaba 1 wybór: złapanie muchy. Udało się: " + str(lunch1))
                file.write("\n")
            elif action1 == 3:
                file.write("Żaba 1 wybór: atak. Przeciwnik cofnął się o: " + str(back1))
                file.write("\n")
            file.write("Pozycja żaby 1: " + str(frog1))
            file.write("\n")
            file.write("Pozycja żaby 2: " + str(frog2))
            file.write("\n")
            if action2 == 1:
                file.write("Żaba 2 wybór: skok. Ruch: " + str(jumped2))
                file.write("\n")
            elif action2 == 2:
                file.write("Żaba 2 wybór: złapanie muchy. Udało się: " + str(lunch2))
                file.write("\n")
            elif action2 == 3:
                file.write("Żaba 2 wybór: atak. Przeciwnik cofnął się o: " + str(back2))
                file.write("\n")
            file.write("Pozycja żaby 1: " + str(frog1))
            file.write("\n")
            file.write("Pozycja żaby 2: " + str(frog2))
            file.write("\n")
    if frog1 > frog2:
        print("WYGRYWA ŻABA 1")
    elif frog2 > frog1:
        print("WYGRYWA ŻABA 2")
    elif frog2 == frog1:
        print("REMIS")


if __name__ == '__main__':
    main()
