chuoi = input("Nhập chuỗi ký tự: ")
so_ky_tu_so = 0
for ky_tu in chuoi:
    if ky_tu.isdigit():
        so_ky_tu_so += 1
print("Số lượng ký tự là số trong chuỗi là:", so_ky_tu_so)
