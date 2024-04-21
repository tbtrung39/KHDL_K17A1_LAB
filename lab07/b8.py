def is_real_number(s):
    if float(s):
        return True
    else:
        return False
A=set()
while True:
    n= input("nhap vao phan tu A (nhan ESC de thoat): ")
    if n == "ESC":
        break
    A.add(n)
so_nguyen = 0
so_thuc =0
ki_tu = 0
for i in A:
    if i.isdigit():
        so_nguyen +=1
    elif i.isalpha():
        ki_tu+=1
    elif is_real_number(i):
        so_thuc+=1
print("phan tu la so nguyen la:",so_nguyen)
print("phan tu la so thuc la:",so_thuc)
print("phan tu la ki tu la:",ki_tu)