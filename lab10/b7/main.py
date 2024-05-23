from pk7 import tong, tao_danh_sach, kiem_tra_so_chinh_phuong, chia_het7

danh_sach = tao_danh_sach()
print("Danh sách ngẫu nhiên:", danh_sach)
print("Các số nguyên tố chia hết cho 7:", chia_het7(danh_sach))
print("Tổng các số chia hết cho 21:", tong(danh_sach))
print("Các số chính phương trong danh sách:", kiem_tra_so_chinh_phuong(danh_sach))
