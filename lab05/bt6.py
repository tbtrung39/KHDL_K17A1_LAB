#nhập chuỗi hex
chuoi_hex = input("Nhập một chuỗi: ")

# Kiểm tra xem chuỗi có phải là chuỗi Hex không
chu_cai_hex = set("0123456789ABCDEF")
la_hex = all(c.upper() in chu_cai_hex for c in chuoi_hex)

if la_hex:
    print("Chuỗi đã nhập là một chuỗi Hex.")
else:
    print("Chuỗi không phải là một chuỗi Hex. Đang chuyển đổi sang số thập phân...")

    # Loại bỏ các ký tự không thuộc hệ Hex và chuyển đổi chuỗi còn lại sang số thập phân
    gia_tri_thap_phan = 0
    so_mu = len(chuoi_hex) - 1
    for chu_so in chuoi_hex:
        if chu_so.upper() in chu_cai_hex:
            gia_tri_thap_phan += chu_cai_hex.index(chu_so.upper()) * (16 ** so_mu)
            so_mu -= 1

    print("Giá trị thập phân của chuỗi là:", gia_tri_thap_phan)