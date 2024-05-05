def la_so_nguyen_to(so):
    if so <= 1:
        return False
    for i in range(2, int(so**0.5) + 1):
        if so % i == 0:
            return False
    return True
def in_so_nguyen_to(n):
    print("cac so nguyen to nho hon", n, "la:")
    for num in range(2, n):
        if la_so_nguyen_to(num):
            print(num, end=" ")
n=int(input("nhap so nguyen n:"))
in_so_nguyen_to(n)
