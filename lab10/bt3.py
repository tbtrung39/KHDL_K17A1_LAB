from pk3 import so_hoc

a = int(input("Nhập giá trị a: "))
b = int(input("Nhập giá trị b: "))

print("Ước chung lớn nhất của", a, "và", b, "là:", so_hoc.Ucln(a, b))
print("Bội số chung nhỏ nhất của", a, "và", b, "là:", so_hoc.Bcnn(a, b))

n = int(input("Nhập giá trị n: "))
print("Tổng các ước của", n, "là:", so_hoc.SumDivisor(n))
