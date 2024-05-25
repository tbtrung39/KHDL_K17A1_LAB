import sys
sys.path.append("lab10\package_4")

import package_4

a=float(input("nhap gia tri a: "))
b=float(input("nhap gia tri b: "))
c=float(input("nhap gia tri c: "))

print(package_4.giai_pt_bac_nhat_mot_an(a,b))
print(package_4.giai_pt_bac_2(a,b,c))