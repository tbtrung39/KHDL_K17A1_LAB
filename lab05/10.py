str1 = input("Nhap chuoi ky tu 1: ")
str2 = input("Nhap chuoi ky tu 2: ")
ky_tu_con_chung=" "
for ky_tu in str1:
    if ky_tu in str2 and ky_tu not in ky_tu_con_chung:
        ky_tu_con_chung += ky_tu
print(ky_tu_con_chung)
print("do dai cuc dai",len(ky_tu_con_chung))
