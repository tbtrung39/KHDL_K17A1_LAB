chieu_cao = [161, 182, 161, 154, 176, 170, 167, 171, 170, 174, 150, 142, 148, 165, 170, 178, 156, 145, 149, 163,
162, 159, 165, 165, 170, 180, 155, 159, 155, 153, 152, 162, 180, 168, 169, 168, 167, 170 ]
# Câu a
so_luong = len(chieu_cao)
print(f"Nhóm có {so_luong} sinh viên")
# Câu b
tong = sum(chieu_cao)
chieu_cao_trung_binh = tong / so_luong
print(f"Chiều cao trung bình của các sinh viên trong nhóm là: {chieu_cao_trung_binh}")
# Câu c
unique_cc = set(chieu_cao)
sl = len(unique_cc)
sx = sorted(unique_cc)
chieu_cao_trung_binh = tong / sl
print("Các chiều cao khác nhau:")
for chieu_cao in sx:
    print(chieu_cao)
print(f"Chiều cao trung bình là: {chieu_cao_trung_binh}")
