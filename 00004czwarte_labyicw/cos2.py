#zad 3.19
import random


def calkaMonteCarlo(a, b, f, M=1000):
    if b <= a:
        raise ValueError("Błędne dane!")
    sukces = 0
    for i in range(M):
        x = random.uniform(a, b)
        y = random.uniform(0, f(b))
        if y <= f(x):
            sukces += 1
    return sukces/M * abs(a-b) * f(b)


print(calkaMonteCarlo(1, 2, lambda x: x**2))
print(calkaMonteCarlo(1, 2, lambda x: x**2, M=10000))
