n = int(input("Nhập số lần tung xúc sắc là:"))
tong = 3**n
khong_co_6 = 2**n
xs_khong_co_6 = khong_co_6/tong
xs_cua_it_nhat_mot_6 = 1 - xs_khong_co_6
print("Xác suất tung ",n,"lần 3 xúc sắc ra 6 là", xs_cua_it_nhat_mot_6)