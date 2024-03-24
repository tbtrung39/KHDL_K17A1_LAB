import math
# Nhập vào ngày, tháng, năm từ bàn phím
ngay = int(input("Nhập vào ngày: "))
thang = int(input("Nhập vào tháng: "))
nam = int(input("Nhập vào năm: "))

# Xác định số ngày trong tháng hiện tại
if thang == 2:
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        so_ngay_trong_thang = 29  # Tháng 2 năm nhuận
    else:
        so_ngay_trong_thang = 28  # Tháng 2 năm không nhuận
elif thang in [4, 6, 9, 11]:
    so_ngay_trong_thang = 30
else:
    so_ngay_trong_thang = 31

# Kiểm tra ngày và tăng giảm ngày, tháng, năm
if ngay < so_ngay_trong_thang:
    ngay_tiep_theo = ngay + 1
else:
    ngay_tiep_theo = 1
    if thang < 12:
        thang_tiep_theo = thang + 1
    else:
        thang_tiep_theo = 1
        nam_tiep_theo = nam + 1

# Xuất ra ngày tiếp theo
print(f"Ngày tiếp theo là: {ngay_tiep_theo}/{thang_tiep_theo}/{nam_tiep_theo}")