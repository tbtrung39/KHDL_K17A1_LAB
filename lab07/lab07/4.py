chieu_cao = [161, 182, 161, 154, 176, 170, 167, 171, 170, 174, 150, 142, 148, 165, 170, 178, 156, 145, 149, 163,
             162, 159, 165, 165, 170, 180, 155, 159, 155, 153, 152, 162, 180, 168, 169, 168, 167, 170]

# a. Số lượng sinh viên trong nhóm
so_sinh_vien = len(chieu_cao)
print("Nhóm có", so_sinh_vien, "sinh viên.")

# b. Tính chiều cao trung bình của các sinh viên trong nhóm
chieu_cao_trung_binh = sum(chieu_cao) / so_sinh_vien
print("Chiều cao trung bình của các sinh viên trong nhóm là:", chieu_cao_trung_binh)

# c. Liệt kê các chiều cao khác nhau của sinh viên trong nhóm và tính chiều cao trung bình của nhóm
chieu_cao_khac_nhau = set(chieu_cao)
so_chieu_cao_khac_nhau = len(chieu_cao_khac_nhau)
print("Các chiều cao khác nhau của sinh viên trong nhóm là:", chieu_cao_khac_nhau)
print("Chiều cao trung bình của nhóm là:", chieu_cao_trung_binh)