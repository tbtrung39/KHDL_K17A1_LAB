def doc_va_ghi_tap_tin(ten_tap_tin):
    try:
        with open(ten_tap_tin, 'r') as file:
            noi_dung = file.read()

        with open('copy.dat', 'w') as file_copy:
            file_copy.write(noi_dung)
        
        print("Đã sao chép nội dung của tệp", ten_tap_tin, "sang tập tin copy.dat.")
    
    except FileNotFoundError:
        print("Lỗi: Không tìm thấy tệp", ten_tap_tin)

ten_tap_tin = input("Nhập tên tập tin: ")

doc_va_ghi_tap_tin(ten_tap_tin)
