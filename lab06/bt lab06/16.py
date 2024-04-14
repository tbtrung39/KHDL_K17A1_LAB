X = int(input("Nhập giá trị X: "))
Y = int(input("Nhập giá trị Y: "))
mang_2_chieu = [[i*j for j in range(Y)] for i in range(X)]

print("Mảng 2 chiều được tạo:")
for row in mang_2_chieu:
    print(row)
