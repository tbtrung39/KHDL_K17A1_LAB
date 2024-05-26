import sys
sys.path.append("lab10\bai10\hinhhoc")
from hinhhoc import is_tamgiac,chu_vi_hinh_vuong,ChuViTamGiac,dien_tich_hinh_vuong,S_tam_giac
a = float(input("nhap a: "))
b = float(input("nhap b: "))
c = float(input("nhap c: "))
print("day co phai la 3 canh tam giac: ",is_tamgiac(a,b,c))
print("chu vi tam giac = ",ChuViTamGiac(a,b,c))
print("dien tich tam giac =",S_tam_giac(a,b,c))
print("chu vinh hinh vuong: ",chu_vi_hinh_vuong(a))
print("dien tich hinh vuong: ",dien_tich_hinh_vuong(a))   