import math

def tinh_chu_vi(ban_kinh):
    return 2 * math.pi * ban_kinh

def tinh_dien_tich(ban_kinh):
    return math.pi * (ban_kinh ** 2)
ban_kinh = float(input("nhap ban kinh hinh tron: "))
chu_vi = tinh_chu_vi(ban_kinh)
dien_tich = tinh_dien_tich(ban_kinh)
print("chu vi hinh tron la:", chu_vi)
print("dien tich hinh tron la:", dien_tich)