# 3
def kiem_tra_so_nguyen_to(x):
    if x<=1:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True
# in ra cac so nguyen to
def in_cac_so_nguyen_to(n):
    print("cac so nguyen to la:",n)
    for i in range(2,n):
        if kiem_tra_so_nguyen_to(i):
            print(i)
n=int(input("nhap n"))
in_cac_so_nguyen_to(n)
