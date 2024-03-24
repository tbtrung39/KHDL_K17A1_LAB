TNCT = int(input("Nhập số tháng công tác: "))
luong_co_ban = 1350000
if TNCT < 12:
    he_so = 2.34
    print("Lương của bạn là: ",he_so*luong_co_ban)
elif 12 <= TNCT < 36:
    he_so = 3.33
    print("Lương của bạn là: ",he_so*luong_co_ban)
elif 36 <= TNCT < 60:
    he_so = 3.66
    print("Lương của bạn là: ",he_so*luong_co_ban)
else: 
    he_so = 3.99
    print("Lương của bạn là: ",he_so*luong_co_ban)