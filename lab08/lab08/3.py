def kiem_tra_so_nguyen_to(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
def in_so_nguyen_to(n):
    print("Cac so nguyen to nho hon", n, "la:")
    for num in range(2, n):
        if kiem_tra_so_nguyen_to(num):
            print(num)

n = int(input("Nhap so nguyen n: "))
in_so_nguyen_to(n)
