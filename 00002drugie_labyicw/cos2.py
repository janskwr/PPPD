from math import sqrt


num = int(input("Podaj liczbę naturalną."))
is_prime = True
for i in range(2, int(sqrt(num))):
    if num % i == 0:
        is_prime = False
        break

if is_prime:
    print(str(num) + " jest liczbą pierwszą.")
else:
    print(str(num) + " nie jest liczbą pierwszą.")
