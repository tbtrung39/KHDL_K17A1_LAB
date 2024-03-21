kw=int(input('Nhập số kw tiêu thụ :'))
if kw>0 and kw<=100:
    don_gia=2000
elif kw>100 and kw<=200 :
    don_gia=2500
elif kw>201 and kw<=300 :
    don_gia=3000
elif kw>300:
    don_gia=5000
else:
    print('Loi')

tien_dien=kw*don_gia
print("Tien dien la :", tien_dien)