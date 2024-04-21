chieu_cao= [
    161, 182, 161, 154, 176, 170, 167, 171, 170, 174,
    150, 142, 148, 165, 170, 178, 156, 145, 149, 163,
    162, 159, 165, 165, 170, 180, 155, 159, 155, 153,
    152, 162, 180, 168, 169, 168, 167, 170
]
so_luong_hoc_sinh = len(chieu_cao)
chieu_cao_trung_binh = sum(chieu_cao) /so_luong_hoc_sinh
chieu_cao_duy_nhat = set(chieu_cao)
so_luong_chieu_cao_duy_nhat = len(chieu_cao_duy_nhat)
chieu_cao_trung_binh_nhom = sum(chieu_cao_duy_nhat) / so_luong_chieu_cao_duy_nhat
print("a. Số lượng sinh viên trong nhóm:", so_luong_hoc_sinh)
print("b. Chiều cao trung bình của các sinh viên trong nhóm:", chieu_cao_trung_binh)
print("c. Các chiều cao khác nhau của sinh viên trong nhóm:", chieu_cao_duy_nhat)
print("Chiều cao trung bình của nhóm:", chieu_cao_trung_binh_nhom)