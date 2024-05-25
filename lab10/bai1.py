import sys
sys.path.append("lab10\package_1")

import package_1

a=float(input("nhap canh a: "))
b=float(input("nhap canh b: "))
c=float(input("nhap canh c: "))

print(package_1.is_tam_giac(a,b,c))
package_1.chu_vi_tam_giac(a,b,c)
package_1.S_tam_giac(a,b,c)