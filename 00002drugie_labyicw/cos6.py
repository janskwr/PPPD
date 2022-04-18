num = int(input())
dlugosc = 1
while num != 1:
    if num % 2 == 0:
        num = num // 2
    else:
        num = 3 * num + 1
    dlugosc += 1
print(dlugosc)
