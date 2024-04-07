so_thap_phan = int(input('Nhap so thap phan: '))
so_nhi_phan = ""

if so_thap_phan == 0:
    so_nhi_phan = "0"
else:
    while so_thap_phan > 0:
        so_nhi_phan = str(so_thap_phan % 2) + so_nhi_phan
        so_thap_phan //= 2

print("So nhi phan tuong ung la: ", so_nhi_phan)
