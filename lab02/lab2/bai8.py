tnct0 =  int(input('Nhập năm công tác : '))

tnct = tnct0 * 12

if tnct > 0 :
    if tnct < 12:
        he_so = 2.34
    elif 12 <= tnct < 36:
        he_so = 3.33
    elif 36 <= tnct < 60:
        he_so = 3.66
    elif tnct >= 60:
        he_so = 3.99
else:
    print('Số năm k  hợp lệ ')
 

print('lương của nhân viên là :',he_so*1350000,'VND')