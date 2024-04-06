str1 = input +("Nhập chuỗi từ bàn phìm: ")
chuoi = "".join(char for char in str1 if char.isdigit())
chuoi = int(chuoi)
s = 0
for i in range(1, chuoi):
    if chuoi % i ==0:
        s += 1
        if s == chuoi:
            print(chuoi, "là số hoàn hảo")
            break
else:
    print(chuoi, "Không là số hoàn hảo")