n = input("Nhap ki tu:")
num = ''
for char in n:
    if char.isdigit():
        num += char
print("Chuoi sau khki xoa ki tu la:",num)

if num.isdigit():
    numb = int(num)
    tong_uoc = 0
    for i in range (1,numb):
        if numb % i == 0:
            tong_uoc += 1
        if tong_uoc == numb:
            print("Chuoi so la so hoan hao.")
        else:
            print("Chuoi so khong la so hoan hao.")
else:
    print("Khong la mot chuoi.")
