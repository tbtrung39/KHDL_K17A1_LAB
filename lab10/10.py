import sys
sys.path.append("lab10\hinhhoc")
import packages
a, b, c=3, 4, 5
print("chu vi: ", packages.chu_vi_hinh_vuong(a))
print("Diện tích: ",packages.dien_tich_hv(a) )
if packages.la_tram_giac(a, b, c):
    print("llà tam giác")
else:
    print("Ko là tam giác")
print("chu vi", packages.chu_vi(a,b,c))
print("diện tích",packages.dien_tich(a,b,c))