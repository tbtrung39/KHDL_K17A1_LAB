str = input("Nhap chuoi ky tu la:")
print("Chuoi ky tu vua nhap la:",str)
dem = 0
for c in str:
    if "0" <= c <= "9":
        dem += 1
print("So ky tu la so trong chuoi vua nhap la:",dem)