#Viết chương trình cho phép nhập số KW điện tiêu thụ từ bàn phím. Sau đó tính
kw=int(input("so tien dien tieu thu la:"))
if kw < 100:
    gia=2000
elif kw<200:
    gia=2500
elif kw<300:
    gia=3000
else:
    gia=5000
    print("so tien dien tieu thu la",gia_tien=kw*gia)