chuoi_nhap = input("Nhập chuỗi: ")
chu_so_hex = set('0123456789ABCDEF')
la_hex = all(char.upper() in chu_so_hex for char in chuoi_nhap)
if la_hex:
    print("Chuỗi bạn nhập là chuỗi hệ Hex.")
else:
    chuoi_clean = ''.join(char for char in chuoi_nhap if char.upper() in chu_so_hex)
    print("Chuỗi sau khi loại bỏ các ký tự không phải hex:", chuoi_clean)
    gia_tri_thap_phan = 0
    for chu_so in chuoi_clean:
        if chu_so.isdigit():
            gia_tri_thap_phan = 16 * gia_tri_thap_phan + int(chu_so)
        else:
            gia_tri_thap_phan = 16 * gia_tri_thap_phan + ord(chu_so.upper()) - ord('A') + 10
    print("Giá trị thập phân của chuỗi:", gia_tri_thap_phan)