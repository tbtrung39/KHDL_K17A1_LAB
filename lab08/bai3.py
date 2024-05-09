
def la_so_nguyen_to(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
           print("x không phải sô nguyên tố")
           return False
    print("x là số nguyên tố")
    return True
x = int(input("nhập số x:"))
print(la_so_nguyen_to(x))