n = int(input("Nhập vào số n: "))

ma_tran_don_vi = tuple((1 if i == j else 0 for j in range(n)) for i in range(n))

print("Ma trận đơn vị bậc", n, "là:")
for row in ma_tran_don_vi:
    print(row) 