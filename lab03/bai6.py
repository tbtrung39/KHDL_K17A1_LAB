n = int(input("Nhập số nguyên dương n: "))
tong=0
if n <= 0:
    print("số không hợp lệ!!!")
else:
    for i in range(1, n + 1):
        tong += i ** 3
    print("tổng bậc 3 của n số nguyên dầu tiên là:", tong)