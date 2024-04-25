def lap_phuong_so(so):
    """Tính giá trị lập phương của một số nguyên."""
    return so ** 3

try:
    so_nguyen = int(input("Nhập một số nguyên: "))
    gia_tri_lap_phuong = lap_phuong_so(so_nguyen)
    print("Giá trị lập phương của", so_nguyen, "là:", gia_tri_lap_phuong)
except ValueError:
    print("Vui lòng nhập một số nguyên.")