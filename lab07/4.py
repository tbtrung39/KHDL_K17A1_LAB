chieu_cao = [161, 182, 161, 154, 176, 170, 167, 171, 170, 174, 150, 142, 148, 165, 170, 178, 156, 145, 149, 163, 162, 159, 165, 165, 170, 180, 155, 153, 152, 162, 180, 168, 167, 170]
num_students = len(chieu_cao)
tong = sum(chieu_cao)/ len(chieu_cao)
liet_ke = set(chieu_cao)

print("Số lượng học sinh trong nhóm:", num_students)
print("tổng trung bình của sinh viên trong nhóm", tong)
print("liệt kê các chiều cao khác nhau", liet_ke)
