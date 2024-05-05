def hinh_tron(r):
    chu_vi = r*2*3.14
    dien_tich = r**2*3.14
    return chu_vi,dien_tich
r = int(input("Nhập bán kính: "))
chu_vi,dien_tich = hinh_tron(r)
print("Chu vi hình tròn là: ",chu_vi)
print("Diện tích hình tròn: ",dien_tich)