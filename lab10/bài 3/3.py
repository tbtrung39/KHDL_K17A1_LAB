import sohoc
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
result = sohoc.Ucln(a, b)
print(f"Ước chung lớn nhất của {a} và {b} là: {result}")
result1 = sohoc.Bcnn(a, b)
print(f"Bội số chung nhỏ nhất của {a} và {b} là: {result1}")

n = int(input("Nhập số nguyên n: "))
result2 = sohoc.SumDivisor(n)
print(f"Tổng các ước của {n} là: {result}")
