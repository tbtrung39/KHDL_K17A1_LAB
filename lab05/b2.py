str = input("Nhap chuoi ky tu la:")
print("Chuoi ky tu vua nhap la:",str)
dem1 = 0
dem2 = 0
for c in str:
    if c.isalpha():
        dem1 += 1
    if "0" <= c <= "9":
        dem2 += 1
print("So ky tu khong la so trong chuoi str la:",dem1)
print("So ky tu khong la chu cai tieng anh la",dem2)