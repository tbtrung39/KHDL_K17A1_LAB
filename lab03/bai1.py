n = int(input("Nhập một số nguyên dương n: "))

tong = 0
tich = 1

for i in range(1, n + 2):
    tich *= (2 * i) / (2 * i + 1)
    tong += tich

print("Kết quả của phép toán là:", round(tong, 3))
