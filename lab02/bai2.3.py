thu = int(input("Nhập vào thứ (1-7): "))
if thu >= 1 and thu <= 7:
    print("nhập sai")
if thu == 1:
    print("Chủ Nhật.")
elif thu == 2:
    print("Thứ Hai.")
elif thu == 3:
    print("Thứ Ba.")
elif thu == 4:
    print("Thứ Tư.")
elif thu == 5:
    print("Thứ Năm.")
elif thu == 6:
    print("Thứ Sáu.")
else:
    print("Thứ Bảy.")