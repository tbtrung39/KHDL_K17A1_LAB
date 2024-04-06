chuoi= input("Nhập chuỗi: ")
chuoi_hex = chuoi.replace(' ', '')  
chuoi_hex = chuoi_hex.lower() 
if all(c in '0123456789abcdef' for c in chuoi_hex):
    print("Chuỗi này là hệ hex.")
    so_thap_phan = int(chuoi_hex, 16)
    print("Chuyển đổi sang hệ thập phân:", so_thap_phan)
else:
    print("Chuỗi này không phải là hệ hex.")