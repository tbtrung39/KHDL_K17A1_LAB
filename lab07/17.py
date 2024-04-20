
sinh_vien = {}
so_sinh_vien = int(input("Nhập số lượng sinh viên: "))
for i in range(so_sinh_vien):
    ma_sinh_vien = input("Nhập mã số sinh viên (6 kí tự số): ")
    ten_sinh_vien = input("Nhập tên sinh viên: ")
    diem = float(input("Nhập điểm số (từ 0 đến 10): "))
    diem = round(diem)  
    sinh_vien[ma_sinh_vien] = (ten_sinh_vien, diem)
sorted_sinh_vien = sorted(sinh_vien.items(), key=lambda x: x[1][1], reverse=True)
print("Danh sách sinh viên theo thứ tự giảm dần của điểm số:")
for sv in sorted_sinh_vien:
    print(f"Mã sinh viên: {sv[0]}, Tên sinh viên: {sv[1][0]}, Điểm số: {sv[1][1]}")
