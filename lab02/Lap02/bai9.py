kw=float(input('Nhập số kw: '))
if kw>0:
    if 0<kw<=100:
        don_gia=2000
    elif 100<kw<=200:
        don_gia=2500
    elif 200<kw<=300:
        don_gia=3000
    elif kw>300:
        don_gia=5000
else:
    print("Không hợp lệ!")
tien_dien=kw*don_gia    
print('Tiền điện là:',tien_dien)
