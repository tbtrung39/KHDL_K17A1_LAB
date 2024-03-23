import math

a = float(input("Nhập vận tốc ban đầu của ô tô (m/s): "))

# Giải phương trình bậc hai để tìm thời gian khi vận tốc gần đến 0
A = math.log(45)
B = -a ** 4
delta = B ** 2 - 4 * A * 0
t = (-B + math.sqrt(delta)) / (2 * A)

print("Thời gian ô tô đi được cho đến khi dừng là:", round(t, 2), "giây")
