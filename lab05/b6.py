chuoi_ky_tu = input("Nhập chuỗi ký tự: ")

ky_tu_hex = set("0123456789ABCDEF")
la_hex = True

for ki_tu in chuoi_ky_tu:
    if ki_tu.upper() not in ky_tu_hex:
        la_hex = False
        break

if la_hex:
    print("Chuỗi này là chuỗi được viết trong hệ Hex.")
else:
    chuoi_hex = ""
    for ki_tu in chuoi_ky_tu:
        if ki_tu.upper() in ky_tu_hex:
            chuoi_hex += ki_tu.upper()

    if chuoi_hex:
        so_thap_phan = 0
        luy_thua = len(chuoi_hex) - 1
        for ki_tu in chuoi_hex:
            if ki_tu.isdigit():
                so_thap_phan += int(ki_tu) * (16 ** luy_thua)
            else:
                so_thap_phan += (ord(ki_tu) - 55) * (16 ** luy_thua)
            luy_thua -= 1
        print("Chuỗi được chuyển đổi sang số thập phân:", so_thap_phan)
    else:
        print("Không có ký tự nào thuộc hệ Hex trong chuỗi đã nhập.")
