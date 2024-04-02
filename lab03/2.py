n = int(input("Nhập số n: "))
for i in range(1, n):
    sum = 0
    for i in range(1, i):
        if i % i == 0:
            sum += i
print(f" số hoàn hảo nhỏ hơn {n} là:",i)