def find_divisor(n):
    divisor = []
    for i in range(1,n+1):
        if n % i == 0:
            divisor.append(i)
    return divisor
n = int(input("nhập vào số nguyên n: "))
find_divisor(n)
print(f"các ước số của số {n} là {find_divisor(n)}")