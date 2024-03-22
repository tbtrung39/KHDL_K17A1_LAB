#câu 3 tìm số nguyên tố gần nhất
n = int(input("Nhập một số nguyên dương n: "))

la_so_nguyen_to = True
so_nguyen_to_gan_nhat = 0

for num in range(n, 1, -1):
    la_so_nguyen_to = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            la_so_nguyen_to = False
            break
    if la_so_nguyen_to:
        so_nguyen_to_gan_nhat = num
        break
if la_so_nguyen_to:
    if n == so_nguyen_to_gan_nhat:
        print(n, "là số nguyên tố.")
    else:
        print(n, "không phải là số nguyên tố. Số nguyên tố gần nhất là:", so_nguyen_to_gan_nhat)
else:
    print("Không có số nguyên tố nào nhỏ hơn", n)