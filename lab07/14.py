tu_dien_nhi_phan = {}

for so in range(1, 101):
    tu_dien_nhi_phan[so] = bin(so)[2:]

for so, chuoi_nhị_phan in tu_dien_nhi_phan.items():
    print(f"{so}: {chuoi_nhị_phan}")
