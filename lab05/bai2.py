Str  = str(input('nhập chuỗi ở  đây:'))
so_ky_tu_khong_hop_le = sum(not (c.isalpha() or c.isdigit()) for c in Str)
print("Số ký tự không hợp lệ trong chuỗi là:", so_ky_tu_khong_hop_le)