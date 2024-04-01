chuoi = input("Nhập chuỗi ký tự: ")
so_ky_tu_khong_hop_le = 0
for ky_tu in chuoi:
    if not ky_tu.isalpha() and not ky_tu.isdigit():
        so_ky_tu_khong_hop_le += 1
print("Số ký tự không phải là chữ cái tiếng Anh và không là số là:", so_ky_tu_khong_hop_le)
