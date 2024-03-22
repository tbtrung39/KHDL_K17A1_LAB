import math
van_toc_ban_dau = float(input("Nhập vận tốc ban đầu của ô tô (m/s): "))
thoi_gian_dung = round(math.log(van_toc_ban_dau**4, 5), 2)
print("Thời gian ô tô đi được cho đến khi dừng là:",thoi_gian_dung, "giây")