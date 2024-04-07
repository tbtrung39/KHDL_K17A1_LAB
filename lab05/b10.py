chuoi_nhi_phan = input("Nhập chuỗi ký tự nhị phân: ")

so_thap_phan = 0
mu = len(chuoi_nhi_phan) - 1

for ki_tu in chuoi_nhi_phan:
    if ki_tu == '1':
        so_thap_phan += 2 ** mu
    mu -= 1

print("Số thập phân tương ứng là:", so_thap_phan)
