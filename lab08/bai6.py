def find_bcnn(a,b):
    a_goc = a
    b_goc = b
    while a != b:
        if a < b:
            a += a_goc
        else: 
            b += b_goc
    return a
a = int(input("nhập vào số nguyên a: "))
b = int(input("nhập vào số nguyên b: "))
print(f"bội chung nhỏ nhất của {a} và {b} là {find_bcnn(a,b)}")