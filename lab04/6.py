so_a = int(input("Nhập số nguyên a: "))
so_b = int(input("Nhập số nguyên b: "))
a, b = so_a, so_b
while b:
    a, b = b, a % b
bcnn = (so_a * so_b) // a
print("BCNN", so_a, "và", so_b, "là:", bcnn)
