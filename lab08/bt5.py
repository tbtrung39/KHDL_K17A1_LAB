#thuật toán euclid ta cho a = b , b = phần dư của a / b đến khi nào phép dư bằng 0 thì trả về giá trị a
#a là ước chung lớn nhất sau khi trả về
def tim_ucln(a, b):
    #Tìm ước chung lớn nhất của hai số a và b.
    while b != 0:
        a, b = b, a % b
    return a
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
print(f"ước chung lớn nhất của hai số a và b là {a}")