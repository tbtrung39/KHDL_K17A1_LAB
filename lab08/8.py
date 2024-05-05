# tính chu vi diện tích hình tròn 
import math
def chu_vi_dien_tich(r):
    return r
r = int(input("nhập giá trị bán kính:"))
chu_vi = 2*math.pi*r
dien_tich = (math.pi)*r**2
ban_kinh = chu_vi_dien_tich(r)
print("với bán kính bằng",ban_kinh)
print("chu vi hình tròn là", chu_vi)
print("diện tích hình tròn là", dien_tich)