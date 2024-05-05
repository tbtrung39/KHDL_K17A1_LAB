def uoc_so(n):
    uoc = []
    for i in range(1, n + 1):
        if n % i == 0:
            uoc.append(i)
    return uoc

n = int(input("Nhập số nguyên dương n: "))
if n <= 0:
    print("Vui lòng nhập số nguyên dương.")
else:
    cac_uoc = uoc_so(n)
    print("Các ước số của", n, "là:", cac_uoc)
