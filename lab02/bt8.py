thang = int(input("Nhập vào thâm niên công tác (tính bằng tháng): "))
luong_can_ban = 1350000
if thang < 12:
    he_so = 2.34
elif thang < 36:
    he_so = 3.33
elif thang < 60:
    he_so = 3.66
else:
    he_so = 3.99
print(f"Lương của nhân viên là: {thang*luong_can_ban} đồng")