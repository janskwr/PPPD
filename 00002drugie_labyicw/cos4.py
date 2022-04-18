num = int(input())
x = int(input())
counter = 0
while num > 0:
    if num % 10 == x:
        counter += 1
    num = num // 10
print(counter)
