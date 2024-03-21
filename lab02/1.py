nhap_thang = int(input("nhập tháng cần sử dụng:"))
if nhap_thang % 2 == 0 and nhap_thang < 8 and nhap_thang != 2:
    print("tháng có 30 ngày")
elif nhap_thang == 2:
    print("tháng có 28 ngày hoặc 29 ngày")
elif nhap_thang % 2 != 0 and nhap_thang >= 8:
    print("tháng có 31 ngày")