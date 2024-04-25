def tim_ucln(a, b):
    #Tìm ước chung lớn nhất của hai số a và b.
    while b != 0:
        a, b = b, a % b
    return a

def tim_bcnn(a, b):
    #Tìm bội chung nhỏ nhất của hai số a và b.
    return (a * b) // tim_ucln(a, b)

# Nhập hai số từ người dùng
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

# Tìm và in ra bội chung nhỏ nhất của a và b
bcnn = tim_bcnn(a, b)
print("Bội chung nhỏ nhất của", a, "và", b, "là:", bcnn)