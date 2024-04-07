chuoi = input("Nhap chuoi: ")

he_thap_luc_phan= '0123456789ABCDEF'
gia_tri_he = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,'8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}


chuoi_he_thap_luc_phan = ''
for char in chuoi:
    if char.upper() in he_thap_luc_phan:
        chuoi_he_thap_luc_phan += char


gia_tri_thap_phan = 0
for char in chuoi_he_thap_luc_phan:
    gia_tri_thap_phan = gia_tri_thap_phan * 16 + gia_tri_he[char.upper()]

print("Gia tri thap phan cua chuoi he thap luc phan là: ", gia_tri_thap_phan)