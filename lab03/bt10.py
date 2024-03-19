n = int(input("Nhập số nguyên dương: "))
print("Thừa số nguyên tố của số nguyên dương: ",end="")
for i in range(2,n+1):
    while i <= n:
        if n % i == 0:
            print(i, end="")
            n //= i
            if n > 1:
                print('*', end="")
            i = 1
        i += 1