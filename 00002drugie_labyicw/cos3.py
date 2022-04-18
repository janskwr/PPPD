lower = int(input())
upper = int(input())
primes = [True] * (upper + 1)
for i in range(2, upper + 1):
    if primes[i]:
        for j in  range(i + i, upper + 1, i):
            primes[j] = False

for i in range(lower, upper + 1):
    if primes[i]:
        print(i)
