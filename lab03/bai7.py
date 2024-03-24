n = int(input("Nhập số nguyên dương n: "))
if n <= 0:
    print("Vui lòng nhập một số nguyên dương.")
else:
    tong = 0
    for i in range(1,n + 1):
        tong += 1/i
    print("Tổng nghịch đảo là:", tong)