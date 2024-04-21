# Khởi tạo từ điển để lưu thông tin sinh viên
sinh_vien = {}

# Nhập thông tin từng sinh viên
while True:
    ma_sv = input("Nhập mã sinh viên (6 ký tự số): ")
    if len(ma_sv) != 6 or not ma_sv.isdigit():
        print("Mã sinh viên phải có 6 ký tự số. Vui lòng nhập lại.")
        continue
    
    ten_sv = input("Nhập tên sinh viên: ")
    
    while True:
        diem = input("Nhập điểm số (từ 0 đến 10): ")
        try:
            diem = int(diem)
            if 0 <= diem <= 10:
                break
            else:
                print("Điểm số phải thuộc khoảng từ 0 đến 10. Vui lòng nhập lại.")
        except ValueError:
            print("Điểm số phải là một số nguyên. Vui lòng nhập lại.")
    
    # Lưu thông tin sinh viên vào từ điển
    sinh_vien[ma_sv] = {'Tên': ten_sv, 'Điểm': diem}
    
    tiep_tuc = input("Nhập thông tin sinh viên tiếp (C/K): ")
    if tiep_tuc.lower() != 'c':
        break

# Thực hiện sắp xếp các sinh viên theo giá trị điểm giảm dần
sinh_vien_sap_xep = sorted(sinh_vien.items(), key=lambda x: x[1]['Điểm'], reverse=True)
# In ra thông tin sinh viên đã sắp xếp
print("\nDanh sách sinh viên sau khi sắp xếp:")
for ma_sv, thong_tin in sinh_vien_sap_xep:
    print(f"Mã sinh viên: {ma_sv}, Tên: {thong_tin['Tên']}, Điểm: {thong_tin['Điểm']}")