# Nhập vào một số nguyên có ba chữ số
so_nguyen = int(input("Nhập vào một số nguyên có ba chữ số: "))

# Kiểm tra và in ra cách đọc của số nguyên
if 100 <= so_nguyen <= 999:
    hang_tram = so_nguyen // 100
    hang_chuc = (so_nguyen % 100) // 10
    hang_don_vi = so_nguyen % 10

    print(f"Cách đọc của số {so_nguyen} là: {hang_tram} trăm", end=" ")

    if hang_chuc != 0:
        print(f"{hang_chuc} chục", end=" ")

    if hang_don_vi != 0:
        print(f"{hang_don_vi} đơn vị")
else:
    print("Số không hợp lệ. Vui lòng nhập lại số nguyên có ba chữ số.")