import sys
sys.path.append("lab10\hinh_hoc")

import hinh_hoc

a=float(input("nhap canh a: "))
b=float(input("nhap canh b: "))
c=float(input("nhap canh c: "))

print('la tam giac:', hinh_hoc.is_tam_giac(a,b,c))
print('chu vi tam giac la:')
hinh_hoc.chu_vi_tam_giac(a,b,c)
print("dien tich tam gian la:")
hinh_hoc.S_tam_giac(a,b,c)


print('chu vi hinh vuong la:',hinh_hoc.chu_vi_hinh_vuong(a))
print('dien tich hinh vuong:',hinh_hoc.dien_tich_hinh_vuong(a))