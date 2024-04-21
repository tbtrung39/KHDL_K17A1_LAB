import random
n = int(input("Nhập số phần tử: "))
tap_a = set(random.randint(0,100) for _ in range(n))
nho = min(tap_a)
lon = max(tap_a)
tong = sum(tap_a)
print("Max: ", lon)
print("Min: ", nho)
print("Tổng:" ,tong)