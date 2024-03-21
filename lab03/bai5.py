n = int(input("Nhap vao mot so nguyen n:"))
tong = 0
for i in range(1,n+1):
    tong += i**3
    print("Tong cua n so nguyen to la:",tong)