#công thức tính diện tích hình tròn s = pi.r^2
#công thức tính chu vi hình tròn c = r.2.3,14
#tính diện tích:
pi = 3.14
r = int(input("nhập bán kính của hình tròn:"))
def dien_tich_hinh_tron(pi,r):
    dien_tich_hinh_tron = pi*r**2
    print(f"diện tích của hình tròn là:{dien_tich_hinh_tron}")
    return dien_tich_hinh_tron
dien_tich_hinh_tron(pi,r)
#tính chu vi:
def chu_vi_hinh_tron(pi,r):
    chu_vi_cua_hinh_tron = r*2*3.14
    print(f"chu vi của hình tròn là:{chu_vi_cua_hinh_tron}")
    return chu_vi_cua_hinh_tron
chu_vi_hinh_tron(pi,r)
