chuoi = input("Nhập chuỗi: ")
hex_chuoi = "0123456789ABCDEFabcdef"
hex = True
gia_tri_thap_phan = 0

for ki_tu in chuoi:
    if ki_tu not in hex_chuoi:
        hex = False
        continue
    gia_tri_thap_phan = gia_tri_thap_phan * 16 + int(ki_tu, 16)

if hex:
    print("Chuỗi là chuỗi Hex.")
else:
    print("Chuỗi không phải là chuỗi Hex.")
    print("Giá trị thập phân của chuỗi:", gia_tri_thap_phan)