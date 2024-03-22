n = int(input("Nhập vào một số nguyên dương n: "))
print("Các số nguyên tố nhỏ hơn hoặc bằng", n, "là:")
for j in range(2, n + 1):
    so_nguyen_to = 1
    for i in range(2, int(j ** 0.5) + 1):
        if j % i == 0:
            so_nguyen_to = 0
            break
    if so_nguyen_to:
        print(j, end=" ")