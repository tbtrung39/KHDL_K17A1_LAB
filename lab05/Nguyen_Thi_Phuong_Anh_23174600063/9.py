chuoi1 = input("Nhập chuỗi ký tự thứ nhất: ")
chuoi2 = input("Nhập chuỗi ký tự thứ hai: ")
chuoi_chung_max = ""

for i in range(len(chuoi1)):
    for j in range(i + 1, len(chuoi1) + 1):
        phan_tu = chuoi1[i:j]
        if phan_tu in chuoi2 and len(phan_tu) > len(chuoi_chung_max):
            chuoi_chung_max= phan_tu

if chuoi_chung_max:
    print(f"Chuỗi ký tự con chung dài nhất là: {chuoi_chung_max}")
else:
    print("Không có chuỗi ký tự con chung nào.")