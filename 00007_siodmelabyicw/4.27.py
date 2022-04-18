def cykle(tab):
    pom = [False] * len(tab)
    licznik = 0
    for i in range(len(tab)):
        if not pom[i]:
            curr = i
            while not pom[curr]:
                pom[curr] = True
                curr = tab[curr]
            licznik += 1
    return licznik
