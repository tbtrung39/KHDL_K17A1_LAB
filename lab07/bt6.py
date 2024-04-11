# Nhập số tự nhiên n từ bàn phím
so_luong_nguyen_to = int(input("Nhập số tự nhiên n: "))

# In ra dãy n số nguyên tố đầu tiên
print(f"Dãy {so_luong_nguyen_to} số nguyên tố đầu tiên:")
so_luong_da_tim_thay = 0
so = 2
nguyen_to = []

for so in range(2, 1000):
    la_nguyen_to = True
    for i in range(2, int(so ** 0.5) + 1):
        if so % i == 0:
            la_nguyen_to = False
            break
    if la_nguyen_to:
        nguyen_to.append(so)
        so_luong_da_tim_thay += 1
    if so_luong_da_tim_thay == so_luong_nguyen_to:
        break

print(nguyen_to)
