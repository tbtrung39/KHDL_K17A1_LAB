tso = int(input("Nhập tử số:"))
mso = int(input("Nhập mẫu số:"))

def tim_ucln(a, b):
    while b:
        a, b = b, a % b
    return a
ucln = tim_ucln(tso, mso)
tso //= ucln
mso //= ucln
print("Phân số sau khi rút gọn là:", tso, "/", mso)

