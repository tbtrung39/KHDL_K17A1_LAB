a = float(input("Nhập vào vận tốc a của một ô tô đang chạy là:"))
a1 = float(input("Nhập vào gia tốc xe chạy là:"))
def tinh_thoi_gian(a,a1):
    t = a/a1
    return round(t, 2)
tinh=tinh_thoi_gian(a,a1)
print("Thời gian ô tô đi cho đến lúc dừng là:", tinh)