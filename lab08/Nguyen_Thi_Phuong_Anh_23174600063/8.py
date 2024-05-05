import math
def tinh_chu_vi(x):
    return 2 * math.pi * r
def tinh_dien_dich(x):
    return math.pi*(r**2)
r = int(input('Nhập bán kính:'))
chu_vi = tinh_chu_vi(r)
dien_tich = tinh_dien_dich(r)
print(f'Chu vi hình tròn là: {chu_vi:.2f}')
print(f'Diện tích hình tròn là: {dien_tich:.2f}')