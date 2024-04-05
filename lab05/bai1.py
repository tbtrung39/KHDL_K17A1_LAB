nhap_chuoi_ki_tu = input("nhập chuỗi kí tự:")
so = 0
for i in nhap_chuoi_ki_tu:
    if i.isdigit():
        so += 1
print(f"số các kí tự là số trong chuỗi kí tự là:{so}")