import random


def dom(x, a, b):
    count = [0] * (b - a + 1)
    for el in x:
        count[el - a] += 1
    maximum = max(count)
    doms = []
    for i in range(len(count)):
        if count[i] == maximum:
            doms.append(i + a)
    choice = random.randint(0, len(count) - 1)
    return doms[choice]
