def doc_va_ghi_tap_tin(ten_tap_tin, ten_tap_tin_ghi):
    try:
        with open(ten_tap_tin, 'r') as file:
            noi_dung = file.read()

        with open(ten_tap_tin_ghi, 'w') as file_ghi:
            file_ghi.write(noi_dung)
        
        print("Đã sao chép nội dung của tệp", ten_tap_tin, "sang tệp", ten_tap_tin_ghi)
    
    except FileNotFoundError:
        print("Lỗi: Không tìm thấy tệp", ten_tap_tin)
    except PermissionError:
        print("Lỗi: Không thể mở tệp", ten_tap_tin_ghi, "trong chế độ ghi.")

ten_tap_tin_doc = input("Nhập tên tệp tin cần đọc: ")
ten_tap_tin_ghi = input("Nhập tên tệp tin cần ghi: ")

doc_va_ghi_tap_tin(ten_tap_tin_doc, ten_tap_tin_ghi)
