import qlyhanghoa

# Nhập thông tin các mặt hàng
danh_sach_hang_hoa = qlyhanghoa.nhap_thong_tin_hang_hoa()

# Tính thành tiền cho mỗi mặt hàng
qlyhanghoa.tinh_thanh_tien(danh_sach_hang_hoa)

# Tính thuế cho mỗi mặt hàng
qlyhanghoa.tinh_thue(danh_sach_hang_hoa)

# Hiển thị thông tin các mặt hàng trước khi sắp xếp
print("Thông tin các mặt hàng trước khi sắp xếp:")
qlyhanghoa.hien_thi_hang_hoa(danh_sach_hang_hoa)

# Sắp xếp các mặt hàng theo thứ tự giảm dần về thuế
qlyhanghoa.sap_xep_theo_thue(danh_sach_hang_hoa)

# Hiển thị thông tin các mặt hàng sau khi sắp xếp
print("\nThông tin các mặt hàng sau khi sắp xếp:")
qlyhanghoa.hien_thi_hang_hoa(danh_sach_hang_hoa)
