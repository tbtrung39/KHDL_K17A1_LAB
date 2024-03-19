n = int(input("nhập một số nguyên dương: "))
if n <= 0:
    print("số không hợp lệ!!!")
else:
    for i in range(2, n + 1):
        for j in range(n):
            if n % i == 0:
                print(i,'', end=' ')
                n //= i
            else:
                break