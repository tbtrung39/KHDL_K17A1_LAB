def ucln(x,y):
    while x != y:
        if x > y: 
            x = x - y
        else: 
            y = y - x
    return x
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
print(f"Ước chung lớn nhất của {a} và {b} là {ucln(a,b)}")