import math
def tinh_chu_vi(r):
    chu_vi = 2 * math.pi * r
    return chu_vi
def tinh_dien_tich(r):
    dien_tich = math.pi * r ** 2
    return dien_tich
ban_kinh = float(input("Nhập bán kính của hình tròn: "))
chu_vi = tinh_chu_vi(ban_kinh)
dien_tich = tinh_dien_tich(ban_kinh)
print("Chu vi của hình tròn là:", chu_vi)
print("Diện tích của hình tròn là:", dien_tich)
