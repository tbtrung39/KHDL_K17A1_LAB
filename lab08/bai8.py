def chu_vi_hinh_tron(r):
    return 2*2.14*r
def dien_tich_hinh_tron(r):
    return 2*2.14*(r**2)

r=int(input("nhap ban kinh hinh tron: "))
print(chu_vi_hinh_tron(r))
print(dien_tich_hinh_tron(r))