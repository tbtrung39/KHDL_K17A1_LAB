hours = int(input("nhap so gio  thue san: "))
time = int(input("nhap thoi gian bat dau thue san: "))
if hours <0 or hours >17:
    print("vui long nhap lai hours")
elif time <=5 or time >=22:
    print("vui long nhap lai time")
else:
    if hours <=3 :
        gia_tien=100000*hours
    elif hours >3:
        gia_tien= 100000*hours*(25/100)
    if time >= 11 and time <= 15:
        gia_tien=gia_tien*(10/100)
    print("gia tien la: ",gia_tien,"dong")