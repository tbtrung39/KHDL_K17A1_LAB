chuoi = input("Nhập chuỗi ký tự: ")
hexx = set("0123456789ABCDEF")
is_hex = all(char.upper() in hexx for char in chuoi)
if is_hex:
    print("Chuỗi đã nhập được viết trong hệ Hex")
else:
    print("Chuỗi không phải là chuỗi được viết trong hệ Hex")
    hex_chuoi = ''.join(char for char in chuoi if char.upper() in set("0123456789ABCDEF"))
    thap_phan = int(hex_chuoi, 16)
    print("Số thập phân là:", thap_phan)
