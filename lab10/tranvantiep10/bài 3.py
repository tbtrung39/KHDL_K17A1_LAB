from pk3 import modult3

a = int(input("Nhập giá trị a: "))
b = int(input("Nhập giá trị b: "))

print("Ước chung lớn nhất của", a, "và", b, "là:", modult3.Ucln(a, b))
print("Bội số chung nhỏ nhất của", a, "và", b, "là:", modult3.Bcnn(a, b))

n = int(input("Nhập giá trị n: "))
print("Tổng các ước của", n, "là:", modult3.SumDivisor(n))