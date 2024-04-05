ky_tu_1 = input("Nhap chuoi ky tu 1: ")
ky_tu_2 = input("Nhap chuoi ky tu 2: ")
s = ""
for i in range(len(ky_tu_1)):
    for j in ky_tu_2:
        if ky_tu_1[i] == j:
            s += j
print(s)