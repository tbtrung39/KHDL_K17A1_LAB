string = input("Nhập chuỗi ký tự: ")
hex_chars = set('0123456789ABCDEF')
if all(char.upper() in hex_chars for char in string):
    print("Chuỗi là chuỗi Hex.")
    print("Chuyển sang số thập phân:", int(string, 16))
else:
    filtered_hex = ''.join(char for char in string if char.upper() in '0123456789ABCDEF')
    print("Chuỗi không phải là chuỗi Hex.")
    print("Chuỗi sau khi loại bỏ các ký tự không thuộc hệ Hex:", filtered_hex)
    print("Chuyển chuỗi còn lại sang số thập phân:", int(filtered_hex, 16))