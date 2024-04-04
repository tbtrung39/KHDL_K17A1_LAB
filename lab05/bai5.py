n = input("nhập vào một chuỗi ký tự: ")
chuoi = "".join(char for char in n if char.isdigit())
print(chuoi)
chuoi = int(chuoi)
tong = 0
for i in range(1,chuoi):
    if chuoi % i == 0:
        tong += i
        if tong == chuoi :
            print(f"chuỗi {chuoi} là số hoàn hảo")
            break
else:
    print(f"chuỗi {chuoi} ko phải số hoàn hảo")