def rm_dup(x):
    n = len(x)
    nowa_lista = []
    for i in range(n - 1):
        if x[i] != x[i + 1]:
            nowa_lista.append(x[i])
    if n != 0:
        nowa_lista.append(x[n-1])
    return nowa_lista
