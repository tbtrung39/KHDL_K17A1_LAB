n = int(input("Nhập số n: "))
ma_tran_don_vi = [[0] * n for _ in range(n)]
for i in range(n):
    ma_tran_don_vi[i][i] = 1
print("Ma trận đơn vị bậc", n, "là:")
for dong in ma_tran_don_vi:
    print(dong)
