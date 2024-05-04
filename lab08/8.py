import math
def tinh_chu_vi(n):
    chu_vi=2*math.pi*n
    return chu_vi
def tinh_dien_tich(n):
    dien_tich=math.pi*n**2
    return dien_tich
n=float("Độ dài bán kính:")
print("Diện tích hình tròn:",tinh_dien_tich(n))
print("Chu vi hình tròn:",tinh_chu_vi(n))