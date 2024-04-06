a = input("Nhập chuỗi kí tự: ")
chuoi ="".join(char for char in a if char.isdigit())
chuoi = int(chuoi)
s = 0
for i in range(1,chuoi):
    if chuoi % i == 0:
        s += i
        if s == chuoi:
            print(chuoi, "là số hoàn hảo")
            break
else:
    print(chuoi, "không là số hoàn hảo")