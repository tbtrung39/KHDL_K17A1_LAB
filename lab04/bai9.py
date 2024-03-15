while True:
    tong = 0
    n = int(input("Nhập số: "))
    for so in str(n):
        tong += int(so)
    print(tong)
    break