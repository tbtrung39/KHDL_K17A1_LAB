def kiem_tra_so_nguyen_to(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def in_so_nguyen_to(n):
    so_nguyen_to = []
    for num in range(2, n):
        if kiem_tra_so_nguyen_to(num):
            so_nguyen_to.append(num)
    return so_nguyen_to

n = int(input("Nhập một số nguyên dương n: "))
so = in_so_nguyen_to(n)
print(so)