chuoi_nhi_phan = input("Nhập chuỗi nhị phân: ")

so_thap_phan = 0

for i in range(len(chuoi_nhi_phan)):
    if chuoi_nhi_phan[i] == '1':
        so_thap_phan += 2 ** (len(chuoi_nhi_phan) - i - 1)

print("Số thập phân tương ứng là:", so_thap_phan)
