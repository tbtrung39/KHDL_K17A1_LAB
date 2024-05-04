def tinh_luong(a,b,c):
    luong=a/b*c
    return luong
a=float(input("moi nhap luong luc vao"))
b=float(input("moi nhap luong trong luc lam"))
c=float(input("moi nhap luong luc nghi"))
ho_ten=input("nhap ten")
luong_thang=tinh_luong(a,b,c)
print("ten nv la:",ho_ten)
print("luong cua nv la:",luong_thang)