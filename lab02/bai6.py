# Nhập số nguyên có ba chữ số từ người dùng
so_nguyen = int(input("Nhập một số nguyên có ba chữ số: "))

# Tách và in ra từng chữ số của số nguyên
hang_tram = so_nguyen // 100
hang_chuc = (so_nguyen // 10) % 10
hang_don_vi = so_nguyen % 10

# In ra cách đọc của số nguyên này
print("Cách đọc của số nguyên", so_nguyen, "là:")
print(hang_tram, "trăm", end=" ")

if hang_chuc == 1:
    if hang_don_vi == 0:
        print("mười")
    elif hang_don_vi == 5:
        print("mười lăm")
    else:
        print("mười", hang_don_vi)
elif hang_chuc > 1:
    print("mươi", end=" ")
    if hang_don_vi == 0:
        print(hang_chuc)
    elif hang_don_vi == 1:
        print("mốt")
    elif hang_don_vi == 4:
        print("tư")
    else:
        print(hang_don_vi)
else:
    if hang_don_vi == 0:
        print()
    elif hang_don_vi == 1:
        print("một")
    elif hang_don_vi == 4:
        print("bốn")
    elif hang_don_vi == 5:
        print("năm")
    elif hang_don_vi == 6:
        print("sáu")
    elif hang_don_vi == 7:
        print("bảy")
    elif hang_don_vi == 8:
        print("tám")
    elif hang_don_vi == 9:
        print("chín")