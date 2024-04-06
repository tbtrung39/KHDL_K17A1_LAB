Str1 = input("Nhap chuoi ky tu thu nhat : ")
Str2 = input("Nhap chuoi ky tu thu hai : ")
xau_ket_qua = ''
i = 0
while i < len(Str1) and i < len(Str2):
    xau_ket_qua += Str1[i]
    xau_ket_qua += Str2[i]
    i += 1

xau_ket_qua += Str1[i:]
xau_ket_qua += Str2[i:]

print(xau_ket_qua)