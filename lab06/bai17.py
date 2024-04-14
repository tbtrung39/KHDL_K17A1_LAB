#17
n = int(input("Nhập bậc của ma trận đơn vị: "))
a = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
print("Ma trận đơn vị bậc", n, "là:")
for k in a:
    print(k)