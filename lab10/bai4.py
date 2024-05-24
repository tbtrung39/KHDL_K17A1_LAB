from package_4 import module
print("Giải phương trình bậc nhất ax + b = 0")
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
print(module.giaiPTBacNhat(a, b))

print("\nGiải phương trình bậc hai ax^2 + bx + c = 0")
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
print(module.giaiPTBacHai(a, b, c))