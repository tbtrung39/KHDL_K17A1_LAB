import math

v_strart = float(input("Nhập vận tốc ban đầu của ô tô (m/s): "))

time_dung = v_strart * 4 / math.log(5, 4)
print("Thời gian ô tô đi được cho đến lúc dừng:", round(time_dung, 2), "giây")
