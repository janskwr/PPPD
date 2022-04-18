#zad 3.17
def bisekcja(f, a, b, eps=10e-12, M=100):
    if a >= b:
        raise ValueError("Złe dane")
    if f(a) * f(b) > 0:
        raise ValueError("Złe dane")
    if eps <= 0:
        raise ValueError("Złe dane")
    if abs(f(a)) < eps:
        return a, True
    if abs(f(b)) < eps:
        return b, True
    lewo = a
    prawo = b
    for i in range(M):
        srodek = (lewo + prawo) / 2
        f_srodek = f(srodek)
        if f_srodek * f(lewo) < 0:
            prawo = srodek
        elif abs(f_srodek) < eps:
            return srodek, True
        else:
            lewo = srodek
    return srodek, False


print(bisekcja(lambda x: x**2 - 1, -0.5, 7.81))