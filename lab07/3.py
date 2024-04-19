import random
A = set()
n = input("Nhap so luong phan tu: ")
while n.isalpha() == True:
    n = input("Gia tri khong hop le, vui long nhap lai: ")
while n <= "0":
    n = input("Gia tri khong hop le, vui long nhap lai:")
while int(len(A)) <int(n):
    A.add(random.random())
print("Tap hop A la: ", A)
phan_tu_max = max(A)
phan_tu_min = min(A)
tong = sum(A)
print("Phan tu lon nhat cua tap hop A la: ", phan_tu_max)
print("Phan tu nho nhat cua tap hop A la: ",phan_tu_min)
print("Tong cac phan tu cua tap hop A la: ", tong)