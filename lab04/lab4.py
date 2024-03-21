#1
n = int(input("Nhập số n: "))
s4 = 0
s5 = 0
s6 = 0
while n > 0:
    for i in  range(1,n+1):
        s4 += i**2
        if i % 2 != 0:
            s5 += i**3
        if i % 2 == 0:
            s6 += i**4
    break
print(f"S4 = {s4}")
print(f"S5 = {s5}")
print(f"S6 = {s6}")
#2
n = int(input("Nhập vào số nguyên n: "))
s = 0
sb = 0
sc = 0
while n > 0:
    for i in range(1,n+1):
        if i % 2 == 0:
            s -= 1/i
        else:
            s += 1/i
    break
print(s)
while n > 0:
    for i in range(1,n):
        sb += 1/(i*(i+1))
    break
print(sb)
while n > 0:
    for i in range(2,n+1):
        sc += 1/(i**0.5)
    break
print(sc)
#3
x = int(input("nhập vào một số nguyên x: "))
cosx = 1
while cosx > 0:
    for i in range(1,x+1):
        if i % 2 == 0:
            cosx = -x**2 / ((2*x - 1) * (2*x))
            print(cosx)
    break
#4
while True:
    tu_so = int(input("Nhập tử số của phân số: "))
    mau_so = int(input("Nhập mẫu số của phân số: "))
    if mau_so != 0:
        break
    else:
        print("Mẫu số không được = 0, nhập lại")
print(f"phân số là {tu_so/mau_so}")
#5
while True:
    n = int(input("nhập vào số n: "))
    if n < 0:
        break
    else:
        print("vui lòng nhập tiếp")
print("số nhập vào là số âm")
#6
chu_so = {
    '0': 'không',
    '1': 'một',
    '2': 'hai',
    '3': 'ba',
    '4': 'bốn',
    '5': 'năm',
    '6': 'sáu',
    '7': 'bảy',
    '8': 'tám',
    '9': 'chín'
}
so = input("Nhập số: ")
so_chu = ''
i = 0
while i < len(so):
    so_chu += chu_so[so[i]] + ' '
    i += 1
print("Số", so, "bằng chữ là:", so_chu.strip())
#7
a =int(input("nhập vào số a: "))
b =int(input("nhập vào số b: "))
mer_a = a
mer_b = b
while mer_a != mer_b:
    if mer_a < mer_b:
        mer_a += a
    else:
        mer_b += b
bcnn = mer_a
print("Bội chung nhỏ nhất của hai số là:" ,bcnn)
#8
char = input("Nhập một ký tự: ")
avalue = ord(char)
print(f"Giá trị ASCII của ký tự '{char}' là: {avalue}")
#9
n = int(input("Nhập một số n: "))
sum = 0
while n > 0:
    digit = n % 10
    sum += digit
    n //= 10 
print("Tổng các chữ số của số vừa nhập là:", sum)
#10
stp = int(input("Nhập một số thập phân: "))
if stp < 0:
    print("Vui lòng nhập một số không âm.")
else:
    ky_tu = ""
    chu_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    while stp > 0:
        don_vi = stp % 10
        ky_tu = chu_so[don_vi] + " " + ky_tu
        stp //= 10
    print("Số được chuyển thành dạng ký tự là:", ky_tu.strip())
#11
while True:
    print("1.Cafe")
    print("2.Cam vắt")
    print("3.Nước ép cà rốt")
    print("4.Nước lọc")
    print("5.Nước dừa")
    choice = int(input("nhập lựa chọn: "))
    if choice == 1:
        print("Cafe")
        break
    if choice == 2:
        print("Cam vắt")
        break
    if choice == 3:
        print("Nước ép cà rốt")
        break
    if choice == 4:
        print("Nước lọc")
        break
    if choice == 5:
        print("Nước dừa")
        break
    else:
        print("ko có đồ uống này")
    break
