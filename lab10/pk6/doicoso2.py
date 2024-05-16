def loai_bo_ky_tu_khong_hop_le(string):
    """Loại bỏ các ký tự không hợp lệ từ chuỗi và in ra chuỗi kết quả."""
    valid_chars = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'}
    filtered_string = ''
    for char in string:
        if char.upper() in valid_chars:
            filtered_string += char
    print("Chuỗi kết quả sau khi loại bỏ các ký tự không hợp lệ:", filtered_string)
    return filtered_string

def kieu_co_so(string):
    """Cho biết một chuỗi số cho trước là biểu diễn cơ số mấy."""
    if all(char in '01' for char in string):
        print("Chuỗi số", string, "là biểu diễn cơ số 2.")
    elif all(char in '01234567' for char in string):
        print("Chuỗi số", string, "là biểu diễn cơ số 8.")
    elif all(char in '0123456789ABCDEF' for char in string.upper()):
        print("Chuỗi số", string, "là biểu diễn cơ số 16.")
    else:
        print("Chuỗi số", string, "không phải là biểu diễn của bất kỳ cơ số nào.")

def chuyen_co_so_to_10(string, base):
    """Chuyển đổi một chuỗi số từ cơ số base sang cơ số 10."""
    try:
        decimal = int(string, base)
        print("Chuỗi số", string, "được chuyển sang cơ số 10 là:", decimal)
        return decimal
    except ValueError:
        print("Không thể chuyển đổi chuỗi số", string, "từ cơ số", base, "sang cơ số 10.")
