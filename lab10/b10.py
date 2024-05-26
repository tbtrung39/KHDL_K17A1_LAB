import sys
sys.path.append("lab10\hinhhoc")
import packages
a, b, c=3, 4, 5
print("chu vi: ", packages.chuviHinhVuong(a))
print("Diện tích: ",packages.Dien_tich_hinh_vuong(a) )
if packages.is_TamGiac(a, b, c):
    print("là tam giác")
else:
    print("Ko là tam giác")
print("chu vi", packages.ChuviTamGiac(a,b,c))
print("diện tích",packages.S_TamGiac(a,b,c))