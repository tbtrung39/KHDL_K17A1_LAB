str = input("Nhap mot chuoi ky tu : ")
tong = 0
for i in str:
    if not i.isalnum():
        tong += 1
print(tong)