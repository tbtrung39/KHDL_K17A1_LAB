# Danh sách chiều cao của sinh viên
chieu_cao_sinh_vien = [
    161, 182, 161, 154, 176, 170, 167, 171, 170, 174, 150, 142, 148, 165, 170, 
    178, 156, 145, 149, 163, 162, 159, 165, 165, 170, 180, 155, 159, 155, 153, 
    152, 162, 180, 168, 169, 168, 167, 170
]

# a. Số lượng sinh viên
so_luong_sinh_vien = len(chieu_cao_sinh_vien)

# b. Chiều cao trung bình
chieu_cao_trung_binh = sum(chieu_cao_sinh_vien) / so_luong_sinh_vien

# c. Các chiều cao duy nhất và chiều cao trung bình của nhóm
# chuyển veed set để k thay đổi đc data
chieu_cao_duy_nhat = set(chieu_cao_sinh_vien)
so_luong_chieu_cao_duy_nhat = len(chieu_cao_duy_nhat)
chieu_cao_trung_binh_nhom = sum(chieu_cao_duy_nhat) / so_luong_chieu_cao_duy_nhat

# In kết quả
print("a. Số lượng sinh viên trong nhóm:", so_luong_sinh_vien)
print("b. Chiều cao trung bình của các sinh viên trong nhóm:", chieu_cao_trung_binh)
print("c. Các chiều cao khác nhau của sinh viên trong nhóm:", chieu_cao_duy_nhat)
print("   Chiều cao trung bình của nhóm:", chieu_cao_trung_binh_nhom)