n = int(input("Nhập số n: "))
x = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
print("ma trận đơn vị bâc", n, ":")
for row in x:
    print(row) 