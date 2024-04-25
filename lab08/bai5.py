def find_ucln(a,b):
    while b != 0:
        a, b = b, a%b
    return a
a = int(input("nhập vào số nguyên a: "))
b = int(input("nhập vào số nguyên b: "))
find_ucln(a,b)
print(f"ước chung lớn nhất của {a} và {b} là {find_ucln(a,b)}")