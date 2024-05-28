from packages import xoa_kt_ko_hop_le,cs2_to_cs10,cs8_to_cs10
chuoi = input("nhập vào chuỗi: ")
cs2 = input("nhập vào chuỗi: ")
cs10 = input("nhập vào chuỗi: ")
print(f"chuỗi n sau khi xóa ký tự không hợp lệ: {xoa_kt_ko_hop_le(chuoi)}")
print(f"chuỗi n sau khi chuyển từ cơ số 2 qua cơ số 10 là {cs2_to_cs10(cs2)}")
print(f"chuỗi n sau khi chuyển từ cơ số 2 qua cơ số 10 là {cs8_to_cs10(cs10)}")