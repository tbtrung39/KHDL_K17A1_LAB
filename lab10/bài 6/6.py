import doicoso2
input_str = input("Nhập chuỗi ký tự: ")
clean_str, invalid_chars = doicoso2.remove_invalid_chars(input_str)
if invalid_chars:
    print("Các ký tự không hợp lệ:", ", ".join(invalid_chars))
print("Chuỗi sau khi loại bỏ ký tự không hợp lệ:", clean_str)
base = doicoso2.get_base(clean_str)
if base is None:
    print("Chuỗi không phải là số hợp lệ.")
else:
    print(f"Chuỗi {clean_str} là biểu diễn cơ số {base}")

    base10_value = doicoso2.convert_to_base10(clean_str, base)
    print(f"Giá trị cơ số 10 của {clean_str} là: {base10_value}")