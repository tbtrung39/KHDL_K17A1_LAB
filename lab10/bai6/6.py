import doicoso2
def main():
    try:
        # Nhập chuỗi ký tự
        input_str = input("Nhập một chuỗi ký tự: ")
        
        # Loại bỏ các ký tự không hợp lệ
        filtered_str = doicoso2.filter_hex_chars(input_str)
        
        # Xác định cơ số của chuỗi
        base = doicoso2.detect_base(filtered_str)
        print(f"Chuỗi {filtered_str} biểu diễn ở cơ số {base}.")
        
        if base == 2:
            # Chuyển đổi từ nhị phân sang thập phân
            doicoso2.convert_base_to_decimal(filtered_str, 2)
        elif base == 8:
            # Chuyển đổi từ cơ số 8 sang thập phân
            doicoso2.convert_base_to_decimal(filtered_str, 8)
        elif base == 16:
            # Chuyển đổi từ cơ số 16 sang thập phân
            doicoso2.convert_base_to_decimal(filtered_str, 16)
        else:
            print("Không thể chuyển đổi, cơ số không hợp lệ hoặc không xác định.")
        
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

if __name__ == "__main__":
    main()
