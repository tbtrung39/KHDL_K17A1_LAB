Str  = str(input("Nhap chuoi: "))
so_ky_tu_khong_hop_le = sum(not (c.isalpha() or c.isdigit()) for c in Str)
print("So ky tu khong hop le trong chuoi la:", so_ky_tu_khong_hop_le)