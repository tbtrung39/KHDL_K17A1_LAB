import math

van_toc_ban_dau = float(input("Nhập vào vận tốc ban đầu của xe (m/s): "))
a = float(input("Nhập vào hệ số a: "))

thoi_gian = van_toc_ban_dau / (math.log(5,4) - a**4)
thoi_gian = round(thoi_gian, 2)

print("Thời gian để xe dừng là:", thoi_gian, "giây.")