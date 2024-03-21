n=int(input("nhap so tu nhien n: "))
if n<0:
    print("vui long nhap lai!!!")
else:
    tong=0
    while n>0:
        chu_so_cuoi=n%10
        tong=tong+chu_so_cuoi
        n//=10
    print("tong cac so cua n =", tong)