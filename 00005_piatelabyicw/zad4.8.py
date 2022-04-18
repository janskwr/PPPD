def ktynajwiekszy(t, k):
    knajwiekszych = [None for i in range(k)]
    for i in range(len(t)):
        pom = t[i]
        for j in range(k):
            if knajwiekszych[j] != None and pom > knajwiekszych[j]:
                knajwiekszych[j], pom = pom, knajwiekszych[j]
            elif knajwiekszych[j] == None:
                knajwiekszych[j] = pom
                break
    return knajwiekszych


print(ktynajwiekszy([312, 21, 21, 312, 21, 21, 4, 35, 3422432, 313], 3))
