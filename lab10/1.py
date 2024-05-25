import sys
sys.path.append("lab10\packages")
import packages
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
if packages.la_tram_giac(a, b, c):
    print("llà tam giác")
else:
    print("Ko là tam giác")
print("chu vi", packages.chu_vi(a,b,c))
print("diện tích",packages.dien_tich(a,b,c))