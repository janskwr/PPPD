def najdluszy_rosnacy_podciag(ciag):
    t = [1] * len(ciag)
    for i in range(1, len(ciag)):
        max_ciag = 0
        for j in range(i - 1, -1, -1):
            if ciag[i] > ciag[j] and t[max_ciag] < t[j]:
                max_ciag = j
            t[i] = t[max_ciag] + 1
    return max(t)
