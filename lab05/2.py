str1 = input("Nhap chuoi tu ban phim: ")
chuoi = "".join(char for char in str1 if char.isdigit())
chuoi = int(chuoi)
s = 0
for i in range(1, chuoi):
    if chuoi % i == 0:
        s += i
        if s == chuoi:
            print(chuoi, "La so hoan hao")
            break
else:
    print(chuoi, "Khong la so hoan hao")