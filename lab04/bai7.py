a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai: "))
if a == 0 or b == 0:
    print("Không tồn tại bội chung nhỏ nhất")
else:
    i = 1
    while True:
        if i % a == 0 and i % b == 0:
            boi_chung_nho_nhat = i
            break
        i += 1

    print("Bội chung nhỏ nhất của", a, "và", b, "là:", boi_chung_nho_nhat)