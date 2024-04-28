def find_divisor(n):
    divisor = []
    for i in range(1,n+1):
        if n % i == 0:
            divisor.append(i)
    return divisor
n = int(input("nhap vao so nguyen n: "))
find_divisor(n)
print(f"cac uoc so cua so {n} la {find_divisor(n)}")




