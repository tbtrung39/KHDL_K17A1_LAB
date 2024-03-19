dien_tieu_thu= int(input("nhap KW dien tieu thu: "))
if dien_tieu_thu <0:
    print("vui long nhap lai")
elif dien_tieu_thu >=0 and dien_tieu_thu<=100:
    don_gia=2000*dien_tieu_thu
elif dien_tieu_thu >100 and dien_tieu_thu<=200:
    don_gia=2500*dien_tieu_thu
elif dien_tieu_thu >200 and dien_tieu_thu<=300:
    don_gia=3000*dien_tieu_thu
else:
    don_gia=5000*dien_tieu_thu

print("tien dien la: ",don_gia,"dong")