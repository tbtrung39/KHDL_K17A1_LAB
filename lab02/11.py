#Cho trước số ngày trong một tháng của năm không nhuận như sau:
ngay=int(input("moi nhap he so nam"))
thang=int(input("moi nhap he so thang:"))
nam=int(input("moi nhap he so thang"))
if thang==2:
    if (nam%4==0 and nam%100!=0) or (nam%400==0):
        so_ngay_trong_thang=29
    else:
        so_ngay_trong_thang=28
elif (thang%2==0 and thang<=7 ) or (thang%2==1 and thang>=8):
        so_ngay_trong_thang=30
else:
        so_ngay_trong_thang=21


if 1 <= ngay <= so_ngay_trong_thang:
     ngay += 1
else:
     ngay = 1
     thang += 1

if thang == 13:
     thang = 1
     nam += 1
     print(f"Ngày tiếp theo là: {thang}/{thang}/{nam}")


