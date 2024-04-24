# viết chương trình nhập thông tin sinh viên gồm :mã sinh viên (6 ký tự số), tên sinh viên, điểm số và lưu thông tin trong 1 từ điển . điểm số làm trong số nguyên quen thuộc {0,1,2,...10} thống kê và sắp xếp sinh viên theo giá trị điểm giảm dần 
danh_sach_sinh_vien = {"mã sinh viên": [], "tên sinh viên": [], "điểm số": []}

while True:
    ma_sv = input("Nhập mã sinh viên (6 ký tự số): ")
    ten_sv = input("Nhập tên sinh viên: ")
    diem = int(input("Nhập điểm số (từ 0 đến 10): "))

    danh_sach_sinh_vien["mã sinh viên"].append(ma_sv)
    danh_sach_sinh_vien["tên sinh viên"].append(ten_sv)
    danh_sach_sinh_vien["điểm số"].append(diem)

    choice = input("Bạn có muốn nhập thông tin sinh viên khác không? (yes/no): ")
    if choice.lower() != "yes":
        break
sorted_danh_sach_sinh_vien = sorted(range(len(danh_sach_sinh_vien["mã sinh viên"])), key=lambda x: danh_sach_sinh_vien["điểm số"][x], reverse=True)
print("Danh sách sinh viên sau khi sắp xếp theo điểm giảm dần:")
for index in sorted_danh_sach_sinh_vien:
    print("Mã SV:", danh_sach_sinh_vien["mã sinh viên"][index], "- Tên SV:", danh_sach_sinh_vien["tên sinh viên"][index], "- Điểm số:", danh_sach_sinh_vien["điểm số"][index])
    
    
    