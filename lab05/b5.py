str = input("Nhap chuoi ky tu la:")
chuoi = "".join(char for char in str if char.isdigit())
print(chuoi)
chuoi = int(chuoi)
s = 0
for i in range(1,chuoi):
    if chuoi % i ==0:
        s += 1
        if s == chuoi:
            print(chuoi,"la so hoan hao")
            break
else:
    print(chuoi,"khong la so hoan hao")