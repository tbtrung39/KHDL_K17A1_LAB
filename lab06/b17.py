n = int(input("Nhập vào số nguyên dương n: "))
if n <= 0:
    print("Vui lòng nhập số nguyên dương.")
else:
    ma_tran = [[1 if j == i else 0 for j in range(n)] for i in range(n)]
    # In ra ma trận đơn vị
    print("Ma trận đơn vị bậc", n, "là:")
    for row in ma_tran:
        print(row)
