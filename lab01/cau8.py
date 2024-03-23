import math
x= float(input("Nhập giá trị của x: "))
gia_tri_cua_bieu_thuc = math.log(x, 4) + math.log(2, x)
print(f'gia tri cua bieu thuc la: {gia_tri_cua_bieu_thuc:.2f}')