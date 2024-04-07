str_1=str(input("Nhap chuoi ki tu 1:"))
str_2=str(input("Nhap chuoi ki tu 2:"))

max_len = max(len(str_1),len(str_2))

ket_qua=""

for i in range(max_len):
    if i<len(str_1):
        ket_qua += str_1[i]
    if i<len(str_2):
        ket_qua += str_2[i]

print("Chuoi ki tu sau khi tron: ",ket_qua)