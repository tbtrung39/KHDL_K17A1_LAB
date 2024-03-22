#câu 7 tính tổng nghịch đảo
n = int(input("Nhập số nguyên dương n: "))
tong_nguoc_dao = 0

for i in range(1, n + 1):
    tong_nguoc_dao += 1 / i

print("Tổng nghịch đảo của", n, "số nguyên đầu tiên là:", tong_nguoc_dao)
