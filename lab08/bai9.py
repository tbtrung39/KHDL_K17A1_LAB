def basic_math(a,b):
    add = a + b
    sub = a - b
    mul = a * b
    div = a / b
    return add,sub,mul,div
a = int(input("nhập vào số nguyên a: "))
b = int(input("nhập vào số nguyên b: "))
print(f"các phép toán cơ cộng,trừ,nhân,chia của a và b lần lượt là {basic_math(a,b)}")