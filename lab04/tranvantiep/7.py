
a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai: "))

while b != 0:
    temp = b
    b = a % b
    a = temp

bcnn = (a * b) // abs(a)

print("Bội chung nhỏ nhất của", a, "và", b, "là:", bcnn)



