import math

van_toc_ban_dau = float(input("Nhập vận tốc ban đầu của ô tô (m/s): "))

thoi_gian = (van_toc_ban_dau * 4) / math.log(5, 4)
print("Thời gian ô tô đi được cho đến lúc dừng:", round(thoi_gian, 2), "giây")
