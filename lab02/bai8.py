# Lương cơ bản
luong_can_ban = 1350000

# Nhập thâm niên công tác từ người dùng
tham_nien_cong_tac = int(input("Nhập thâm niên công tác (tháng): "))

# Xác định hệ số dựa trên thâm niên công tác
if tham_nien_cong_tac < 12:
    he_so = 2.34
elif tham_nien_cong_tac < 36:
    he_so = 3.33
elif tham_nien_cong_tac < 60:
    he_so = 3.66
else:
    he_so = 3.99

# Tính toán lương
luong = he_so * luong_can_ban

# In ra kết quả
print("Lương của nhân viên là:", luong, "đồng")