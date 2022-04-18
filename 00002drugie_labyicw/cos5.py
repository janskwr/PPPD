num = int(input())
num_reversed = 0
while num > 0:
    num_reversed = num_reversed * 10 + (num % 10)
    num = num // 10
print(num_reversed)
