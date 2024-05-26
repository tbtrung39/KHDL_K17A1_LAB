def uoc_n(n):
    return [i for i in range(1, n+1) if n % i == 0]
n = int(input("Nhập số nguyên dương n: "))
print("Các ước số của", n, "là:",uoc_n(n))