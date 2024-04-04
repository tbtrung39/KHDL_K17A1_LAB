chuoi = input("Nhập chuỗi ký tự: ")
so_ky_tu_khong_hop_le = 0
for ky_tu in chuoi:
    if ky_tu.isalpha() or ky_tu.isdigit():
        continue
    else:    
        so_ky_tu_khong_hop_le += 1
print("Số ký tự không phải là chữ cái tiếng Anh và không là số là:", so_ky_tu_khong_hop_le)