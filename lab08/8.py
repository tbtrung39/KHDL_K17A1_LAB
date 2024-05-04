#8
import math
def tinh_chu_vi(r):
    return 2*math.pi*r
def tinh_dien_tich(r):
    return math.pi*r**2
ban_kinh=float(input("moi nhap ban kinh:"))
chu_vi=tinh_chu_vi(ban_kinh)
dien_tich=tinh_dien_tich(ban_kinh)
print("chu vi cua hinh tron la:",chu_vi)
print("dien tich cua hinh tron la:",dien_tich)
