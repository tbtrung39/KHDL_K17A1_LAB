def uoc_so(n):
    print("Cac uoc so cua", n, "la:")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)
n = int(input("Nhap so n: "))
uoc_so(n)
