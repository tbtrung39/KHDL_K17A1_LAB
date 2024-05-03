def tinh_lap_phuong(so_nguyen):
    lap_phuong = so_nguyen**3
    return lap_phuong
so_nguyen = int(input("Nhập 1 số nguyên: "))
lap_phuong = tinh_lap_phuong(so_nguyen)
print(f"Giá trị lập phương của {so_nguyen} là {lap_phuong}")