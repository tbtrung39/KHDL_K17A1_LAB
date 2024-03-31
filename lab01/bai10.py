import math
a = float(input("Nhập vận tốc a của xe ô tô: "))
thoigiandung = a**4 / math.log(5, 4)
print(f"Thời gian ô tô đi được cho đến khi dừng: {thoigiandung:.2f} giây")