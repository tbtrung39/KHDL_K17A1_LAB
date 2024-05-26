from pk_9 import quanly

# Nhập thông tin của các mặt hàng từ bàn phím
hang_hoa = quanly.nhap_thong_tin_hang_hoa()

# Tính cột thành tiền cho mỗi mặt hàng
quanly.tinh_thanh_tien(hang_hoa)

# Tính cột thuế VAT cho mỗi mặt hàng
quanly.tinh_thue_VAT(hang_hoa)

# Sắp xếp các mặt hàng theo thứ tự giảm dần của thuế VAT và đưa ra màn hình kết quả trước và sau khi sắp xếp
quanly.sap_xep_giam_gian(hang_hoa)
