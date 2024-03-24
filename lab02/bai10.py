giobatdau = int(input("Nhập giờ bắt đầu thuê sân (từ 5 đến 22): "))
gioketthuc = int(input("Nhập giờ kết thúc thuê sân (từ 5 đến 22): "))
if not (5 <= giobatdau <= 22 and 5 <= gioketthuc <= 22):
    print("Giờ không hợp lệ, hãy nhập lại từ 5 đến 22.")
elif giobatdau <= gioketthuc:
    print("Giờ kết thúc phải sau giờ bắt đầu.")
tong_gio=gioketthuc- giobatdau
if tong_gio<=3:
    tien=tong_gio*100000
elif tong_gio>3:
    tien=(tong_gio-3)*100000*0.75+3*100000
if 11 <= giobatdau <= 15:
    tien=((3)*100000+(tong_gio-3)*100000*0.75)-(0.1*((3)*100000+(tong_gio-3)*100000*0.75))
print("Số tiền khách hàng phải trả là:", tien , "đồng.")